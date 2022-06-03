"""
Puts and updates data into player basic latest stats database
"""
import requests
import json

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']


def main():
    for player in player_data:
        if (player['isActive']):
            player_id = player['personId']
            PLAYER_STATS_API = f"https://data.nba.net/data/10s/prod/v1/{SEASON}/players/{player_id}_profile.json"
            print(PLAYER_STATS_API)
            player_stats = requests.get(PLAYER_STATS_API)
            try:
                player_stats = player_stats.json(
                )['league']['standard']['stats']['regularSeason']['season'][0]['total']
            except:
                player_stats = player_stats.json(
                )['league']['standard']['stats']['latest']
            try:
                pfpg = str(
                    round(float(player_stats['pFouls'])/float(player_stats['gamesPlayed']), 2))
            except:
                pfpg = '0'
            try:
                data = json.dumps({
                    'mpg': player_stats['mpg'],
                    'games_played': player_stats['gamesPlayed'],
                    'games_started': player_stats['gamesStarted'],
                    'ppg': player_stats['ppg'],
                    'apg': player_stats['apg'],
                    'rpg': player_stats['rpg'],
                    'spg': player_stats['spg'],
                    'bpg': player_stats['bpg'],
                    'topg': player_stats['topg'],
                    'pfpg': pfpg,
                    'fta': player_stats['fta'],
                    'ftm': player_stats['ftm'],
                    'ftp': player_stats['ftp'],
                    'fga': player_stats['fga'],
                    'fgm': player_stats['fgm'],
                    'fgp': player_stats['fgp'],
                    'tpa': player_stats['tpa'],
                    'tpm': player_stats['tpm'],
                    'tpp': player_stats['tpp']
                })
            except:
                data = json.dumps({
                    'mpg': '0',
                    'games_played': '0',
                    'games_started': '0',
                    'ppg': '0',
                    'apg': '0',
                    'rpg': '0',
                    'spg': '0',
                    'bpg': '0',
                    'topg': '0',
                    'pfpg': '0',
                    'fta': '0',
                    'ftm': '0',
                    'ftp': '0',
                    'fga': '0',
                    'fgm': '0',
                    'fgp': '0',
                    'tpa': '0',
                    'tpm': '0',
                    'tpp': '0'
                })
            response = requests.request(
                'DELETE', BASE + f"player/basic_latest/{player_id}")
            headers = {'Content-type': 'application/json'}
            response = requests.request(
                'POST', BASE + f"player/basic_latest/{player_id}", data=data, headers=headers)
            print(response.text)


if __name__ == "__main__":
    main()
