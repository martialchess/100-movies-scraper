import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")
movies = soup.find_all("h3", class_="title")
movie_titles = [movie.getText() for movie in movies]
movie_titles.reverse()
with open("movies.txt", "w", encoding="utf-8") as file:
    for title in movie_titles:
        file.write(f"{title}\n")

print(movie_titles)
# print(soup.prettify())
