import pandas as pd
import requests as requests
from bs4 import BeautifulSoup
import csv

urls = [
    "https://www.vlr.gg/303087/evil-geniuses-vs-loud-champions-tour-2024-americas-kickoff-sf/?game=160718&tab=overview",
    "https://www.vlr.gg/303087/evil-geniuses-vs-loud-champions-tour-2024-americas-kickoff-sf/?game=160719&tab=overview",
    "https://www.vlr.gg/303087/evil-geniuses-vs-loud-champions-tour-2024-americas-kickoff-sf/?game=160720&tab=overview",
    "https://www.vlr.gg/303088/nrg-esports-vs-sentinels-champions-tour-2024-americas-kickoff-sf/?game=160721&tab=overview",
    "https://www.vlr.gg/303088/nrg-esports-vs-sentinels-champions-tour-2024-americas-kickoff-sf/?game=160722&tab=overview",
    "https://www.vlr.gg/303088/nrg-esports-vs-sentinels-champions-tour-2024-americas-kickoff-sf/?game=160723&tab=overview",
    "https://www.vlr.gg/303086/loud-vs-sentinels-champions-tour-2024-americas-kickoff-gf/?game=160715&tab=overview",
    "https://www.vlr.gg/303086/loud-vs-sentinels-champions-tour-2024-americas-kickoff-gf/?game=160716&tab=overview",
    "https://www.vlr.gg/303086/loud-vs-sentinels-champions-tour-2024-americas-kickoff-gf/?game=160717&tab=overview",
    "https://www.vlr.gg/303086/loud-vs-sentinels-champions-tour-2024-americas-kickoff-gf/?game=160724&tab=overview",
    "https://www.vlr.gg/303086/loud-vs-sentinels-champions-tour-2024-americas-kickoff-gf/?game=160725&tab=overview"
]

# All data collected
all_data = []

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the current URL
        
        team_names = [team.text.strip() for team in soup.find_all('div', class_='wf-title-med')]
        map_name = [map.text.strip().split('\t')[0] for map in soup.find_all('div', class_='map')]
        agent_names = [a.find('img').get('alt') for a in soup.find_all("span", {"class": "stats-sq mod-agent small"}) if a.find('img')]
        map_results = [result.text.strip().split('\t')[0] for result in soup.find('div', class_='score')]
        economy_ratings = [rating.text.strip() for rating in soup.find_all('div', class_='wf-table-inset mod-econ')]

        # Create a list to store all the data
        url_data = [
            team_names,
            map_name,
            agent_names,
            map_results,
            economy_ratings
        ]

        # Append the dictionary to the list
        all_data.append(url_data)
    else:
        print(f"Failed to retrieve the data from {url}")

# Save Data to a CSV File
with open ('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Team Names', 'Map Played', 'Agents Played', 'Map Results', 'Economy Rating'])
    for data_row in all_data:
        writer.writerow(data_row)
