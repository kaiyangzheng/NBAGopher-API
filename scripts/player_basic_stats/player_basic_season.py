"""
Puts and updates data into player basic season stats database
"""
import requests
import json

BASE = "https://nbagopher-api.herokuapp.com/"
SEASON = 2021
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']


def main():
    for player in player_data:
        if (player['isActive']):
            player_id = player['personId']
            PLAYER_STATS_API = f"https://data.nba.net/data/10s/prod/v1/{SEASON}/players/{player_id}_profile.json"
            player_stats = requests.get(PLAYER_STATS_API)
            player_stats = player_stats.json(
            )['league']['standard']['stats']['regularSeason']['season']
            for stats in player_stats:
                season_stats = stats['total']
                try:
                    pfpg = str(
                        round(float(season_stats['pFouls'])/float(season_stats['gamesPlayed']), 2))
                except:
                    pfpg = '0'
                data = json.dumps({
                    'mpg': season_stats['mpg'],
                    'games_played': season_stats['gamesPlayed'],
                    'games_started': season_stats['gamesStarted'],
                    'ppg': season_stats['ppg'],
                    'apg': season_stats['apg'],
                    'rpg': season_stats['rpg'],
                    'spg': season_stats['spg'],
                    'bpg': season_stats['bpg'],
                    'topg': season_stats['topg'],
                    'pfpg': pfpg,
                    'fta': season_stats['fta'],
                    'ftm': season_stats['ftm'],
                    'ftp': season_stats['ftp'],
                    'fga': season_stats['fga'],
                    'fgm': season_stats['fgm'],
                    'fgp': season_stats['fgp'],
                    'tpa': season_stats['tpa'],
                    'tpm': season_stats['tpm'],
                    'tpp': season_stats['tpp']
                })
                response = requests.request(
                    'DELETE', BASE + f"player/basic_stats/{player_id}/{stats['seasonYear']}")
                headers = {'Content-type': 'application/json'}
                response = requests.request(
                    'POST', BASE + f"player/basic_stats/{player_id}/{stats['seasonYear']}", data=data, headers=headers)
                print(response.text)


if __name__ == "__main__":
    main()
