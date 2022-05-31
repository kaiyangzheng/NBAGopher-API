"""
Puts and updates data into player basic latest stats database
"""
import requests
import json

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2020
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']


def main():
    for player in player_data:
        if (player['isActive']):
            player_id = player['personId']
            PLAYER_STATS_API = f"https://data.nba.net/data/10s/prod/v1/{SEASON}/players/{player_id}_profile.json"
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
            response = requests.request(
                'DELETE', BASE + f"player/basic_prev_stats/{player_id}")
            headers = {'Content-type': 'application/json'}
            response = requests.request(
                'POST', BASE + f"player/basic_prev_stats/{player_id}", data=data, headers=headers)
            print(response.text)


if __name__ == "__main__":
    main()
