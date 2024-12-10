import os
import json
import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('LEADERBOARD_URL')
cookies = {"session": os.getenv('SESSION_COOKIE')}
json_file_path = "leaderboard.json"
html_file_path = "leaderboard.html"
update_interval = 15


def save_json(data, file_path):
    """Saves the JSON data to a file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_json(file_path):
    """Loads the JSON file."""
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def is_update_needed(file_path, interval_minutes):
    """Check if the file needs to be updated based on the interval."""
    if not os.path.exists(file_path):
        return True  # File does not exist -> update needed
    file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
    return datetime.now() - file_mtime > timedelta(minutes=interval_minutes)


def calculate_daily_scores(data):
    """Calculates scores for each day with separate scores for Part 1 and Part 2."""
    scores = {}
    members = data["members"]

    # Collect all days and ensure all participants are included
    all_days = set()
    for member_data in members.values():
        all_days.update(member_data.get("completion_day_level", {}).keys())

    for day in all_days:
        scores[day] = []

    for member_id, member_data in members.items():
        name = member_data.get("name", "N/A")
        completion = member_data.get("completion_day_level", {})

        for day in all_days:
            levels = completion.get(day, {})
            part1_ts = levels.get("1", {}).get("get_star_ts", None)
            part2_ts = levels.get("2", {}).get("get_star_ts", None)

            scores[day].append({
                "Name": name,
                "Part 1 Time": part1_ts,
                "Part 2 Time": part2_ts,
                "Part 1 Points": 0,  # Placeholder
                "Part 2 Points": 0,  # Placeholder
                "Total Points": 0,   # Placeholder
                "Part 1 Rank": None,  # Placeholder
                "Part 2 Rank": None   # Placeholder
            })

    # Calculate points and ranks
    for day, members_scores in scores.items():
        # Calculate Part 1 ranks and points
        part1_sorted = sorted(
            members_scores, key=lambda x: x["Part 1 Time"] or float('inf')
        )
        for i, member in enumerate(part1_sorted):
            if member["Part 1 Time"]:  # Assign points only if Part 1 is completed
                member["Part 1 Rank"] = int(i + 1)
                member["Part 1 Points"] = len(members_scores) - i

        # Calculate Part 2 ranks and points
        part2_sorted = sorted(
            members_scores, key=lambda x: x["Part 2 Time"] or float('inf')
        )
        for i, member in enumerate(part2_sorted):
            if member["Part 2 Time"]:  # Assign points only if Part 2 is completed
                member["Part 2 Rank"] = int(i + 1)
                member["Part 2 Points"] = len(members_scores) - i

        # Calculate total points
        for member in members_scores:
            member["Total Points"] = member["Part 1 Points"] + member["Part 2 Points"]

    return scores


def generate_html_with_tabs(data, file_path):
    """Generates an HTML file with tabs for each day and a total overview."""
    members = data["members"]
    daily_scores = calculate_daily_scores(data)

    # Total Tab Data
    total_data = []
    for member_id, member_data in members.items():
        total_data.append({
            "Name": member_data.get("name", "N/A"),
            "Stars": member_data.get("stars", 0),
            "Local Score": member_data.get("local_score", 0)
        })

    # Create DataFrame for Total Tab and add rank
    total_df = pd.DataFrame(total_data).sort_values(by="Local Score", ascending=False).reset_index(drop=True)
    total_df.insert(0, "Rank", total_df.index + 1)  # Add rank as the first column

    total_html_table = total_df.to_html(index=False, classes="sortable", border=0)

    # Generate HTML content for tabs
    tabs = []
    contents = []

    # Add Total Tab
    tabs.append(f'<button class="tablinks" onclick="openTab(event, \'Total\')">Total</button>')
    contents.append(f'''
        <div id="Total" class="tabcontent">
            <h2>Total Overview</h2>
            {total_html_table}
        </div>
    ''')

    # Day Tabs
    for day, scores in sorted(daily_scores.items(), key=lambda x: int(x[0])):
        df = pd.DataFrame(scores)

        # Convert timestamps to readable dates in a specific timezone
        for column in ["Part 1 Time", "Part 2 Time"]:
            df[column] = (pd.to_datetime(df[column], unit="s", errors="coerce")
                          .dt.tz_localize('UTC')  # Set UTC as the source timezone
                          .dt.tz_convert('Europe/Berlin')  # Convert to desired timezone
                          .dt.strftime('%Y-%m-%d %H:%M:%S')  # Format as string
                          .fillna('-'))  # Replace missing values with '-'

        # Ensure ranks are integers, missing values are replaced with '-'
        rank_columns = ["Part 1 Rank", "Part 2 Rank"]
        for col in rank_columns:
            df[col] = df[col].apply(lambda x: int(x) if pd.notnull(x) else '-')

        # Replace NaN points with '-', and sort by Total Points
        point_columns = ["Part 1 Points", "Part 2 Points", "Total Points"]
        for col in point_columns:
            df[col] = df[col].apply(lambda x: int(x) if pd.notnull(x) else '-')

        # Sort by Total Points in descending order
        df = df.sort_values(by="Total Points", ascending=False)
        df.insert(0, "Rank", total_df.index + 1)

        # Rearrange columns in the desired order
        df = df[[
            "Rank", "Name", "Part 1 Rank", "Part 1 Points",
            "Part 2 Rank", "Part 2 Points", "Total Points",
            "Part 1 Time", "Part 2 Time"
        ]]

        html_table = df.to_html(index=False, classes="sortable", border=0)
        tabs.append(f'<button class="tablinks" onclick="openTab(event, \'Day {day}\')">Day {day}</button>')
        contents.append(f'''
            <div id="Day {day}" class="tabcontent">
                <h2>Day {day} Overview</h2>
                {html_table}
            </div>
        ''')

    # Save HTML with tabs
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Advent of Code Leaderboard</title>
            <style>
                body {{ font-family: Arial, sans-serif; }}
                .tab {{ overflow: hidden; border-bottom: 1px solid #ccc; }}
                .tab button {{ background-color: inherit; border: none; cursor: pointer; padding: 10px 15px; font-size: 16px; }}
                .tab button:hover {{ background-color: #ddd; }}
                .tab button.active {{ background-color: #ccc; }}
                .tabcontent {{ display: none; padding: 20px; border: 1px solid #ccc; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: center; }}
                th {{ background-color: #f4f4f4; cursor: pointer; }}
                tr:nth-child(even) {{ background-color: #f9f9f9; }}
                tr:hover {{ background-color: #f1f1f1; }}
            </style>
            <script>
                function sortTable(table, colIndex, asc) {{
                    const rows = Array.from(table.querySelectorAll("tbody tr"));

                    const comparer = (rowA, rowB) => {{
                        const cellA = rowA.children[colIndex].innerText || rowA.children[colIndex].textContent;
                        const cellB = rowB.children[colIndex].innerText || rowB.children[colIndex].textContent;

                        // Handle '-' and place it at the bottom
                        if (cellA === '-' && cellB === '-') return 0; // Both are '-', keep the order
                        if (cellA === '-') return 1; // Move '-' to the bottom
                        if (cellB === '-') return -1; // Move '-' to the bottom

                        // Otherwise, sort normally
                        const valA = isNaN(cellA) ? cellA : parseFloat(cellA);
                        const valB = isNaN(cellB) ? cellB : parseFloat(cellB);

                        return asc ? (valA > valB ? 1 : -1) : (valA > valB ? -1 : 1);
                    }};

                    rows.sort(comparer).forEach(row => table.querySelector("tbody").appendChild(row));
                }}

                document.addEventListener("DOMContentLoaded", () => {{
                    document.querySelectorAll("th").forEach(header => {{
                        header.addEventListener("click", () => {{
                            const table = header.closest("table");
                            const colIndex = Array.from(header.parentNode.children).indexOf(header);
                            const asc = header.classList.toggle("asc");
                            sortTable(table, colIndex, asc);
                        }});
                    }});

                    const defaultTab = document.querySelector(".tablinks");
                    if (defaultTab) defaultTab.click();
                }});

                function openTab(evt, tabName) {{
                    const tabContents = document.querySelectorAll(".tabcontent");
                    tabContents.forEach(content => content.style.display = "none");

                    const tabLinks = document.querySelectorAll(".tablinks");
                    tabLinks.forEach(link => link.classList.remove("active"));

                    document.getElementById(tabName).style.display = "block";
                    evt.currentTarget.classList.add("active");
                }}
            </script>
        </head>
        <body>
            <h1>Advent of Code Leaderboard</h1>
            <div class="tab">
                {" ".join(tabs)}
            </div>
            {" ".join(contents)}
        </body>
        </html>
        """)


if __name__ == '__main__':
    if is_update_needed(json_file_path, update_interval):
        print("JSON file will be updated...")
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            data = response.json()
            save_json(data, json_file_path)
            print("JSON file successfully updated.")
        else:
            raise Exception(f"Error fetching data: {response.status_code}")
    else:
        print("JSON file is up-to-date. No update needed.")

    data = load_json(json_file_path)
    if data:
        generate_html_with_tabs(data, html_file_path)
        print(f"HTML saved as '{html_file_path}'")
    else:
        print("No JSON file found.")
