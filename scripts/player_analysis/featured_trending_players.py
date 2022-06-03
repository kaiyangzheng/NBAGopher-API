"""
Posts and updates featured trending players (improve offense, defense), (decline offense, defense)
"""
import requests
import json
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


BASE = "https://nbagopher-api.herokuapp.com/"
BBR_BASE = "https://basketball-reference.com"
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
    html_text = urlopen(
        f"https://www.basketball-reference.com/leagues/NBA_{BBREF_SEASON}.html")
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find('table', {'id': 'per_game-team'})
    df = pd.read_html(str(table))[0]
    return df[df['Team'] == team_full_name]['G'].values[0]


def offense_value(player_basic_by_season, player_advanced_by_season):
    basic_latest_year = player_basic_by_season[0]
    basic_prev_year = player_basic_by_season[1]
    advanced_latest_year = player_advanced_by_season[0]
    advanced_prev_year = player_advanced_by_season[1]

    offense_basic_stats = ['ppg', 'apg', 'fgp', 'ftp', 'tpp']
    offense_basic_weights = {'ppg': 100, 'apg': 80,
                             'fgp':  60, 'ftp':  40, 'tpp':  50}
    offense_advanced_stats = ['TS_pctg', 'AST_pctg', 'ORB_pctg', 'OBPM']
    offense_advanced_weights = {'TS_pctg': 90,
                                'AST_pctg': 70,  'ORB_pctg': 70,  'OBPM': 100}

    basic_latest_list = []
    for stat in offense_basic_stats:
        basic_latest_list.append(float(
            basic_latest_year[stat]) * offense_basic_weights[stat])

    basic_latest_list = np.array(basic_latest_list).astype(float)

    basic_prev_list = []
    for stat in offense_basic_stats:
        basic_prev_list.append(
            float(basic_prev_year[stat]) * offense_basic_weights[stat])

    basic_prev_list = np.array(basic_prev_list).astype(float)

    basic_diff1 = np.mean(np.array(basic_latest_list) -
                          np.array(basic_prev_list))

    advanced_latest_list = []
    for stat in offense_advanced_stats:
        advanced_latest_list.append(
            float(advanced_latest_year[stat]) * offense_advanced_weights[stat])

    advanced_latest_list = np.array(advanced_latest_list).astype(float)

    advanced_prev_list = []
    for stat in offense_advanced_stats:
        advanced_prev_list.append(
            float(advanced_prev_year[stat]) * offense_advanced_weights[stat])

    advanced_prev_list = np.array(advanced_prev_list).astype(float)

    advanced_diff1 = np.mean(np.array(advanced_latest_list) -
                             np.array(advanced_prev_list))

    value = basic_diff1 + advanced_diff1
    return value


def defense_value(player_basic_by_season, player_advanced_by_season):
    basic_latest_year = player_basic_by_season[0]
    basic_prev_year = player_basic_by_season[1]
    basic_prev_2_year = player_basic_by_season[2]
    advanced_latest_year = player_advanced_by_season[0]
    advanced_prev_year = player_advanced_by_season[1]
    advanced_prev_2_year = player_advanced_by_season[2]

    defense_basic_stats = ['rpg', 'bpg', 'spg']
    defense_basic_weights = {'rpg': 90, 'bpg': 80, 'spg': 80}
    defense_advanced_stats = ['DRB_pctg', 'STL_pctg', 'BLK_pctg', 'DBPM']
    defense_advanced_weights = {'DRB_pctg': 90,
                                'STL_pctg': 80, 'BLK_pctg': 80, 'DBPM': 100}

    basic_latest_list = []
    for stat in defense_basic_stats:
        basic_latest_list.append(
            float(basic_latest_year[stat]) * defense_basic_weights[stat])

    basic_latest_list = np.array(basic_latest_list).astype(float)

    basic_prev_list = []
    for stat in defense_basic_stats:
        basic_prev_list.append(
            float(basic_prev_year[stat]) * defense_basic_weights[stat])

    basic_prev_list = np.array(basic_prev_list).astype(float)

    basic_diff1 = np.mean(np.array(basic_latest_list) -
                          np.array(basic_prev_list))

    advanced_latest_list = []
    for stat in defense_advanced_stats:
        advanced_latest_list.append(
            float(advanced_latest_year[stat]) * defense_advanced_weights[stat])

    advanced_latest_list = np.array(advanced_latest_list).astype(float)

    advanced_prev_list = []
    for stat in defense_advanced_stats:
        advanced_prev_list.append(
            float(advanced_prev_year[stat]) * defense_advanced_weights[stat])

    advanced_prev_list = np.array(advanced_prev_list).astype(float)

    advanced_prev_2_list = np.array(advanced_prev_2_list).astype(float)

    advanced_diff1 = np.mean(np.array(advanced_latest_list) -
                             np.array(advanced_prev_list))

    value = basic_diff1 + advanced_diff1
    return value


def main():
    offense_val_list = []
    offense_player_id_list = []
    defense_val_list = []
    defense_player_id_list = []
    for player in player_data:
        if player['isActive']:
            player_id = player['personId']
            team_id = player['teamId']
            try:
                player_stats_by_season = requests.request(
                    'GET', f"{BASE}player/compiled/by_season/{player_id}")
                player_stats_by_season = player_stats_by_season.json()
                player_basic_by_season = player_stats_by_season['player_basic_stats']
            except:
                continue
            try:
                if (float(player_basic_by_season[0]['games_played'])/get_team_gp(team_id) < 0.7 or len(player_basic_by_season) < 3):
                    continue
            except:
                continue
            player_advanced_by_season = player_stats_by_season['player_advanced_stats']
            offense_val = offense_value(
                player_basic_by_season, player_advanced_by_season)
            print(offense_val)
            offense_val_list.append(offense_val)
            offense_player_id_list.append(player_id)
            defense_val = defense_value(
                player_basic_by_season, player_advanced_by_season)
            print(defense_val)
            defense_val_list.append(defense_val)
            defense_player_id_list.append(player_id)

    print(offense_player_id_list)
    print(defense_player_id_list)

    improving_off_list = []
    for i in range(5):
        max_value = max(offense_val_list)
        max_index = offense_val_list.index(max_value)
        improving_off_list.append(offense_player_id_list[max_index])
        offense_val_list.pop(max_index)
        offense_player_id_list.pop(max_index)

    improving_def_list = []
    for i in range(5):
        max_value = max(defense_val_list)
        max_index = defense_val_list.index(max_value)
        improving_def_list.append(defense_player_id_list[max_index])
        defense_val_list.pop(max_index)
        defense_player_id_list.pop(max_index)

    declining_off_list = []
    for i in range(5):
        min_value = min(offense_val_list)
        min_index = offense_val_list.index(min_value)
        declining_off_list.append(offense_player_id_list[min_index])
        offense_val_list.pop(min_index)
        offense_player_id_list.pop(min_index)

    declining_def_list = []
    for i in range(5):
        min_value = min(defense_val_list)
        min_index = defense_val_list.index(min_value)
        declining_def_list.append(defense_player_id_list[min_index])
        defense_val_list.pop(min_index)
        defense_player_id_list.pop(min_index)

    print(improving_off_list)
    print(improving_def_list)
    print(declining_off_list)
    print(declining_def_list)

    headers = {'Content-Type': 'application/json'}
    data = json.dumps({
        'featured_offense_improve_id': improving_off_list[0],
        'featured_defense_improve_id': improving_def_list[0],
        'featured_offense_decline_id': declining_off_list[0],
        'featured_defense_decline_id': declining_def_list[0]
    })
    response = requests.request(
        'POST', f"{BASE}player/featured_trending_players", data=data, headers=headers)
    print(response.text)


if __name__ == "__main__":
    main()
