"""
puts data in mvp candidate database
"""
import requests
import pickle
import json
from sklearn.linear_model import LogisticRegression
import numpy as np

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
BBREF_SEASON = SEASON+1
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']


def get_team_win_perc(team_id):
    STANDINGS_API = 'https://data.nba.net/data/10s/prod/v1/current/standings_all.json'
    standings_data = requests.get(STANDINGS_API)
    standings_data = standings_data.json()['league']['standard']['teams']
    for team in standings_data:
        if team['teamId'] == team_id:
            return float(team['winPct'])


def main():
    classifier = pickle.load(open('./ML/classifiers/mvp_model.pkl', 'rb'))
    for player in player_data:
        if player['isActive']:
            player_id = player['personId']
            PLAYER_STATS_API = f"https://data.nba.net/data/10s/prod/v1/{SEASON}/players/{player_id}_profile.json"
            player_info = requests.get(PLAYER_STATS_API)
            team_id = player_info.json()['league']['standard']['teamId']
            player_stats = requests.get(
                f"https://nbagopher-api.herokuapp.com/player/compiled/{player_id}")
            print(
                f"https://nbagopher-api.herokuapp.com/player/compiled/{player_id}")
            player_stats = player_stats.json()
            try:
                player_advanced_latest = player_stats['player_advanced_latest']
                player_basic_latest = player_stats['player_basic_latest']
                if (team_id == ''):
                    team_win_perc = 0
                else:
                    team_win_perc = get_team_win_perc(team_id)

                classifier_stats = [float(player_basic_latest['mpg']), float(player_basic_latest['ppg']), float(player_basic_latest['rpg']), float(player_basic_latest['apg']), float(player_basic_latest['spg']), float(player_basic_latest['bpg']), float(
                    player_basic_latest['fgp'])/100, float(player_basic_latest['tpp'])/100, float(player_basic_latest['ftp'])/100, float(player_advanced_latest['WS']), float(player_advanced_latest['WS_48']), team_win_perc]
            except:
                classifier_stats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            prediction = np.uint32(
                (classifier.predict([classifier_stats])[0])).item()
            response = requests.request(
                'DELETE', BASE_TEST + f'mvp_candidate/{player_id}')
            headers = {'Content-Type': 'application/json'}
            response = requests.request('POST', BASE_TEST +
                                        f'/mvp_candidate/{player_id}', data=json.dumps({'id': player_id, 'is_mvp_cand': prediction}), headers=headers)
            print(response.text)


if __name__ == "__main__":
    main()
