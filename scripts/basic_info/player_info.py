"""
Puts and updates data into player info database
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
            data = json.dumps({
                "team_id": player["teamId"],
                "first_name": player["firstName"],
                "last_name": player["lastName"],
                "pos_abbr": player["pos"],
                "pos_full": player["teamSitesOnly"]["posFull"],
                "jersey_number": player["jersey"],
                "debut_year": player["nbaDebutYear"],
                "years_pro": player["yearsPro"],
                "height_feet": player["heightFeet"],
                "height_inches": player["heightInches"],
                "height_meters": player["heightMeters"],
                "weight_pounds": player["weightPounds"],
                "weight_kilos": player["weightKilograms"],
                "draft_team_id": player["draft"]["teamId"],
                "draft_year": player["draft"]["seasonYear"],
                "draft_round": player["draft"]["roundNum"],
                "draft_pick": player["draft"]["pickNum"],
                "college": player["collegeName"],
                "country": player["country"]
            })
            response = requests.request(
                'DELETE', BASE + f"player/info/{player_id}")
            headers = {'Content-type': 'application/json'}
            response = requests.request(
                "POST", BASE + f"player/info/{player_id}", data=data, headers=headers)
            print(response.text)


if __name__ == "__main__":
    main()
