# Advent of Code
Welcome to my collection of solutions for the **Advent of Code** challenges!  
This repository contains my daily puzzle solutions, showcasing different approaches and techniques to tackle each problem.

## Bonus: Leaderboard Viewer
In addition to the solutions, this repository includes a tool to fetch and display data from a private Advent of Code leaderboard. 
The leaderboard is presented as an interactive HTML file with sortable tables and daily performance breakdowns.

---

# Advent of Code Leaderboard Viewer
A script to fetch, store, and display data from a private Advent of Code leaderboard as an interactive HTML file.

## Requirements
- **Python 3.8+**
- Libraries: `pandas`, `requests`, `python-dotenv`  
  Install with:
  ```bash
  pip install pandas requests python-dotenv

## Setup
1. **Clone the Repository**  
   Download the script and extract it.
2. **Get Your Leaderboard URL**  
   Copy the URL of your private leaderboard (e.g., `https://adventofcode.com/2024/leaderboard/private/view/123456.json`).
3. **Obtain Session Cookie**  
   - Log in to [Advent of Code](https://adventofcode.com).  
   - Open your browser’s developer tools (`F12`).  
   - Find the `session` cookie in the `Cookies` section.
4. **Create a `.env` File**  
   Add your leaderboard URL and session cookie to a `.env` file in the same directory:
   ```plaintext
   LEADERBOARD_URL=<your-leaderboard-url, e.g. https://adventofcode.com/2024/leaderboard/private/view/123456.json>
   SESSION_COOKIE=<your-session-cookie>
   ```

## Usage
1. **Run the Script**  
   ```bash
   python get_private_leaderboard.py
2. **View the HTML**  
   Open the generated `leaderboard.html` file in your browser.


## Customization
1. **Update Interval**  
   Change the `update_interval` variable in the script (default: 15 minutes). This keeps the requests limited.
2. **Timezone**  
   Adjust the `.dt.tz_convert('Europe/Berlin')` line in the script to your desired timezone.


## Example Output
### Total View
| Rank | Name   | Stars | Local Score |
|------|--------|-------|-------------|
| 1    | Alice  | 10    | 120         |
| 2    | Bob    | 8     | 100         |

### Day Tabs
| Name   | Part 1 Rank | Part 1 Points | Part 2 Rank | Total Points | Part 1 Time       | Part 2 Time       |
|--------|-------------|---------------|-------------|--------------|-------------------|-------------------|
| Alice  | 1           | 10            | 2           | 18           | 2024-12-01 00:01  | 2024-12-01 00:05  |
| Bob    | 2           | 8             | 1           | 18           | 2024-12-01 00:02  | 2024-12-01 00:04  |



<!-- CONTACT -->
# Contact
[![LinkedIn][linkedin-shield]][linkedin-url] [![Github][github-shield]][github-url] [![Youtube][youtube-shield]][youtube-url]

Please share your thoughts and connect with me on [linkedin](https://linkedin.com/in/viet-anh-le-cong) 

Viet Anh Le Cong - [@linkedin](https://linkedin.com/in/viet-anh-le-cong) - [hello@v1et4nh.de](mailto:hello@v1et4nh.de)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[github-shield]: https://img.shields.io/github/followers/v1et4nh?label=Github&style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555&logoColor=blue
[youtube-shield]: https://img.shields.io/endpoint?color=red&label=Youtube&logoColor=red&style=for-the-badge&url=https%3A%2F%2Fyoutube-channel-badge-v1.vercel.app%2Fapi%2Fsubscriber
[github-url]: https://github.com/v1et4nh
[linkedin-url]: https://linkedin.com/in/viet-anh-le-cong
[youtube-url]: https://www.youtube.com/channel/UC7PMQLO9HIZ5zEogOkHp8yw