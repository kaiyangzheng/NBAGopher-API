"""
puts data in dpoy database
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


def main():
    classifier = pickle.load(open('./models/DPOY_classifier.pkl', 'rb'))
    predicted_dpoys = []
    for player in player_data:
        if player['isActive']:
            player_id = player['personId']
            print(
                f"https://nbagopher-api.herokuapp.com/player/compiled/{player_id}")
            player_stats = requests.get(
                f"https://nbagopher-api.herokuapp.com/player/compiled/{player_id}")
            player_stats = player_stats.json()
            try:
                player_basic_latest = player_stats['player_basic_latest']
                player_advanced_latest = player_stats['player_advanced_latest']
                classifier_stats = [float(player_basic_latest['rpg']), float(
                    player_basic_latest['spg']), float(player_basic_latest['bpg']), float(player_advanced_latest['TRB_pctg']), float(player_advanced_latest['STL_pctg']), float(player_advanced_latest['BLK_pctg']), float(player_advanced_latest['DBPM'])]
            except:
                classifier_stats = [0, 0, 0, 0, 0, 0, 0]

            classifier_prediction = classifier.predict([classifier_stats])
            print(classifier_prediction)
            predict_proba = classifier.predict_proba([classifier_stats])
            print(predict_proba)
            if classifier_prediction[0] == 1:
                predicted_dpoys.append(
                    {'player': player_id, 'predict_proba': predict_proba[0][1]})

    sorted_dpoy = sorted(
        predicted_dpoys, key=lambda k: k['predict_proba'], reverse=True)
    predicted_dpoy = json.dumps(sorted_dpoy[0])
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        BASE + "player/predicted_dpoy", data=predicted_dpoy, headers=headers)
    print(response.text)


if __name__ == "__main__":
    main()
