"""
puts data into 6moy database
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
    classifier = pickle.load(
        open('./ML/classifiers/6MOY_classifier.pkl', 'rb'))
    predicted_6moy_cands = []
    for player in player_data:
        if player['isActive']:
            player_id = player['personId']
            print(
                f"https://nbagopher-api.herokuapp.com/player/compiled/{player_id}")
            player_stats = requests.get(
                f"https://nbagopher-api.herokuapp.com/player/compiled/{player_id}")
            player_stats = player_stats.json()
            try:
                player_advanced_latest = player_stats['player_advanced_latest']
                player_basic_latest = player_stats['player_basic_latest']
                if (int(player_basic_latest['games_started']) > 41):
                    continue
                if (int(player_basic_latest['games_played']) < 57):
                    continue
                classifier_stats = [player_basic_latest['ppg'], player_basic_latest['apg'],
                                    player_basic_latest['rpg'], player_advanced_latest['TS_pctg'], player_advanced_latest['BPM']]
                classifier_stats = np.array(classifier_stats).astype(float)
            except:
                print('!')
                classifier_stats = [0, 0, 0, 0, 0]
            print(classifier_stats)
            classifier_prediction = classifier.predict([classifier_stats])
            predict_proba = classifier.predict_proba([classifier_stats])
            print(predict_proba[0][1])
            if classifier_prediction == 1:
                print(classifier_stats)
                predicted_6moy_cands.append(
                    {'player': player_id, 'predict_proba': predict_proba[0][1]})
    sorted_6moy = sorted(predicted_6moy_cands,
                         key=lambda k: k['predict_proba'], reverse=True)
    print(sorted_6moy)
    predicted_6moy = json.dumps(sorted_6moy[0])
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        BASE + 'player/predicted_6moy', data=predicted_6moy, headers=headers)
    print(response.text)


if __name__ == "__main__":
    main()
