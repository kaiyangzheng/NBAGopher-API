"""
Get 3 featured teams to display on front page
"""
import requests
import json

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
BBREF_SEASON = SEASON+1


def featured_offense():
    API = "https://nbagopher-api.herokuapp.com/team/stats/advanced/all"
    teams_advanced = requests.get(API)
    teams_advanced = teams_advanced.json()

    for team in teams_advanced:
        if teams_advanced[team]['advanced_rankings']['ORTG'] == "1":
            return team


def featured_defense():
    API = "https://nbagopher-api.herokuapp.com/team/stats/advanced/all"
    teams_advanced = requests.get(API)
    teams_advanced = teams_advanced.json()

    for team in teams_advanced:
        if teams_advanced[team]['advanced_rankings']['DRTG'] == "30":
            return team


def featured_overall():
    API = "https://nbagopher-api.herokuapp.com/team/standings"
    teams_standings = requests.get(API)
    teams_standings = teams_standings.json()

    highest_win_pctg = 0
    highest_win_pctg_id = ""
    for team in teams_standings:
        if float(teams_standings[team]['win_pctg']) > highest_win_pctg:
            highest_win_pctg = float(teams_standings[team]['win_pctg'])
            highest_win_pctg_id = team

    return highest_win_pctg_id


def main():
    featured_offense_id, featured_defense_id, featured_overall_id = featured_offense(
    ), featured_defense(), featured_overall()

    data = {
        'featured_offense_id': featured_offense_id,
        'featured_defense_id': featured_defense_id,
        'featured_overall_id': featured_overall_id
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(BASE + "featured_teams",
                             data=json.dumps(data), headers=headers)
    print(response.text)


if __name__ == "__main__":
    main()
