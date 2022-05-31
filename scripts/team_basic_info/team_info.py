"""
Puts and updates data into team info database
"""
import requests
import json

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/teams.json"
team_data = requests.get(NBA_API)
team_data = team_data.json()['league']['standard']

NBA_API_stats = ['city', 'fullName', 'tricode', 'confName', 'divName']
REST_API_stat_names = ['city', 'name', 'tricode', 'conference', 'division']


def main():
    for team in team_data:
        if (team['isNBAFranchise']):
            data = {}
            team_id = team['teamId']
            for i in range(len(NBA_API_stats)):
                data[REST_API_stat_names[i]] = team[NBA_API_stats[i]]
            headers = {'Content-type': 'application/json'}
            data = json.dumps(data)
            response = requests.delete(BASE + f"team/info/{team_id}")
            response = requests.post(
                BASE + f'team/info/{team_id}', data=data, headers=headers)
            print(response.text)


if __name__ == "__main__":
    main()
