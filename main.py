from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text

soup = BeautifulSoup(movies, "html.parser")

all_films = soup.find_all(name="h3", class_="title")

film_titles = [film.getText() for film in all_films]
films = film_titles[::-1]

with open("movies.txt", "w") as file:
    for film in films:
        file.write(f"{film}\n")






