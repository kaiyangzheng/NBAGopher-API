"""
get improving and declining players
"""

import requests
import json
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
BBREF_SEASON = SEASON+1
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']


def get_team_gp(team_id):
    team_api = f"https://data.nba.net/data/10s/prod/v1/{SEASON}/teams.json"
    team_data = requests.get(team_api)
    team_data = team_data.json()['league']['standard']
    team_full_name = ""
    for team in team_data:
        if team['teamId'] == team_id:
            team_full_name = team['fullName']
    if team_full_name == 'LA Clippers':
        team_full_name = 'Los Angeles Clippers'
    print(team_full_name)
    html_text = urlopen(
        f"https://www.basketball-reference.com/leagues/NBA_{BBREF_SEASON}.html")
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find('table', {'id': 'per_game-team'})
    df = pd.read_html(str(table))[0]
    return df[df['Team'] == team_full_name]['G'].values[0]


def gen_value_list():
    player_id_list = []
    value_list = []
    for player in player_data:
        if player['isActive']:
            player_id = player['personId']
            try:
                player_pctls = requests.get(
                    f"{BASE}player/compiled/pctls/{player_id}")
                player_pctls = player_pctls.json()
                player_stats = requests.get(
                    f"{BASE}player/compiled/{player_id}")
                player_stats = player_stats.json()
                player_info = player_stats['player_info']
                player_basic_stats_latest = player_stats['player_basic_latest']
                player_basic_stats_prev = player_stats['player_basic_prev']
            except:
                continue
            print(f"{BASE}player/compiled/{player_id}")
            gp = get_team_gp(player_info['team_id'])
            if 'player_basic_prev_pctls' in player_pctls and 'player_advanced_prev_pctls' in player_pctls and len(player_pctls['player_basic_prev_pctls']) > 0 and len(player_pctls['player_advanced_prev_pctls']) > 0:
                try:
                    if (float(player_basic_stats_latest['games_played'])/float(gp) <= 0.7):
                        continue
                except:
                    continue
                player_basic_prev_pctls = player_pctls['player_basic_prev_pctls']
                player_advanced_prev_pctls = player_pctls['player_advanced_prev_pctls']
                player_basic_latest_pctls = player_pctls['player_basic_latest_pctls']
                player_advanced_latest_pctls = player_pctls['player_advanced_latest_pctls']
                player_basic_prev_pctls_list = []
                for key in player_basic_prev_pctls:
                    if player_basic_prev_pctls[key] == 'NQ':
                        player_basic_prev_pctls_list.append(0)
                    else:
                        player_basic_prev_pctls_list.append(
                            player_basic_prev_pctls[key])

                player_advanced_prev_pctls_list = []
                for key in player_advanced_prev_pctls:
                    if player_advanced_prev_pctls[key] == 'NQ':
                        player_advanced_prev_pctls_list.append(0)
                    else:
                        player_advanced_prev_pctls_list.append(
                            player_advanced_prev_pctls[key])

                player_basic_latest_pctls_list = []
                for key in player_basic_latest_pctls:
                    if player_basic_latest_pctls[key] == 'NQ':
                        player_basic_latest_pctls_list.append(0)
                    else:
                        player_basic_latest_pctls_list.append(
                            player_basic_latest_pctls[key])

                player_advanced_latest_pctls_list = []
                for key in player_advanced_latest_pctls:
                    if player_advanced_latest_pctls[key] == 'NQ':
                        player_advanced_latest_pctls_list.append(0)
                    else:
                        player_advanced_latest_pctls_list.append(
                            player_advanced_latest_pctls[key])

                player_basic_prev_pctls_list = np.array(
                    player_basic_prev_pctls_list).astype(np.float)
                player_advanced_prev_pctls_list = np.array(
                    player_advanced_prev_pctls_list).astype(np.float)
                player_basic_latest_pctls_list = np.array(
                    player_basic_latest_pctls_list).astype(np.float)
                player_advanced_latest_pctls_list = np.array(
                    player_advanced_latest_pctls_list).astype(np.float)

                print(player_basic_prev_pctls_list)
                print(player_basic_latest_pctls_list)

                player_basic_diff = np.subtract(
                    player_basic_latest_pctls_list, player_basic_prev_pctls_list)
                player_advanced_diff = np.subtract(
                    player_advanced_latest_pctls_list, player_advanced_prev_pctls_list)

                # add ALL and weight

                value = np.mean(player_basic_diff) + \
                    np.mean(player_advanced_diff)

                player_id_list.append(player_id)
                value_list.append(value)
    return player_id_list, value_list


def get_improving(player_id_list, value_list):
    improving_player_id_list = []
    for i in range(10):
        max_value = max(value_list)
        max_index = value_list.index(max_value)
        max_player_id = player_id_list[max_index]
        improving_player_id_list.append(max_player_id)
        value_list.pop(max_index)
        player_id_list.pop(max_index)
    return improving_player_id_list


def get_declining(player_id_list, value_list):
    declining_player_id_list = []
    for i in range(10):
        min_value = min(value_list)
        min_index = value_list.index(min_value)
        min_player_id = player_id_list[min_index]
        declining_player_id_list.append(min_player_id)
        value_list.pop(min_index)
        player_id_list.pop(min_index)
    return declining_player_id_list


def main():
    player_id_list, value_list = gen_value_list()
    improving_player_id_list = get_improving(player_id_list, value_list)
    declining_player_id_list = get_declining(player_id_list, value_list)

    print(improving_player_id_list)
    print(declining_player_id_list)

    response = requests.delete(f"{BASE}player/trending_players")
    print(response.text)

    for player in improving_player_id_list:
        data = json.dumps({'is_improving': True})
        headers = {'Content-Type': 'application/json'}
        response = requests.request(
            "POST", f"{BASE}player/trending_player/{player}", data=data, headers=headers)
        print(response.text)

    for player in declining_player_id_list:
        data = json.dumps({'is_improving': False})
        headers = {'Content-Type': 'application/json'}
        response = requests.request(
            "POST", f"{BASE}player/trending_player/{player}", data=data, headers=headers)
        print(response.text)


if __name__ == "__main__":
    main()
