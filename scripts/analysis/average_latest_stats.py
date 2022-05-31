"""
Posts data into average advanced db
"""

import pandas as pd
import numpy as np
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


def get_top_20_ppg():
    ppg_dict = {}
    for player in player_data:
        player_id = player['personId']
        if (player['isActive']):
            try:
                player_stats = requests.get(
                    BASE+f"player/compiled/{player_id}")
                player_stats = player_stats.json()
                player_basic = player_stats['player_basic_latest']
                ppg = player_basic['ppg']
                ppg_dict[player_id] = float(ppg)
            except:
                ppg_dict[player_id] = 0
    ppg_dict = sorted(ppg_dict.items(), key=lambda x: x[1], reverse=True)
    return (ppg_dict[0:30])


def main():
    stats_total = {}
    ppg_dict = get_top_20_ppg()
    for (playerId, ppg) in ppg_dict:
        player_stats = requests.get(BASE+f"player/compiled/{playerId}")
        player_stats = player_stats.json()
        player_basic = player_stats['player_basic_latest']
        player_advanced = player_stats['player_advanced_latest']
        for key in player_basic:
            if key not in stats_total:
                stats_total[key] = 0
            stats_total[key] += float(player_basic[key])
        for key in player_advanced:
            if key not in stats_total:
                stats_total[key] = 0
            stats_total[key] += float(player_advanced[key])
    for key in stats_total:
        if (key == 'TS_pctg' or key == 'TPAr' or key == 'FTr' or key == 'WS_48'):
            stats_total[key] = round(stats_total[key]/30, 4)
        else:
            stats_total[key] = round(stats_total[key]/30, 1)
    stats_total = json.dumps(stats_total)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        BASE+f"player/average_basic_stats_top_30_ppg", data=stats_total, headers=headers)
    print(response.text)
    response = requests.post(
        BASE + f"player/average_advanced_stats_top_30_ppg", data=stats_total, headers=headers)
    print(response.text)


def gen_stats_df():
    player_stats = requests.get(BASE+f"player/compiled/201939")
    player_stats = player_stats.json()
    player_basic = player_stats['player_basic_latest']
    player_advanced = player_stats['player_advanced_latest']
    columns = []
    for key in player_basic:
        columns.append(key)
    for key in player_advanced:
        columns.append(key)
    print(columns)
    df = pd.DataFrame(columns=columns)
    for player in player_data:
        player_id = player['personId']
        if (player['isActive']):
            try:
                player_stats = requests.get(
                    BASE+f"player/compiled/{player_id}")
                player_stats = player_stats.json()
                player_basic = player_stats['player_basic_latest']
                player_advanced = player_stats['player_advanced_latest']
                player_basic_list = {}
                player_advanced_list = {}
                for key in player_basic:
                    player_basic_list[key] = (player_basic[key])
                for key in player_advanced:
                    player_advanced_list[key] = (player_advanced[key])
                data = {**player_basic_list, **player_advanced_list}
                print(data)
                df = df.append(data, ignore_index=True)
                print(df)
                print(BASE+f"player/compiled/{player_id}")
            except:
                continue
    df.to_csv(f"player_stats.csv")


def main_2():
    stats_total = {}
    #df = pd.read_csv("player_stats.csv")
    df = gen_stats_df()
    df = df.fillna(0)
    df = df.drop(['Unnamed: 0'], axis=1)
    for col in df.columns:
        stat_list = np.array(df[col].tolist()).astype(float)
        stats_total[col] = np.percentile(stat_list, 75)
    stats_total = json.dumps(stats_total)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        BASE+f"player/average_basic_stats_top_30_ppg", data=stats_total, headers=headers)
    print(response.text)
    response = requests.post(
        BASE + f"player/average_advanced_stats_top_30_ppg", data=stats_total, headers=headers)
    print(response.text)


if __name__ == "__main__":
    main_2()
