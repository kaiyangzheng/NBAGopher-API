import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from random import randint
import pandas as pd
from urllib.request import urlopen
import unidecode
from bs4 import BeautifulSoup
import numpy as np

dpoy_table = pd.read_csv('ML/data/DPOY.csv')

player_list = dpoy_table['Player'].tolist()
seasons_list = dpoy_table['Season'].tolist()
player_names = []
player_links = []
player_seasons = []
i = 0
for player in player_list:
    player_links.append(player.split('\\')[1])
    player_names.append(player.split('\\')[0])
    player_seasons.append(seasons_list[i])
    i += 1

dpoy_stats = []
for i in range(len(player_links)):
    html_text = urlopen(
        f'https://www.basketball-reference.com/players/{player_links[i][0]}/{player_links[i]}.html')
    soup = BeautifulSoup(html_text.read(), 'lxml')
    basic_table = soup.find('table', {'id': 'per_game'})
    advanced_table = soup.find('table', {'id': 'advanced'})
    basic_table = pd.read_html(str(basic_table))[0]
    advanced_table = pd.read_html(str(advanced_table))[0]

    basic_table = basic_table[basic_table['Season'] == player_seasons[i]]
    advanced_table = advanced_table[advanced_table['Season']
                                    == player_seasons[i]]

    dpoy_stats.append([basic_table['TRB'].tolist()[0], basic_table['STL'].tolist()[0], basic_table['BLK'].tolist()[0],
                      advanced_table['TRB%'].tolist()[0], advanced_table['STL%'].tolist()[0], advanced_table['BLK%'].tolist()[0], advanced_table['DBPM'].tolist()[0]])

dpoy_stats = np.array(dpoy_stats).astype(float)


season = 2021
non_dpoy_stats = []
while season >= 1983:
    html_text = urlopen(
        f'https://www.basketball-reference.com/leagues/NBA_{season}_per_game.html')
    soup = BeautifulSoup(html_text.read(), 'lxml')
    basic_table = soup.find('table', {'id': 'per_game_stats'})
    basic_table = pd.read_html(str(basic_table))[0]

    html_text = urlopen(
        f'https://www.basketball-reference.com/leagues/NBA_{season}_advanced.html')
    soup = BeautifulSoup(html_text.read(), 'lxml')
    advanced_table = soup.find('table', {'id': 'advanced_stats'})
    advanced_table = pd.read_html(str(advanced_table))[0]

    basic_table = basic_table[basic_table['Player'] != 'Player']
    advanced_table = advanced_table[advanced_table['Player'] != 'Player']

    basic_table = basic_table[~basic_table['Player'].isin(player_names)]
    advanced_table = advanced_table[~advanced_table['Player'].isin(
        player_names)]

    table_length = len(basic_table)
    for i in range(5):
        random_player_index = randint(0, table_length-1)
        basic_stats = basic_table.iloc[random_player_index]
        advanced_stats = advanced_table.iloc[random_player_index]
        non_dpoy_stats.append([basic_stats['TRB'], basic_stats['STL'], basic_stats['BLK'],
                               advanced_stats['TRB%'], advanced_stats['STL%'], advanced_stats['BLK%'], advanced_stats['DBPM']])
    season -= 1

labels = []
for i in range(len(dpoy_stats)):
    labels.append(1)

for i in range(len(non_dpoy_stats)):
    labels.append(0)


dpoy_stats = np.array(dpoy_stats)
non_dpoy_stats = np.array(non_dpoy_stats)

x_data = np.concatenate((dpoy_stats, non_dpoy_stats), axis=0)
y_data = np.array(labels)

x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.2, random_state=42)


logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)

predictions = logisticRegr.predict(x_test)
print(predictions)
score = logisticRegr.score(x_test, y_test)
print(score)

logistic_regression = LogisticRegression()
logistic_regression.fit(x_data, y_data)

pickle.dump(logistic_regression, open(
    'ML/classifiers/DPOY_classifier.pkl', 'wb'))
