"""
Puts and updates data into the player bbr id database
"""
from inspect import getblock
import requests
import string
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
import unidecode
import json

BASE = "https://nbagopher-api.herokuapp.com/"
BASE_TEST = "http://localhost:5000/"
SEASON = 2021
BBREF_SEASON = SEASON+1
NBA_API = f"http://data.nba.net/data/10s/prod/v1/{SEASON}/players.json"
player_data = requests.get(NBA_API)
player_data = player_data.json()['league']['standard']
alphabet = list(string.ascii_lowercase)


def get_Bbr_id(player_name, last_name):
    letter_index = last_name[0].lower()
    bbr_url = f"https://www.basketball-reference.com/players/{letter_index}/"
    html_text = urlopen(bbr_url)
    soup = BeautifulSoup(html_text.read(), 'lxml')
    table = soup.find('table', {'id': 'players'})
    a_tags = table.find_all('a')
    for tag in a_tags:
        name = unidecode.unidecode(tag.text.strip()).replace('*', '')
        name = name.replace('.', '')
        player_name = player_name.replace('.', '')
        # edge cases :(
        if (player_name == "Kevin Knox II"):
            player_name = "Kevin Knox"
        if (player_name == 'Marcus Morris Sr'):
            player_name = 'Marcus Morris'
        if (player_name == 'Jason Preston'):
            return '/players/p/prestja01.html'
        if (player_name == 'Xavier Tillman'):
            player_name = 'Xavier Tillman Sr.'
        if (player_name == 'Robert Williams III'):
            player_name = 'Robert Williams'
        # compare
        if (name == player_name):
            return tag['href']
    print('ERROR!')
    print(player_name)
    return ''


def main():
    for player in player_data:
        if (player['isActive']):
            player_id = player['personId']
            player_name = player['firstName'] + ' ' + player['lastName']
            last_name = player['lastName']
            bbr_id = get_Bbr_id(player_name, last_name)
            data = json.dumps({
                'bbr_id': bbr_id
            })
            response = requests.request(
                'DELETE', BASE + f"player/bbr_id/{player_id}")
            headers = {'Content-Type': 'application/json'}
            print(data)
            response = requests.request(
                'POST', BASE + f"player/bbr_id/{player_id}", data=data, headers=headers)
            print(response.text)


if __name__ == "__main__":
    main()
