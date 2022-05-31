"""
posts data in FuturePerformance db
"""

import requests
import pickle
import json
import numpy as np

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
BBREF_SEASON = SEASON+1
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']


def main_2():
    regression = pickle.load(open("./models/future_perf_2.pickle", "rb"))
    for player in player_data:
        player_id = player['personId']
        PLAYER_STATS_API = f"{BASE}player/compiled/{player_id}"
        player_stats = requests.get(PLAYER_STATS_API)
        player_stats = player_stats.json()
        try:
            player_basic_latest = player_stats['player_basic_latest']
            player_advanced_latest = player_stats['player_advanced_latest']
            player_info = player_stats['player_info']
            regression_data = [int(player_info['years_pro']), float(player_basic_latest['mpg']), float(player_advanced_latest['TS_pctg']), float(player_advanced_latest['TRB_pctg']), float(player_advanced_latest['AST_pctg']), float(player_advanced_latest['STL_pctg']), float(player_advanced_latest['BLK_pctg']), float(
                player_advanced_latest['TOV_pctg']), float(player_advanced_latest['USG_pctg']), float(player_advanced_latest['BPM']), float(player_basic_latest['rpg']), float(player_basic_latest['apg']), float(player_basic_latest['spg']), float(player_basic_latest['bpg']), float(player_basic_latest['topg']), float(player_basic_latest['ppg'])]
        except:
            print('oops')
            regression_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        prediction = regression.predict([regression_data])[0]
        data = json.dumps({
            'TS_pctg': str(round(prediction[0], 3)),
            'mpg': str(round(prediction[1], 1)),
            'ppg': str(round(prediction[2], 1)),
            'apg': str(round(prediction[3], 1)),
            'rpg': str(round(prediction[4], 1)),
            'bpg': str(round(prediction[5], 1)),
            'spg': str(round(prediction[6], 1)),
            'BPM': str(round(prediction[7], 1)),
        })
        response = requests.request(
            'DELETE', f"{BASE}player/future_performance/{player_id}")
        headers = {'Content-Type': 'application/json'}
        response = requests.request(
            'POST', f"{BASE}player/future_performance/{player_id}", data=data, headers=headers)
        print(response.text)


def main():
    regression = pickle.load(open('./models/future_perf.pickle', 'rb'))
    for player in player_data:
        player_id = player['personId']
        PLAYER_STATS_API = f"{BASE}player/compiled/{player_id}"
        player_stats = requests.get(PLAYER_STATS_API)
        player_stats = player_stats.json()
        try:
            player_basic_latest = player_stats['player_basic_latest']
            player_advanced_latest = player_stats['player_advanced_latest']
            player_info = player_stats['player_info']
            regression_data = [int(player_info['years_pro']), float(player_info['height_meters']), float(player_basic_latest['mpg']), float(player_basic_latest['ppg']), float(
                player_basic_latest['apg']), float(player_basic_latest['rpg']), float(player_advanced_latest['TS_pctg']), float(player_advanced_latest['BPM'])]
        except:
            regression_data = [0, 0, 0, 0, 0, 0, 0, 0]
        prediction = regression.predict([regression_data])[0]
        data = json.dumps({
            'mpg': str(round(prediction[0], 1)),
            'ppg': str(round(prediction[1], 1)),
            'apg': str(round(prediction[2], 1)),
            'rpg': str(round(prediction[3], 1)),
            'TS_pctg': str(round(prediction[4], 3)),
            'BPM': str(round(prediction[5], 1)),
        })
        response = requests.request(
            'DELETE', f"{BASE}player/future_performance/{player_id}")
        headers = {'Content-Type': 'application/json'}
        response = requests.request(
            'POST', f"{BASE}player/future_performance/{player_id}", data=data, headers=headers)
        print(response.text)


if __name__ == "__main__":
    main()
