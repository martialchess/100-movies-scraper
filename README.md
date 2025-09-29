## 100 Movies that You Must Watch

# Objective

Scrape the top 100 movies of all time from a website. Generate a text file called `movies.txt` that lists the movie titles in ascending order (starting from 1). 
The result should look something like this:

```
1) The Godfather
2) The Empire Strikes Back
3) The Dark Knight
4) The Shawshank Redemption
... and so on
```
The central idea behind this project is to be able to use BeautifulSoup to obtain some data - like movie titles - from a website like Empire's (or from, say Timeout or Stacker that have curated similar lists). 

### ⚠️ Important: Use the Internet Archive's URL

Since websites change very frequently, **use this link** 
```
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
```
from the Internet Archive's Wayback machine. That way your work will match the solution video.

(Do *not* use https://www.empireonline.com/movies/features/best-movies-2/ which I've used in the screen recording)

# Solution

You can find the code from my walkthrough and solution as a downloadable .zip file in the course resources for this lesson. 

# Additional Project Information

## Features
- Fetches movie data from a web page using `requests` and `BeautifulSoup`
- Extracts movie titles from the HTML
- Saves the list of movies to `movies.txt`

## How It Works
1. The script sends a request to the Empire Online archive page.
2. It parses the HTML to find all movie titles listed in `<h3 class="title">` tags.
3. The titles are reversed (so the first movie is at the top of the list).
4. The final list is written to `movies.txt`, one title per line.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

Install dependencies with:
```bash
pip install requests beautifulsoup4
```

## Usage
Run the script:
```bash
python main.py
```
Check the `movies.txt` file for the list of movies.

## Files
- `main.py`: The main Python script
- `movies.txt`: Output file containing the movie titles
- `README.md`: Project documentation

## License
This project is for educational purposes.