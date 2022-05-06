import pandas as pd

x = pd.read_csv('music.csv')
y = x.describe()
z = x.values

x_in = x.drop(columns=['genre'])
x_out = x['genre']