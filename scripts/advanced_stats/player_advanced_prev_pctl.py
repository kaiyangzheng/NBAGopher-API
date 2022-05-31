"""
Puts and updates data into the player advanced latest pctls database
"""
import pandas as pd
import requests
from urllib.request import urlopen
import unidecode
from bs4 import BeautifulSoup
import json

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2020
BBREF_SEASON = SEASON+1
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']


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


def gen_player_pctls(player_id, df):
    output = {}
    i = 0
    for columnName, columnData in df.iteritems():
        if (i > 1):
            df[columnName] = pd.to_numeric(df[columnName], errors='coerce')
            df = df.sort_values(by=columnName, ascending=True)
            df = df.reset_index(drop=True)
            try:
                player_stats = df.loc[df['Player'] == player_id]
                percentile = str(
                    round(player_stats.index.values[0]/len(df)*100, 2))
                output[columnName] = percentile
            except:
                output[columnName] = 0
        i += 1
    return output


def main():
    df = advanced_stats()
    df = df.drop(columns=['PER'])
    df.columns = ['Rk', 'Player', 'TS_pctg', 'TPAr', 'FTr', 'ORB_pctg', 'DRB_pctg', 'TRB_pctg', 'AST_pctg',
                  'STL_pctg', 'BLK_pctg', 'TOV_pctg', 'USG_pctg', 'OWS', 'DWS', 'WS', 'WS_48', 'OBPM', 'DBPM', 'BPM', 'VORP']
    df.to_csv('test.csv')
    for player in player_data:
        if (player['isActive']):
            player_id = player['personId']
            try:
                player_advanced_latest = requests.request(
                    'GET', BASE + f"player/compiled/{player_id}")
                player_advanced_latest = player_advanced_latest.json()[
                    'player_advanced_latest']
                player_advanced_latest['Player'] = player_advanced_latest['id']
                del player_advanced_latest['id']
                df = df.append(player_advanced_latest, ignore_index=True)
                player_advanced_latest = json.dumps(
                    gen_player_pctls(player_id, df))
                print(player_id)
                print(gen_player_pctls(player_id, df))
            except:
                print(player_id)
                print(gen_player_pctls(player_id, df))
                player_advanced_latest = json.dumps(
                    gen_player_pctls(player_id, df))
            response = requests.request(
                'DELETE', BASE + f"player/advanced_prev_pctls/{player_id}")
            headers = {'Content-Type': 'application/json'}
            response = requests.request(
                'POST', BASE + f"player/advanced_prev_pctls/{player_id}", data=player_advanced_latest, headers=headers)
            print(response.text)


if __name__ == "__main__":
    main()
