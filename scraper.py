import pandas as pd
import requests as requests
from bs4 import BeautifulSoup

urls = [
    "https://www.vlr.gg/297256/t1-vs-paper-rex-champions-tour-2024-pacific-kickoff-playoffs-sf",
    "https://www.vlr.gg/297257/drx-vs-gen-g-champions-tour-2024-pacific-kickoff-playoffs-sf",
    "https://www.vlr.gg/297258/paper-rex-vs-gen-g-champions-tour-2024-pacific-kickoff-playoffs-gf",
    "https://www.vlr.gg/303086/loud-vs-sentinels-champions-tour-2024-americas-kickoff-gf",
    "https://www.vlr.gg/303087/evil-geniuses-vs-loud-champions-tour-2024-americas-kickoff-sf",
    "https://www.vlr.gg/303088/nrg-esports-vs-sentinels-champions-tour-2024-americas-kickoff-sf",
    "https://www.vlr.gg/303093/team-heretics-vs-natus-vincere-champions-tour-2024-emea-kickoff-playoffs-sf",
    "https://www.vlr.gg/303094/fnatic-vs-karmine-corp-champions-tour-2024-emea-kickoff-playoffs-sf",
    "https://www.vlr.gg/303095/team-heretics-vs-karmine-corp-champions-tour-2024-emea-kickoff-playoffs-gf",
    "https://www.vlr.gg/298833/funplus-phoenix-vs-dragon-ranger-gaming-champions-tour-2024-china-kickoff-sf",
    "https://www.vlr.gg/298834/edward-gaming-vs-trace-esports-champions-tour-2024-china-kickoff-sf",
    "https://www.vlr.gg/298835/funplus-phoenix-vs-edward-gaming-champions-tour-2024-china-kickoff-gf",
    "https://www.vlr.gg/312777/gen-g-vs-paper-rex-champions-tour-2024-masters-madrid-ubsf",
    "https://www.vlr.gg/312776/sentinels-vs-loud-champions-tour-2024-masters-madrid-ubsf",
    "https://www.vlr.gg/312778/gen-g-vs-sentinels-champions-tour-2024-masters-madrid-ubf",
    "https://www.vlr.gg/312780/paper-rex-vs-loud-champions-tour-2024-masters-madrid-lr1",
    "https://www.vlr.gg/312781/sentinels-vs-paper-rex-champions-tour-2024-masters-madrid-lbf",
    "https://www.vlr.gg/312779/gen-g-vs-sentinels-champions-tour-2024-masters-madrid-gf"
]

# All data collected
all_data = []

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the current URL
        
        team_names = [team.text.strip() for team in soup.find_all('div', class_='team')]
        agents_played = [agent.text.strip() for agent in soup.find_all('div', class_='col-md-5')]
        map_results = [result.text.strip() for result in soup.find_all('div', class_='map-score')]
        economy_ratings = [rating.text.strip() for rating in soup.find_all('div', class_='economy-score')]

        # Create a dictionary to store all the data
        url_data = {
            "URL" : url,
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
