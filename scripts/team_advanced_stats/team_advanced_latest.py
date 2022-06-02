"""
Puts and updates data into team advanced stats
"""
import requests
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

BBREF_SEASON = 2022
BASE = f"https://www.basketball-reference.com/leagues/NBA_{BBREF_SEASON}.html"

REST_API_STATS = ['', 'Team', '', '', '', '', '', '', '', '', 'ORTG', 'DRTG', 'NRTG', 'Pace', 'FTr', 'TPAr', 'TS_pctg', '', 'eFG_pctg', 'TOV_pctg',
                  'ORB_pctg', 'FT_per_FGA', '',  'opp_eFG_pctg', 'opp_TOV_pctg', 'DRB_pctg', 'opp_FT_per_FGA', '', '', '', '']


def get_team_id(name):
    response = requests.get('https://nbagopher-api.herokuapp.com/team/info')
    teams_data = response.json()
    for team in teams_data:
        if (teams_data[team]['name'] == name):
            return team


def gen_advanced_table():
    html_text = urlopen(BASE)
    soup = BeautifulSoup(html_text.read(), 'lxml')
    table = soup.find('table', {'id': 'advanced-team'})
    team_advanced = pd.read_html(str(table))[0]
    team_advanced.columns = REST_API_STATS
    teams = team_advanced['Team'].tolist()
    for i in range(len(teams)):
        teams[i] = teams[i].replace('*', '')
    team_advanced['Team'] = teams
    team_advanced = team_advanced.drop(axis=0, index=len(teams)-1)

    return team_advanced


def gen_stat_ranks(table, stat, team):
    stat_list = table[stat].tolist()
    for i in range(len(stat_list)):
        stat_list[i] = float(stat_list[i])
    table[stat] = stat_list
    table = table.sort_values(by=[stat], ascending=False)
    table = table.reset_index()
    for (index, row) in table.iterrows():
        if (row['Team'] == team):
            return str(index+1)


def main():
    table = gen_advanced_table()

    for index, row in table.iterrows():
        data = {}
        data_ranks = {}
        for (columnName, columnData) in row.iteritems():
            if columnName != '' and columnName != 'Team':
                data[columnName] = columnData
                data_ranks[columnName] = gen_stat_ranks(
                    table, columnName, row['Team'])
        teamId = get_team_id(row['Team'])
        response = requests.delete(
            f'https://nbagopher-api.herokuapp.com/team/stats/advanced/{teamId}')
        response = requests.delete(
            f'https://nbagopher-api.herokuapp.com/team/stats/advanced/rankings/{teamId}')
        headers = {'Content-type': 'application/json'}
        response = requests.post(
            f'https://nbagopher-api.herokuapp.com/team/stats/advanced/{teamId}', data=json.dumps(data), headers=headers)
        print(response.text)
        response = requests.post(
            f'https://nbagopher-api.herokuapp.com/team/stats/advanced/rankings/{teamId}', data=json.dumps(data_ranks), headers=headers)
        print(response.text)


if __name__ == '__main__':
    main()
