"""
cPuts and updates data into player basic career pctls database
"""
from asyncore import read
import requests
import pandas as pd
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
BBREF_SEASON = 2022
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
    team_list = df['Team'].tolist()
    i = 0
    while (i < len(team_list)):
        team_list[i] = team_list[i].replace('*', '')
        i += 1
    df['Team'] = team_list
    return df[df['Team'] == team_full_name]['G'].values[0]


def create_df():
    df = pd.DataFrame(columns=['player_id', 'mpg', 'games_played', 'games_started', 'ppg', 'apg', 'rpg', 'spg', 'bpg',
                               'topg', 'pfpg', 'fta', 'ftm', 'ftp', 'fga', 'fgm', 'fgp', 'tpa', 'tpm', 'tpp'])
    for player in player_data:
        if player['isActive']:
            player_id = player['personId']
            PLAYER_STATS_API = f"https://data.nba.net/data/10s/prod/v1/{SEASON}/players/{player_id}_profile.json"
            print(PLAYER_STATS_API)
            player_stats = requests.get(PLAYER_STATS_API)
            team_id = player_stats.json()['league']['standard']['teamId']
            try:
                player_stats = player_stats.json(
                )['league']['standard']['stats']['regularSeason']['season'][0]['total']
            except:
                player_stats = player_stats.json(
                )['league']['standard']['stats']['latest']
            games_played = get_team_gp(team_id)
            player_games_played = player_stats['gamesPlayed']
            try:
                pfpg = str(
                    round(float(player_stats['pFouls'])/float(player_stats['gamesPlayed']), 2))
            except:
                pfpg = '0'

            mpg, ppg, apg, rpg, spg, bpg, topg, pfpg = player_stats['mpg'], player_stats['ppg'], player_stats[
                'apg'], player_stats['rpg'], player_stats['spg'], player_stats['bpg'], player_stats['topg'], pfpg
            try:
                if (float(player_games_played)/float(games_played)) < 0.70:
                    mpg = ppg = apg = rpg = spg = bpg = topg = pfpg = 'NQ'
            except:
                mpg = ppg = apg = rpg = spg = bpg = topg = pfpg = 'NQ'

            ftp, fgp, tpp, = player_stats['ftp'], player_stats['fgp'], player_stats['tpp']
            try:
                if (float(player_stats['ftm'])/float(player_stats['gamesPlayed'])) < 2:
                    ftp = 'NQ'
                if (float(player_stats['fgm'])/float(player_stats['gamesPlayed'])) < 4:
                    fgp = 'NQ'
                if (float(player_stats['tpm'])/float(player_stats['gamesPlayed'])) < 1:
                    tpp = 'NQ'
            except:
                ftp = 'NQ'
                fgp = 'NQ'
                tpp = 'NQ'
            data = {
                'player_id': player_id,
                'mpg': mpg,
                'games_played': player_stats['gamesPlayed'],
                'games_started': player_stats['gamesStarted'],
                'ppg': ppg,
                'apg': apg,
                'rpg': rpg,
                'spg': spg,
                'bpg': bpg,
                'topg': topg,
                'pfpg': pfpg,
                'fta': player_stats['fta'],
                'ftm': player_stats['ftm'],
                'ftp': ftp,
                'fga': player_stats['fga'],
                'fgm': player_stats['fgm'],
                'fgp': fgp,
                'tpa': player_stats['tpa'],
                'tpm': player_stats['tpm'],
                'tpp': tpp
            }
            df = df.append(data, ignore_index=True)
    return df


def gen_player_pctls(player_id, df):
    output = {}
    i = 0
    for columnName, columnData in df.iteritems():
        if (i > 0):
            re_add = df[df[columnName] == 'NQ']
            df = df[df[columnName] != 'NQ']
            df[columnName] = pd.to_numeric(df[columnName])
            df = df.append(re_add)
        i += 1
    i = 0
    for columnName, columnData in df.iteritems():
        if (i > 0):
            re_add = df[df[columnName] == 'NQ']
            df = df[df[columnName] != 'NQ']
            df = df.sort_values(by=columnName, ascending=True)
            df = df.reset_index(drop=True)
            player_stats = df.loc[df['player_id'] == player_id]
            try:
                percentile = str(
                    round(player_stats.index.values[0]/len(df) * 100, 2))
            except:
                percentile = 'NQ'
            output[columnName] = percentile
            df = df.append(re_add)
        i += 1
    return output


def main():
    df = create_df()
    for player in player_data:
        if player['isActive']:
            id = player['personId']
            data = json.dumps(gen_player_pctls((id), df))
            response = requests.request(
                'DELETE', BASE + f"player/basic_latest_pctls/{id}")
            headers = {'Content-Type': 'application/json'}
            response = requests.request(
                'POST', BASE + f"player/basic_latest_pctls/{id}", data=data, headers=headers)
            print(response.text)


if __name__ == "__main__":
    main()
