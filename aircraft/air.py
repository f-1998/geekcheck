import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
aircraft = []

aircraft = []

# Select rows with aircraft data
for row in soup.select("table.wikitable tr"):
    # Extract the first link in each row with a title attribute (aircraft name)
    link = row.find("a", title=True)
    if link:
        aircraft.append(link.get("title"))

# Convert to DataFrame for easy handling and display
df = pd.DataFrame(aircraft, columns=["Aircraft Name"])

# Save the DataFrame to a CSV file
df.to_csv('indianaircraft.csv', index=False)

# Display the DataFrame
print(df)