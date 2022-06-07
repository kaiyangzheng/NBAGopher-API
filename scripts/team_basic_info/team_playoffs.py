"""
Puts and updates data in team playoffs database
"""
import requests
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup
import pandas as pd


BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
BBREF_SEASON = SEASON+1
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/teams.json"
team_data = requests.get(NBA_API)
team_data = team_data.json()['league']['standard']


def get_playoffs_data():
    html_text = urlopen(
        f'https://www.basketball-reference.com/playoffs/NBA_{BBREF_SEASON}.html')
    soup = BeautifulSoup(html_text.read(), 'lxml')
    table = soup.find('table', {'id': 'all_playoffs'})
    table = pd.read_html(str(table))[0]
    return table


def get_team_id(name):
    team_info = requests.get(
        'https://nbagopher-api.herokuapp.com/team/info')
    team_info = team_info.json()
    for key in team_info:
        if team_info[key]['name'] == name:
            return key
    return -1


def get_series_info(s):
    team1_wins = s.split('\xa0')[1].replace(
        '(', '').replace(')', '').split('-')[0]
    team2_wins = s.split('\xa0')[1].replace(
        '(', '').replace(')', '').split('-')[1]

    s = s.split(' \xa0')[0]
    keywords = [' trail ', ' lead ', ' tied with ', ' over ']
    for word in keywords:
        if word in s:
            s = s.split(word)
    team1_name = s[0]
    team2_name = s[1]

    team1_id = get_team_id(team1_name)
    team2_id = get_team_id(team2_name)

    return {'team1_id': team1_id, 'team1_wins': team1_wins, 'team2_id': team2_id, 'team2_wins': team2_wins}


def main():
    finals = []
    east_final = []
    west_final = []
    east_semis = []
    west_semis = []
    east_first = []
    west_first = []
    playoffs_data = get_playoffs_data()
    for index, row in playoffs_data.iterrows():
        if (row[0] == 'Finals'):
            finals.append(row[1])
        elif (row[0] == 'Eastern Conference Finals'):
            east_final.append(row[1])
        elif (row[0] == 'Western Conference Finals'):
            west_final.append(row[1])
        elif (row[0] == 'Eastern Conference Semifinals'):
            east_semis.append(row[1])
        elif (row[0] == 'Western Conference Semifinals'):
            west_semis.append(row[1])
        elif (row[0] == 'Eastern Conference First Round'):
            east_first.append(row[1])
        elif (row[0] == 'Western Conference First Round'):
            west_first.append(row[1])

    for i in range(len(finals)):
        finals[i] = get_series_info(finals[i])

    for i in range(len(east_final)):
        east_final[i] = get_series_info(east_final[i])
        west_final[i] = get_series_info(west_final[i])

    for i in range(len(east_semis)):
        east_semis[i] = get_series_info(east_semis[i])
        west_semis[i] = get_series_info(west_semis[i])

    for i in range(len(east_first)):
        east_first[i] = get_series_info(east_first[i])
        west_first[i] = get_series_info(west_first[i])

    data = {}
    data['west_first'] = west_first
    data['east_first'] = east_first
    data['west_semi'] = west_semis
    data['east_semi'] = east_semis
    data['west_final'] = west_final
    data['east_final'] = east_final
    data['nba_final'] = finals

    print(data['east_first'])

    data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        BASE + 'team/playoffs/west/first', data=data, headers=headers)
    print(response.text)
    response = requests.post(
        BASE + 'team/playoffs/east/first', data=data, headers=headers)
    print(response.text)
    response = requests.post(
        BASE + 'team/playoffs/west/semi', data=data, headers=headers)
    print(response.text)
    response = requests.post(
        BASE + 'team/playoffs/east/semi', data=data, headers=headers)
    print(response.text)
    response = requests.post(
        BASE + 'team/playoffs/west/final', data=data, headers=headers)
    print(response.text)
    response = requests.post(
        BASE + 'team/playoffs/east/final', data=data, headers=headers)
    print(response.text)
    response = requests.post(
        BASE + 'team/playoffs/nba/final', data=data, headers=headers)
    print(response.text)


if __name__ == "__main__":
    main()
