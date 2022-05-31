"""
puts data into mip database
"""

import requests
import pickle
import numpy as np
import json

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
BBREF_SEASON = SEASON+1
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']


def main():
    classifier = pickle.load(open('./models/MIP_classifier.pkl', 'rb'))
    predicted_mip_cands = []
    for player in player_data:
        if player['isActive']:
            player_id = player['personId']
            print(
                f"https://nbagopher-api.herokuapp.com/player/compiled/{player_id}")
            player_stats = requests.get(
                f"https://nbagopher-api.herokuapp.com/player/compiled/{player_id}")
            player_stats = player_stats.json()
            current_stats = []
            prev_stats = []
            try:
                player_basic_latest = player_stats['player_basic_latest']
                player_advanced_latest = player_stats['player_advanced_latest']
                current_stats = [float(player_basic_latest['ppg']), float(player_basic_latest['apg']), float(player_basic_latest['rpg']), float(player_basic_latest['spg']), float(
                    player_basic_latest['bpg']), float(player_basic_latest['fgp']), float(player_basic_latest['tpp']), float(player_basic_latest['ftp']), float(player_advanced_latest['BPM'])]
                player_basic_prev = player_stats['player_basic_prev']
                player_advanced_prev = player_stats['player_advanced_prev']
                prev_stats = [float(player_basic_prev['ppg']), float(player_basic_prev['apg']), float(player_basic_prev['rpg']), float(player_basic_prev['spg']), float(
                    player_basic_prev['bpg']), float(player_basic_prev['fgp']), float(player_basic_prev['tpp']), float(player_basic_prev['ftp']), float(player_advanced_prev['BPM'])]
            except:
                print('!')
                current_stats = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                prev_stats = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            current_stats = np.array(current_stats)
            prev_stats = np.array(prev_stats)
            prediction_stats = np.subtract(current_stats, prev_stats)
            try:
                prediction_stats = prediction_stats.tolist() + [float(player_basic_latest['ppg']), float(
                    player_basic_latest['apg']), float(player_basic_latest['rpg'])]
            except:
                prediction_stats = prediction_stats.tolist() + [0, 0, 0]
            classifier_prediction = classifier.predict([prediction_stats])
            predict_proba = classifier.predict_proba([prediction_stats])
            if classifier_prediction == 1:
                print(prediction_stats)
                predicted_mip_cands.append(
                    {'player': player_id, 'predict_proba': predict_proba[0][1]})

    sorted_mip = sorted(predicted_mip_cands,
                        key=lambda k: k['predict_proba'], reverse=True)
    print(sorted_mip)

    predicted_mip = json.dumps(sorted_mip[0])
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        BASE + "player/predicted_mip", data=predicted_mip, headers=headers)
    print(response.text)


if __name__ == "__main__":
    main()
