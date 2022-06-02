import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle

df = pd.read_csv('ML/data/Seasons_Stats.csv')

df = df[df['Year'] >= 1997]

x_data = []
y_data = []

for index, row in df.iterrows():
    player_name = row['Player']
    player_df = df[df['Player'] == player_name]
    i = 0
    for index, row in player_df.iterrows():
        if (i < len(player_df) - 1):
            x_data.append([i, row['MP']/row['G'], row['TS%'], row['TRB%'], row['AST%'], row['STL%'], row['BLK%'], row['TOV%'], row['USG%'], row['BPM'],
                          row['TRB']/row['G'], row['AST']/row['G'], row['STL']/row['G'], row['BLK']/row['G'], row['TOV']/row['G'], row['PTS']/row['G']])
            y_data.append([player_df.iloc[i+1]['TS%'], player_df.iloc[i+1]['MP']/player_df.iloc[i+1]['G'], player_df.iloc[i+1]['PTS']/player_df.iloc[i+1]['G'], player_df.iloc[i+1]
                          ['AST']/player_df.iloc[i+1]['G'], player_df.iloc[i+1]['TRB']/player_df.iloc[i+1]['G'], player_df.iloc[i+1]['BLK'], player_df.iloc[i+1]['STL'], player_df.iloc[i+1]['BPM']])
        i += 1
    df = df[df['Player'] != player_name]

x_data = np.nan_to_num(x_data)
y_data = np.nan_to_num(y_data)

best = 0
for i in range(1000):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
        x_data, y_data, test_size=0.2)
    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)
    acc = model.score(x_test, y_test)
    print(acc)

    if acc > best:
        best = acc
        with open("ML/classifiers/future_perf.pickle", "wb") as f:
            pickle.dump(model, f)
print(best)
