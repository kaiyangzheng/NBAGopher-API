"""
Puts and updates data into player advanced season database
"""
import pandas as pd
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

BASE = "https://nbagopher-api.herokuapp.com/"
BBR_BASE = "https://basketball-reference.com"
SEASON = 2021
BBREF_SEASON = SEASON+1
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']


def advanced_stats_table(bbr_id):
    html_text = urlopen(f'http://www.basketball-reference.com{bbr_id}')
    soup = BeautifulSoup(html_text.read(), 'lxml')
    table = soup.find('table', {'id': 'advanced'})
    advanced_stats_table = pd.read_html(str(table))[0]
    advanced_stats_table = advanced_stats_table.fillna(0)
    return advanced_stats_table


def main():
    for player in player_data:
        if (player['isActive']):
            player_id = player['personId']
            try:
                bbr_id = requests.request(
                    'GET', f"{BASE}/player/bbr_id/{player_id}")
                bbr_id = bbr_id.json()['bbr_id']
                advanced_stats = advanced_stats_table(bbr_id)
            except:
                continue
            for index, row in advanced_stats.iterrows():
                if row['Season'] == 'Career':
                    break
                season = row['Season']
                season = int(str(season).split('-')[0])
                data = json.dumps({
                    'TS_pctg': row['TS%'],
                    'TPAr': row['3PAr'],
                    'FTr': row['FTr'],
                    'ORB_pctg': row['ORB%'],
                    'DRB_pctg': row['DRB%'],
                    'TRB_pctg': row['TRB%'],
                    'AST_pctg': row['AST%'],
                    'STL_pctg': row['STL%'],
                    'BLK_pctg': row['BLK%'],
                    'TOV_pctg': row['TOV%'],
                    'USG_pctg': row['USG%'],
                    'OWS': row['OWS'],
                    'DWS': row['DWS'],
                    'WS': row['WS'],
                    'WS_48': row['WS/48'],
                    'OBPM': row['OBPM'],
                    'DBPM': row['DBPM'],
                    'BPM': row['BPM'],
                    'VORP': row['VORP'],
                })
                response = requests.request(
                    'DELETE', f"{BASE}/player/advanced_stats/{player_id}/{season}")
                headers = {'Content-Type': 'application/json'}
                response = requests.request(
                    'POST', f"{BASE}/player/advanced_stats/{player_id}/{season}", data=data, headers=headers)
                print(response.text)


if __name__ == "__main__":
    main()
