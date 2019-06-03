from bs4 import BeautifulSoup
import requests
import pandas as pd


page = requests.get("http://www.hltv.org/ranking/teams/")
soup = BeautifulSoup(page.content, 'html.parser')   
teams = soup.find("div", {"class": "ranking"})

dicts = {}
df = pd.DataFrame()
for team in teams.find_all("div", {"class": "ranked-team standard-box"}):
    
    newteam = team.find('div', {"class": "ranking-header"}).select('.name')[0].text.strip()
    dicts['teams'] = newteam

    teamlist = [] 
    for player_div in team.find_all("td", {"class": "player-holder"}):
        player = player_div.find('img', {'class': 'playerPicture'})['title']
        teamlist.append(player)
        
    dicts['players'] = teamlist
    
    ts = pd.DataFrame.from_dict(dicts)
    df = df.append(ts)

df = df.reset_index(drop=True)
print(df)    


    