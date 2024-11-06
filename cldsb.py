import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

states = []
populations = []

# Iterate through the rows of the table to extract the required information
for row in soup.select("table.wikitable.sortable tbody tr"):
    # Get the state name from the <th> element with scope="row"
    state = row.select_one("th[scope='row'] a")
    # Get the population from the <td> element
    population = row.select_one("td:nth-of-type(5)")
    
    if state and population:
        states.append(state.get_text())
        populations.append(population.get_text().strip())
    


states_df = pd.DataFrame({
    'State': states,
    'Population': populations
})

# Save the DataFrame to a CSV file
states_df.to_csv('us_states_population.csv', index=False)

print(states_df)

