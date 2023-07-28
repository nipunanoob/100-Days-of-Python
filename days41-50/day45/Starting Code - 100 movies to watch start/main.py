import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
movie_titles = soup.find_all("h3",class_="title")
movie_titles.reverse()

for movie in movie_titles:
    print(movie.text)

with open("movies.txt","w",encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie.text}\n")
