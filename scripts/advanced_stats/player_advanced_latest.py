"""
Puts and updates data into the player advanced latest stats database
"""
import pandas as pd
import requests
from urllib.request import urlopen
import unidecode
from bs4 import BeautifulSoup
import json

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
BBREF_SEASON = SEASON+1
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']

# filters dictionary


def filterTheDict(dictObj, callback):
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict


def advanced_stats():
    html_text = urlopen(
        f'https://www.basketball-reference.com/leagues/NBA_{BBREF_SEASON}_advanced.html')
    soup = BeautifulSoup(html_text.read(), 'lxml')
    table = soup.find('table', {'id': 'advanced_stats'})
    advanced_stats_table = pd.read_html(str(table))[0]

    # formatting table

    players = advanced_stats_table['Player'].tolist()
    i = 0
    while i < len(players):
        players[i] = unidecode.unidecode(players[i])
        players[i] = players[i].replace('*', '')
        i += 1
    advanced_stats_table['Player'] = players
    advanced_stats_table = advanced_stats_table[advanced_stats_table.Rk != 'Rk']
    advanced_stats_table = advanced_stats_table.fillna(0)
    advanced_stats_table = advanced_stats_table.drop(
        columns=["Unnamed: 19", "Unnamed: 24", 'Pos', 'Age', 'Tm', 'G', 'MP'])

    # combine partial rows

    dup_players = []
    dup_indexes = []
    player_list = []
    players = advanced_stats_table['Player'].tolist()
    i = 0
    for player in players:
        if player not in player_list:
            player_list.append(player)
        else:
            if player not in dup_players:
                dup_players.append(player)
                dup_indexes.append(i)
        i += 1
    for player in dup_players:
        player_series = advanced_stats_table[advanced_stats_table['Player'] == player]
        series_length = len(player_series)
        new_series = [0 for i in range(22)]
        for i in range(series_length):
            part_player_series = player_series.iloc[i].tolist()
            new_series[0] = part_player_series[0]
            new_series[1] = part_player_series[1]
            j = 2
            while j < 22:
                new_series[j] += float(part_player_series[j])
                j += 1
        i = 2
        while i < 22:
            if i >= 3 and i <= 5 or i == 17:
                new_series[i] = round(new_series[i]/series_length, 3)
            else:
                new_series[i] = round(new_series[i]/series_length, 1)
            i += 1
        advanced_stats_table[advanced_stats_table['Player']
                             == player] = new_series
    advanced_stats_table = advanced_stats_table.drop_duplicates()
    advanced_stats_table = advanced_stats_table.reset_index(drop=True)
    return advanced_stats_table


def main():
    for player in player_data:
        if (player['isActive']):
            player_id = player['personId']
            player_name = player['firstName'] + ' ' + player['lastName']
            if player_name == 'Robert Williams III':
                player_name = 'Robert Williams'
            player_advanced_stats = advanced_stats_table[advanced_stats_table['Player'] == player_name]
            try:
                data = json.dumps({
                    'TS_pctg': player_advanced_stats['TS%'].tolist()[0],
                    'TPAr': player_advanced_stats['3PAr'].tolist()[0],
                    'FTr': player_advanced_stats['FTr'].tolist()[0],
                    'ORB_pctg': player_advanced_stats['ORB%'].tolist()[0],
                    'DRB_pctg': player_advanced_stats['DRB%'].tolist()[0],
                    'TRB_pctg': player_advanced_stats['TRB%'].tolist()[0],
                    'AST_pctg': player_advanced_stats['AST%'].tolist()[0],
                    'STL_pctg': player_advanced_stats['STL%'].tolist()[0],
                    'BLK_pctg': player_advanced_stats['BLK%'].tolist()[0],
                    'TOV_pctg': player_advanced_stats['TOV%'].tolist()[0],
                    'USG_pctg': player_advanced_stats['USG%'].tolist()[0],
                    'OWS': player_advanced_stats['OWS'].tolist()[0],
                    'DWS': player_advanced_stats['DWS'].tolist()[0],
                    'WS': player_advanced_stats['WS'].tolist()[0],
                    'WS_48': player_advanced_stats['WS/48'].tolist()[0],
                    'OBPM': player_advanced_stats['OBPM'].tolist()[0],
                    'DBPM': player_advanced_stats['DBPM'].tolist()[0],
                    'BPM': player_advanced_stats['BPM'].tolist()[0],
                    'VORP': player_advanced_stats['VORP'].tolist()[0],
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
                'DELETE', BASE + f'player/advanced_latest/{player_id}')
            headers = {'Content-Type': 'application/json'}
            response = requests.request(
                'POST', BASE + f'player/advanced_latest/{player_id}', data=data, headers=headers)
            print(response.text)


if __name__ == "__main__":
    advanced_stats_table = advanced_stats()
    main()
