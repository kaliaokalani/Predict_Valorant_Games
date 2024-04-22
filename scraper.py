import pandas as pd
import requests as requests
from bs4 import BeautifulSoup 

urls = [
    "https://www.vlr.gg/297256/t1-vs-paper-rex-champions-tour-2024-pacific-kickoff-playoffs-sf"
    "https://www.vlr.gg/297257/drx-vs-gen-g-champions-tour-2024-pacific-kickoff-playoffs-sf"
    "https://www.vlr.gg/297258/paper-rex-vs-gen-g-champions-tour-2024-pacific-kickoff-playoffs-gf"
    "https://www.vlr.gg/303086/loud-vs-sentinels-champions-tour-2024-americas-kickoff-gf"
    "https://www.vlr.gg/303087/evil-geniuses-vs-loud-champions-tour-2024-americas-kickoff-sf"
    "https://www.vlr.gg/303088/nrg-esports-vs-sentinels-champions-tour-2024-americas-kickoff-sf"
    "https://www.vlr.gg/303093/team-heretics-vs-natus-vincere-champions-tour-2024-emea-kickoff-playoffs-sf"
    "https://www.vlr.gg/303094/fnatic-vs-karmine-corp-champions-tour-2024-emea-kickoff-playoffs-sf"
    "https://www.vlr.gg/303095/team-heretics-vs-karmine-corp-champions-tour-2024-emea-kickoff-playoffs-gf"
    "https://www.vlr.gg/298833/funplus-phoenix-vs-dragon-ranger-gaming-champions-tour-2024-china-kickoff-sf"
    "https://www.vlr.gg/298834/edward-gaming-vs-trace-esports-champions-tour-2024-china-kickoff-sf"
    "https://www.vlr.gg/298835/funplus-phoenix-vs-edward-gaming-champions-tour-2024-china-kickoff-gf"
    "https://www.vlr.gg/312777/gen-g-vs-paper-rex-champions-tour-2024-masters-madrid-ubsf"
    "https://www.vlr.gg/312776/sentinels-vs-loud-champions-tour-2024-masters-madrid-ubsf"
    "https://www.vlr.gg/312778/gen-g-vs-sentinels-champions-tour-2024-masters-madrid-ubf"
    "https://www.vlr.gg/312780/paper-rex-vs-loud-champions-tour-2024-masters-madrid-lr1"
    "https://www.vlr.gg/312781/sentinels-vs-paper-rex-champions-tour-2024-masters-madrid-lbf"
    "https://www.vlr.gg/312779/gen-g-vs-sentinels-champions-tour-2024-masters-madrid-gf"
]