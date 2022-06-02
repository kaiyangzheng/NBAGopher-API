import pickle
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from random import randint
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np

mip_table = pd.read_csv('ML/data/MIP.csv')

player_list = mip_table['Player'].tolist()
season_list = mip_table['Season'].tolist()
player_names = []
player_links = []
player_seasons = []
i = 0
for player in player_list:
    player_links.append(player.split('\\')[1])
    player_names.append(player.split('\\')[0])
    player_seasons.append(season_list[i])
    i += 1

mip_year_stats = []
mip_prev_stats = []
mip_stats_diff = []
for i in range(len(player_links)):
    html_text = urlopen(
        f'https://www.basketball-reference.com/players/{player_links[i][0]}/{player_links[i]}.html')
    print(
        f'https://www.basketball-reference.com/players/{player_links[i][0]}/{player_links[i]}.html')
    soup = BeautifulSoup(html_text.read(), 'lxml')
    basic_table = soup.find('table', {'id': 'per_game'})
    advanced_table = soup.find('table', {'id': 'advanced'})

    basic_table = pd.read_html(str(basic_table))[0]
    advanced_table = pd.read_html(str(advanced_table))[0]

    basic_table = basic_table.fillna(0)
    advanced_table = advanced_table.fillna(0)

    mip_year = player_seasons[i]
    past_year = player_seasons[i].split('-')
    first = str(int(past_year[0])-1)
    second = str(int(past_year[1])-1)
    if len(second) == 1:
        second = '0' + second
    if (second == '-1'):
        second = '99'
    past_year = first + '-' + second

    basic_table_mip = basic_table[basic_table['Season'] == player_seasons[i]]
    advanced_table_mip = advanced_table[advanced_table['Season']
                                        == player_seasons[i]]

    basic_table_past = basic_table[basic_table['Season'] == past_year]
    advanced_table_past = advanced_table[advanced_table['Season'] == past_year]
    print(player_links[i])
    if (player_links[i] != 'austiis01' and player_links[i] != 'johnske02' and player_links[i] != 'duckwke01'):
        mip_year_stats = ([basic_table_mip['PTS'].to_string(index=False), basic_table_mip['AST'].to_string(index=False), basic_table_mip['TRB'].to_string(index=False), basic_table_mip['STL'].to_string(index=False), basic_table_mip['BLK'].to_string(
            index=False), basic_table_mip['FG%'].to_string(index=False), basic_table_mip['3P%'].to_string(index=False), basic_table_mip['FT%'].to_string(index=False), advanced_table_mip['BPM'].to_string(index=False)])
        mip_prev_stats = ([basic_table_past['PTS'].to_string(index=False), basic_table_past['AST'].to_string(index=False), basic_table_past['TRB'].to_string(index=False), basic_table_past['STL'].to_string(index=False), basic_table_past['BLK'].to_string(
            index=False), basic_table_past['FG%'].to_string(index=False), basic_table_past['3P%'].to_string(index=False), basic_table_past['FT%'].to_string(index=False), advanced_table_past['BPM'].to_string(index=False)])
    print(past_year)
    print([basic_table_past['PTS'].to_string(index=False), basic_table_past['AST'].to_string(index=False), basic_table_past['TRB'].to_string(index=False), basic_table_past['STL'].to_string(index=False), basic_table_past['BLK'].to_string(
        index=False), basic_table_past['FG%'].to_string(index=False), basic_table_past['3P%'].to_string(index=False), basic_table_past['FT%'].to_string(index=False), advanced_table_past['BPM'].to_string(index=False)])

    mip_stats_diff.append(np.subtract(np.array(mip_year_stats).astype(float), np.array(mip_prev_stats).astype(float)).tolist(
    ) + [basic_table_mip['PTS'].to_string(index=False), basic_table_mip['AST'].to_string(index=False), basic_table_mip['TRB'].to_string(index=False)])
    print(np.subtract(np.array(mip_year_stats).astype(float), np.array(mip_prev_stats).astype(float)).tolist(
    ) + [basic_table_mip['PTS'].to_string(index=False), basic_table_mip['AST'].to_string(index=False), basic_table_mip['TRB'].to_string(index=False)])


print(mip_prev_stats[0])
print(mip_year_stats[0])
print(mip_stats_diff[0])


season = 2021
non_mip_stats = []
while season >= 1986:
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

    html_text = urlopen(
        f'https://www.basketball-reference.com/leagues/NBA_{season-1}_per_game.html')
    soup = BeautifulSoup(html_text.read(), 'lxml')
    basic_table_past = soup.find('table', {'id': 'per_game_stats'})
    basic_table_past = pd.read_html(str(basic_table_past))[0]

    html_text = urlopen(
        f'https://www.basketball-reference.com/leagues/NBA_{season-1}_advanced.html')
    soup = BeautifulSoup(html_text.read(), 'lxml')
    advanced_table_past = soup.find('table', {'id': 'advanced_stats'})
    advanced_table_past = pd.read_html(str(advanced_table_past))[0]

    basic_table = basic_table[basic_table['Player'] != 'Player']
    advanced_table = advanced_table[advanced_table['Player'] != 'Player']
    basic_table_past = basic_table_past[basic_table_past['Player'] != 'Player']
    advanced_table_past = advanced_table_past[advanced_table_past['Player'] != 'Player']

    basic_table = basic_table[~basic_table['Player'].isin(player_names)]
    advanced_table = advanced_table[~advanced_table['Player'].isin(
        player_names)]
    basic_table_past = basic_table_past[~basic_table_past['Player'].isin(
        player_names)]
    advanced_table_past = advanced_table_past[~advanced_table_past['Player'].isin(
        player_names)]

    player_list = basic_table['Player'].tolist()
    basic_table_past = basic_table_past[basic_table_past['Player'].isin(
        player_list)]
    advanced_table_past = advanced_table_past[advanced_table_past['Player'].isin(
        player_list)]

    basic_table = basic_table.fillna(0)
    advanced_table = advanced_table.fillna(0)
    basic_table_past = basic_table_past.fillna(0)
    advanced_table_past = advanced_table_past.fillna(0)

    table_length = len(basic_table)
    for i in range(5):
        while (True):
            try:
                random_player_index = randint(0, table_length-1)
                basic_stats = basic_table.iloc[random_player_index]
                advanced_stats = advanced_table.iloc[random_player_index]
                player = basic_stats['Player']

                basic_stats_past = basic_table_past[basic_table_past['Player'] == player]
                advanced_stats_past = advanced_table_past[advanced_table_past['Player'] == player]

                player = basic_stats['Player']
                non_mip_current_stats = [basic_stats['PTS'], basic_stats['AST'], basic_stats['TRB'], basic_stats['STL'],
                                         basic_stats['BLK'], basic_stats['FG%'], basic_stats['3P%'], basic_stats['FT%'], advanced_stats['BPM']]
                non_mip_past_stats = [basic_stats_past['PTS'].to_string(index=False), basic_stats_past['AST'].to_string(
                    index=False), basic_stats_past['TRB'].to_string(index=False), basic_stats_past['STL'].to_string(index=False), basic_stats_past['BLK'].to_string(index=False), basic_stats_past['FG%'].to_string(index=False), basic_stats_past['3P%'].to_string(index=False), basic_stats_past['FT%'].to_string(index=False), advanced_stats_past['BPM'].to_string(index=False)]

                non_mip_current_stats = np.array(
                    non_mip_current_stats).astype(float)
                non_mip_past_stats = np.array(non_mip_past_stats).astype(float)
                prediction_stats = np.subtract(
                    non_mip_current_stats, non_mip_past_stats).tolist()
                prediction_stats = prediction_stats + \
                    [basic_stats['PTS'], basic_stats['AST'], basic_stats['TRB']]
                non_mip_stats.append(prediction_stats)
                print(prediction_stats)

            except:
                print('error')
            else:
                break

    season -= 1

print(non_mip_stats)

labels = []
data = []
for i in range(len(mip_stats_diff)):
    labels.append(1)
    data.append(mip_stats_diff[i])
for i in range(len(non_mip_stats)):
    labels.append(0)
    data.append(non_mip_stats[i])

print(data[0])
print(data[len(data)-1])


x_train, x_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.1, random_state=42)


logisticRegr = SVC(probability=True)
logisticRegr.fit(x_train, y_train)

predictions = logisticRegr.predict(x_test)
print(predictions)
score = logisticRegr.score(x_test, y_test)
print(score)

pickle.dump(logisticRegr, open('ML/classifiers/MIP_classifier.pkl', 'wb'))
