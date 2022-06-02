import pickle
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from random import randint
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np

smoy_table = pd.read_csv('ML\data\\6MOY.csv')

player_list = smoy_table['Player'].tolist()
player_seasons = smoy_table['Season'].tolist()
player_names = []
player_links = []
for player in player_list:
    player_links.append(player.split('\\')[1])
    player_names.append(player.split('\\')[0])

smoy_stats = []
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

    smoy_stats.append([basic_table['PTS'].tolist()[0], basic_table['AST'].tolist()[0], basic_table['TRB'].tolist()[
                      0], advanced_table['TS%'].tolist()[0], advanced_table['BPM'].tolist()[0]])

smoy_stats = np.array(smoy_stats).astype(float)

season = 2021
non_smoy_stats = []
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
        non_smoy_stats.append([basic_stats['PTS'], basic_stats['AST'],
                              basic_stats['TRB'], advanced_stats['TS%'], advanced_stats['BPM']])
    season -= 1
non_smoy_stats = np.array(non_smoy_stats).astype(float)

labels = []
for i in range(len(smoy_stats)):
    labels.append(1)

for i in range(len(non_smoy_stats)):
    labels.append(0)


x_data = np.concatenate((smoy_stats, non_smoy_stats), axis=0)
x_data = np.nan_to_num(x_data, nan=0)
y_data = np.array(labels)


x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.2, random_state=42)


LR_classifier = LogisticRegression()
LR_classifier.fit(x_train, y_train)

SVC_classifier = SVC(probability=True)
SVC_classifier.fit(x_train, y_train)

LR_predictions = LR_classifier.predict(x_test)
SVC_predictions = SVC_classifier.predict(x_test)

LR_score = LR_classifier.score(x_test, y_test)
SVC_score = SVC_classifier.score(x_test, y_test)

print('LR score: ' + str(LR_score))
print('SVC score: ' + str(SVC_score))

pickle.dump(SVC_classifier, open('ML/classifiers/6MOY_classifier.pkl', 'wb'))
