import pandas as pd

sans=pd.read_csv('datasets/sans_country2.csv')
mort=sans[sans['Year']==2016]
