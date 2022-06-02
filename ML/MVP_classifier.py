import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

mvp_data = pd.read_csv('nba_mvp_data.csv')

year = ""
mvp_place = 1
mvp_stats = []
for index, row in mvp_data.iterrows():
    if row['year'] != year:
        mvp_place = 1
        year = row['year']
    if mvp_place <= 3:
        mvp_stats.append(np.array([row['min_avg'], row['pts_avg'], row['rb_avg'], row['ast_avg'], row['stl_avg'], row['blk_avg'],
                         row['fg_perc'], row['3pt_perc'], row['ft_perc'], row['ws'], row['ws_48'], row['win_perc']]).astype(np.float).tolist())
    mvp_place += 1


print(mvp_stats)

mvp_players = mvp_data['player'].tolist()

common_player_data = pd.read_csv('Seasons_Stats.csv')
common_player_stats = []
for index, row in common_player_data.iterrows():
    if row['Year'] >= 2001 and row['Player'] not in mvp_players:
        common_player_stats.append([30, row['PTS'], row['TRB'], row['AST'], row['STL'],
                                   row['BLK'], row['FG%'], row['3P%'], row['FT%'], row['WS'], row['WS/48'], 0.30])

print("common player stats:", common_player_stats[0:10])

x_data = []
y_data = []

for i in range(len(common_player_stats)):
    x_data.append(common_player_stats[i])
    y_data.append(0)


for i in range(len(mvp_stats)):
    x_data.append(mvp_stats[i])
    y_data.append(1)

x_data = np.array(x_data)
y_data = np.array(y_data)

x_data[np.isnan(x_data)] = 0
y_data[np.isnan(y_data)] = 0

x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.25, random_state=0)


logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)

logisticRegr.predict(x_test[0].reshape(1, -1))

predictions = logisticRegr.predict(x_test)
print(predictions)
score = logisticRegr.score(x_test, y_test)
print(score)

pickle.dump(logisticRegr, open('ML/classifiers/mvp_model.pkl', 'wb'))
