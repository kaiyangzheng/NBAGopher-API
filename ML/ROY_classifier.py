import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from random import randint
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np

roy_table = pd.read_csv('ML/data/ROY.csv')

player_list = roy_table['Player'].tolist()
player_seasons = roy_table['Season'].tolist()
player_names = []
player_links = []
for player in player_list:
    player_links.append(player.split('\\')[1])
    player_names.append(player.split('\\')[0])

print(player_names)
print(player_links)
print(player_seasons)

roy_stats = []
for i in range(30):

    html_text = urlopen(
        f'https://www.basketball-reference.com/players/{player_links[i][0]}/{player_links[i]}.html')
    print(
        f'https://www.basketball-reference.com/players/{player_links[i]}/{player_links[i]}.html')
    print(player_seasons[i])
    soup = BeautifulSoup(html_text.read(), 'lxml')
    basic_table = soup.find('table', {'id': 'per_game'})
    advanced_table = soup.find('table', {'id': 'advanced'})

    basic_table = pd.read_html(str(basic_table))[0]
    advanced_table = pd.read_html(str(advanced_table))[0]

    basic_table = basic_table[basic_table['Season'] == player_seasons[i]]
    advanced_table = advanced_table[advanced_table['Season']
                                    == player_seasons[i]]

    roy_stats.append([basic_table['PTS'].tolist()[0], basic_table['AST'].tolist()[0], basic_table['TRB'].tolist()[
                     0], advanced_table['TS%'].tolist()[0], advanced_table['BPM'].tolist()[0]])

roy_stats = np.array(roy_stats).astype(float)
print(roy_stats)
print(len(roy_stats))

season = 2021
non_roy_stats = []
while season >= 1991:
    print(season)
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
        random_player_index = randint(0, table_length - 1)
        basic_stats = basic_table.iloc[random_player_index]
        advanced_stats = advanced_table.iloc[random_player_index]
        non_roy_stats.append([basic_stats['PTS'], basic_stats['AST'],
                             basic_stats['TRB'], advanced_stats['TS%'], advanced_stats['BPM']])
    season -= 1
non_roy_stats = np.array(non_roy_stats).astype(float)
print(non_roy_stats)

labels = []
for i in range(len(roy_stats)):
    labels.append(1)

for i in range(len(non_roy_stats)):
    labels.append(0)


x_data = np.concatenate((roy_stats, non_roy_stats), axis=0)
x_data = np.nan_to_num(x_data, nan=0)
y_data = np.array(labels)

x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.2, random_state=42)

SVC_classifier = SVC(probability=True)
SVC_classifier.fit(x_train, y_train)

LR_classifier = LogisticRegression()
LR_classifier.fit(x_train, y_train)

SVC_predictions = SVC_classifier.predict(x_test)
SVC_score = SVC_classifier.score(x_test, y_test)

LR_predictions = LR_classifier.predict(x_test)
LR_score = LR_classifier.score(x_test, y_test)

print('SVC Score: ' + str(SVC_score))

print('LR Score: ' + str(LR_score))

pickle.dump(SVC_classifier, open('ML/classifiers/ROY_classifier.pkl', 'wb'))
