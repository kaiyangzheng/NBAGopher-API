"""
Puts and updates data into the player advanced career database
"""
import pandas as pd
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
BBR_BASE = "https://basketball-reference.com"
SEASON = 2021
BBREF_SEASON = SEASON+1
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']


def career_advanced_stats(player_id):
    response = requests.get(BASE + f"player/bbr_id/{player_id}")
    print(BASE + f"player/bbr_id/{player_id}")
    try:
        bbr_id = response.json()['bbr_id']
    except:
        return ''
    print(BBR_BASE + bbr_id)
    html_text = urlopen(BBR_BASE + bbr_id)
    soup = BeautifulSoup(html_text.read(), 'lxml')
    try:
        table = soup.find('table', {'id': 'advanced'})
        career_advanced_stats_table = pd.read_html(str(table))[0]
        career_advanced_stats_series = career_advanced_stats_table[
            career_advanced_stats_table['Season'] == 'Career']
        career_advanced_stats_series = career_advanced_stats_series.astype(str)
        return career_advanced_stats_series
    except:
        return ''


def raptor_career_stats(player_id):
    response = requests.get(BASE + f"player/bbr_id/{player_id}")
    bbr_id = response.json()['bbr_id']
    bbr_id_stripped = bbr_id.split('/')[3].split('.')[0]
    raptor_stats_table = pd.read_csv(
        'https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-raptor/modern_RAPTOR_by_player.csv')
    player_raptor_stats = raptor_stats_table[raptor_stats_table['player_id']
                                             == bbr_id_stripped]
    player_raptor_stats_length = len(player_raptor_stats)
    raptor_data = {
        'raptor_offense': 0,
        'raptor_defense': 0,
        'raptor_total': 0
    }
    for i in range(player_raptor_stats_length):
        player_raptor_stats_series = player_raptor_stats.iloc[i]
        for stat in raptor_data:
            raptor_data[stat] += float(player_raptor_stats_series[stat])
    for stat in raptor_data:
        try:
            raptor_data[stat] = str(
                round(raptor_data[stat]/player_raptor_stats_length, 6))
        except:
            raptor_data[stat] = '0'
    return raptor_data


def main():
    for player in player_data:
        if (player['isActive']):
            player_id = player['personId']
            print(player_id)
            player_career_advanced_stats = career_advanced_stats(player_id)
            print(player_career_advanced_stats)
            try:
                data = json.dumps({
                    'TS_pctg': (player_career_advanced_stats['TS%']).to_list()[0],
                    'TPAr': player_career_advanced_stats['3PAr'].to_list()[0],
                    'FTr': player_career_advanced_stats['FTr'].to_list()[0],
                    'ORB_pctg': player_career_advanced_stats['ORB%'].to_list()[0],
                    'DRB_pctg': player_career_advanced_stats['DRB%'].to_list()[0],
                    'TRB_pctg': player_career_advanced_stats['TRB%'].to_list()[0],
                    'AST_pctg': player_career_advanced_stats['AST%'].to_list()[0],
                    'STL_pctg': player_career_advanced_stats['STL%'].to_list()[0],
                    'BLK_pctg': player_career_advanced_stats['BLK%'].to_list()[0],
                    'TOV_pctg': player_career_advanced_stats['TOV%'].to_list()[0],
                    'USG_pctg': player_career_advanced_stats['USG%'].to_list()[0],
                    'OWS': player_career_advanced_stats['OWS'].to_list()[0],
                    'DWS': player_career_advanced_stats['DWS'].to_list()[0],
                    'WS': player_career_advanced_stats['WS'].to_list()[0],
                    'WS_48': player_career_advanced_stats['WS/48'].to_list()[0],
                    'OBPM': player_career_advanced_stats['OBPM'].to_list()[0],
                    'DBPM': player_career_advanced_stats['DBPM'].to_list()[0],
                    'BPM': player_career_advanced_stats['BPM'].to_list()[0],
                    'VORP': player_career_advanced_stats['VORP'].to_list()[0],
                })
            except:
                data = json.dumps({
                    'TS_pctg': '0',
                    'TPAr': '0',
                    'FTr': '0',
                    'ORB_pctg': '0',
                    'DRB_pctg': '0',
                    'TRB_pctg': '0',
                    'AST_pctg': '0',
                    'STL_pctg': '0',
                    'BLK_pctg': '0',
                    'TOV_pctg': '0',
                    'USG_pctg': '0',
                    'OWS': '0',
                    'DWS': '0',
                    'WS': '0',
                    'WS_48': '0',
                    'OBPM': '0',
                    'DBPM': '0',
                    'BPM': '0',
                    'VORP': '0',
                })
        response = requests.request(
            'DELETE', BASE + f"player/advanced_career/{player_id}")
        headers = {'Content-Type': 'application/json'}
        response = requests.request('POST', BASE + f"player/advanced_career/{player_id}",
                                    data=data, headers=headers)
        print(response.text)


if __name__ == "__main__":
    main()
