import requests
from bs4 import BeautifulSoup
import pandas as pd

# IMDb Top 250 movies URL
url = 'https://www.imdb.com/chart/top/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

movies = []

for movie in soup.find_all('h3', class_='ipc-title__text'):
    title = movie.text
    movies.append(title)

# Convert to DataFrame
movies_df = pd.DataFrame(movies)
movies_df.to_csv('moviesdetail.csv')

print(movies_df)