import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def clean_data(df):
    print(df.head(3))
    df = df.drop(['team', 'opp'], axis=1)
    df = df.dropna()
    
    print("\n Checking for Null Values.")
    print(df.isnull().sum())
    print(df.shape)
    print(df.dtypes)
    
    #start by dropping player, team, matchID, opp
    df = df.drop(['ID', 'GAME_ID', 'MATCHUP', 'LOCATION', 'GAME_CLOCK', 'PTS', 'SHOT_RESULT','player_name',
                            'CLOSEST_DEFENDER1', 'made', 'time_remaining', 'shot_type', 'player', 'CLOSEST_DEFENDER'], axis=1)
    
    X = df.drop('FGM', axis=1)
    y = df['FGM']
    
    X_num = X.select_dtypes(include='number')
    X_cat = X.select_dtypes(exclude='number')
    X_num = StandardScaler().set_output(transform='pandas').fit_transform(X_num)
    X_cat = pd.get_dummies(X_cat, drop_first=True)
    X = pd.concat([X_num,X_cat],axis=1)
    
    return X, y
