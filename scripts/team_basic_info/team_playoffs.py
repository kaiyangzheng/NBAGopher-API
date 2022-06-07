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


playoffs_data = get_playoffs_data()
playoffs_data.to_csv('scripts/team_basic_info/playoffs_data.csv')
