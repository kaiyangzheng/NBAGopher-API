"""
Gets 3 featured players to display on the front page
"""
import requests
import json
import numpy

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
BBREF_SEASON = SEASON+1
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']


def featured_scorer():
    featured_scorer_value = 0
    featured_scorer_id = ''
    for player in player_data:
        if (player['isActive']):
            player_id = player['personId']
            print(BASE + f"player/compiled/pctls/{player_id}")
            try:
                player_stats_pctls = requests.request(
                    'GET', BASE + f"player/compiled/pctls/{player_id}")
                player_stats_pctls = player_stats_pctls.json()
                player_basic_pctls = player_stats_pctls['player_basic_latest_pctls']
                player_advanced_pctls = player_stats_pctls['player_advanced_latest_pctls']
                value = (100 * float(player_basic_pctls['ppg'])) + (70 * float(player_basic_pctls['fgp'])) + (60 * float(player_basic_pctls['ftp'])) + (
                    50 * float(player_basic_pctls['tpp'])) - (40 * float(player_basic_pctls['topg'])) + (70 * float(player_advanced_pctls['TS_pctg'])) + (80 * float(player_advanced_pctls['OBPM']))
                if value > featured_scorer_value:
                    featured_scorer_value = value
                    featured_scorer_id = player_id
            except:
                pass
    return featured_scorer_id


def featured_passer():
    featured_passer_value = 0
    featured_passer_id = ''
    for player in player_data:
        if (player['isActive']):
            player_id = player['personId']
            print(BASE + f"player/compiled/pctls/{player_id}")
            try:
                player_stats_pctls = requests.request(
                    'GET', BASE + f"player/compiled/pctls/{player_id}")
                player_stats_pctls = player_stats_pctls.json()
                player_basic_pctls = player_stats_pctls['player_basic_latest_pctls']
                player_advanced_pctls = player_stats_pctls['player_advanced_latest_pctls']
                value = (100 * float(player_advanced_pctls['AST_pctg'])) + (100 * float(player_basic_pctls['apg'])) - (
                    10 * float(player_advanced_pctls['TOV_pctg'])) - (10 * float(player_basic_pctls['topg'])) + (60 * float(player_advanced_pctls['OBPM']))
                print(value)
                if value > featured_passer_value:
                    featured_passer_value = value
                    featured_passer_id = player_id
            except:
                pass
    return featured_passer_id


def featured_defender():
    featured_defender_value = 0
    featured_defender_id = ''
    for player in player_data:
        if (player['isActive']):
            player_id = player['personId']
            print(BASE + f"player/compiled/pctls/{player_id}")
            try:
                player_stats_pctls = requests.request(
                    'GET', BASE + f"player/compiled/pctls/{player_id}")
                player_stats_pctls = player_stats_pctls.json()
                player_basic_pctls = player_stats_pctls['player_basic_latest_pctls']
                player_advanced_pctls = player_stats_pctls['player_advanced_latest_pctls']
                value = (50 * float(player_basic_pctls['rpg'])) + (60 * float(player_basic_pctls['spg'])) + (60 * float(player_basic_pctls['bpg'])) + (50 * float(player_advanced_pctls['DRB_pctg'])) + (
                    60 * float(player_advanced_pctls['BLK_pctg'])) + (60 * float(player_advanced_pctls['STL_pctg'])) + (90 * float(player_advanced_pctls['DBPM']))
                print(value)
                if value > featured_defender_value:
                    featured_defender_value = value
                    featured_defender_id = player_id
            except:
                pass
    return featured_defender_id


def featured_players():
    featured_scorer_value = 0
    featured_scorer_id = ''
    featured_passer_value = 0
    featured_passer_id = 0
    featured_defender_value = 0
    featured_defender_id = ''
    for player in player_data:
        if (player['isActive']):
            player_id = player['personId']
            print(BASE + f"player/compiled/pctls/{player_id}")
            try:
                player_stats_pctls = requests.request(
                    'GET', BASE + f"player/compiled/pctls/{player_id}")
                player_stats_pctls = player_stats_pctls.json()
                player_basic_pctls = player_stats_pctls['player_basic_latest_pctls']
                player_advanced_pctls = player_stats_pctls['player_advanced_latest_pctls']
                scorer_value = (200 * float(player_basic_pctls['ppg'])) + (50 * float(player_basic_pctls['fgp'])) + (40 * float(player_basic_pctls['ftp'])) + (
                    40 * float(player_basic_pctls['tpp'])) + (50 * float(player_advanced_pctls['TS_pctg'])) + (80 * float(player_advanced_pctls['OBPM']))
                if scorer_value > featured_scorer_value:
                    featured_scorer_value = scorer_value
                    featured_scorer_id = player_id
                passer_value = (100 * float(player_advanced_pctls['AST_pctg'])) + (100 * float(player_basic_pctls['apg'])) - (
                    10 * float(player_advanced_pctls['TOV_pctg'])) - (10 * float(player_basic_pctls['topg'])) + (60 * float(player_advanced_pctls['OBPM']))
                if passer_value > featured_passer_value:
                    featured_passer_value = passer_value
                    featured_passer_id = player_id
                defender_value = (50 * float(player_basic_pctls['rpg'])) + (60 * float(player_basic_pctls['spg'])) + (60 * float(player_basic_pctls['bpg'])) + (50 * float(player_advanced_pctls['DRB_pctg'])) + (
                    60 * float(player_advanced_pctls['BLK_pctg'])) + (60 * float(player_advanced_pctls['STL_pctg'])) + (100 * float(player_advanced_pctls['DBPM']))
                if defender_value > featured_defender_value:
                    featured_defender_value = defender_value
                    featured_defender_id = player_id
            except:
                pass
    return featured_scorer_id, featured_passer_id, featured_defender_id


def main():
    featured_scorer_id, featured_passer_id, featured_defender_id = featured_players()
    data = json.dumps({
        'featured_scorer_id': featured_scorer_id,
        'featured_passer_id': featured_passer_id,
        'featured_defender_id': featured_defender_id,
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request(
        'POST', BASE + "featured_players", data=data, headers=headers)
    print(response.text)


if __name__ == "__main__":
    main()
