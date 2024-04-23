import pandas as pd
import requests as requests
from bs4 import BeautifulSoup

urls = [
    "https://www.vlr.gg/303087/evil-geniuses-vs-loud-champions-tour-2024-americas-kickoff-sf/?game=160718&tab=overview"
]

# All data collected
all_data = []

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the current URL
        
        team_names = [team.text.strip() for team in soup.find_all('div', class_='wf-title-med')]
        agents_played = [agent.text.strip() for agent in soup.find_all('div', class_='vm-stats-game')]
        map_results = [result.text.strip() for result in soup.find_all('div', class_='map-score')]
        economy_ratings = [rating.text.strip() for rating in soup.find_all('div', class_='economy-score')]

        # Create a dictionary to store all the data
        url_data = {
            "Team Names": team_names,
            "Agents Played": agents_played,
            "Map Results": map_results,
            "Economy Ratings": economy_ratings
        }

        # Append the dictionary to the list
        all_data.append(url_data)
    else:
        print(f"Failed to retrieve the data from {url}")

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(all_data)

# Display
print(df)
