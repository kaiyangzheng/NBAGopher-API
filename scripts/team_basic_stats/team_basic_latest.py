"""
Puts and updates data into team basic stats
"""
import requests
import json

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/team_stats_rankings.json"
team_data = requests.get(NBA_API)
team_data = team_data.json()['league']['standard']['regularSeason']['teams']

NBA_API_STATS = ['min', 'fgp', 'ftp', 'tpp', 'orpg', 'drpg',
                 'trpg', 'apg', 'spg', 'bpg', 'pfpg', 'ppg', 'oppg', 'eff']
REST_API_STATS = ['mpg', 'fgp', 'ftp', 'tpp', 'orpg', 'drpg',
                  'trpg', 'apg', 'spg', 'bpg', 'pfpg', 'ppg', 'oopg', 'netppg']


def main():
    for team in team_data:
        data = {}
        rankings_data = {}
        teamId = team['teamId']
        for i in range(len(NBA_API_STATS)):
            data[REST_API_STATS[i]] = team[NBA_API_STATS[i]]["avg"]
            rankings_data[REST_API_STATS[i]] = team[NBA_API_STATS[i]]["rank"]
        headers = {'Content-type': 'application/json'}
        data = json.dumps(data)
        response = requests.delete(BASE + f"team/stats/basic/{teamId}")
        response = requests.delete(BASE + f"/team/stats/rankings/{teamId}")
        response = requests.post(
            BASE + f'team/stats/basic/{teamId}', data=data, headers=headers)
        print(response.text)
        response = requests.post(
            BASE + f'team/stats/basic/rankings/{teamId}', data=json.dumps(rankings_data), headers=headers)

        print(response.text)


if __name__ == "__main__":
    main()
