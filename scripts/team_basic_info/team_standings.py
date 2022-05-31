"""
puts and updates data into team standings db
"""
import requests
import json

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
NBA_API = f"https://data.nba.net/data/10s/prod/v1/current/standings_all.json"
team_data = requests.get(NBA_API)
team_data = team_data.json()['league']['standard']['teams']

NBA_API_stats = ['win', 'loss', 'winPct', 'lossPct', 'gamesBehind', 'confRank',
                 'homeWin', 'homeLoss', 'awayWin', 'awayLoss', 'lastTenWin', 'lastTenLoss', 'streak']
REST_API_stat_names = ['wins', 'losses', 'win_pctg', 'loss_pctg', 'games_back', 'conf_rank',
                       'home_wins', 'home_losses', 'away_wins', 'away_losses', 'last_ten_wins', 'last_ten_losses', 'streak']


def main():
    for team in team_data:
        data = {}
        team_id = team['teamId']
        for i in range(len(NBA_API_stats)):
            data[REST_API_stat_names[i]] = team[NBA_API_stats[i]]
        headers = {'Content-type': 'application/json'}
        data = json.dumps(data)
        response = requests.delete(BASE + f"team/standings/{team_id}")
        response = requests.post(
            BASE + f'team/standings/{team_id}', data=data, headers=headers)
        print(response.text)


if __name__ == "__main__":
    main()
