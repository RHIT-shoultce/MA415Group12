import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from helpers import (
    load_and_process_nba_data, 
    load_and_process_nba_height_data,
    get_dataset_summary, 
    get_height_dataset_summary,
    print_dataset_summary
)
    
general_data_path = os.path.join('backend', 'data', '2001-2022_data', 'nba')
height2014_data_path = os.path.join('backend', 'data', '2014-2015_original')
processed_path = os.path.join('backend', 'data', 'processed_nba_shots.csv')
sample_file = '20001031.csv'

def main():
    # Get and print the summary for the sample
    
    # print(f"Processing sample file: {sample_file}")
    # sample_df = load_and_process_nba_data(general_data_path, sample_file=sample_file)
    # print("\nFirst few rows:")
    # print(sample_df.head(3))
    # print("\nSummary stats for sample file:")
    # sample_summary = get_dataset_summary(sample_df)
    # print_dataset_summary(sample_summary)
    
    
    # Get and print the summary for the full dataset
    # full_summary = None;
    # if(os.path.exists(processed_path)):
    #     print(f"\nLoading processed data from {processed_path}...")
    #     full_df = pd.read_csv(processed_path)
    #     full_summary = get_dataset_summary(full_df)
    # else: 
    #     print("\n\nProcessing all CSV files...")
    #     full_df = load_and_process_nba_data(general_data_path)
    #     print("\nSummary stats for full dataset:")
    #     full_summary = get_dataset_summary(full_df)
    #     print_dataset_summary(full_summary)
    #     output_file = os.path.join('backend', 'data', 'processed_nba_shots.csv')
    #     full_df.to_csv(output_file, index=False)
    #     print(f"\nProcessed data saved to {output_file}")
        
    print("\n\nProcessing NBA_Height.csv file...")
    height_df = load_and_process_nba_height_data(height2014_data_path)
    full_df = height_df
    
    print(full_df.head(3))
    full_df = full_df.drop(['team', 'opp'], axis=1)
    full_df = full_df.dropna()
    
    print("\n Checking for Null Values.")
    print(full_df.isnull().sum())
    print(full_df.shape)
    print(full_df.dtypes)
    
    #start by dropping player, team, matchID, opp
    full_df = full_df.drop(['ID', 'GAME_ID', 'MATCHUP', 'LOCATION', 'GAME_CLOCK', 'PTS', 'SHOT_RESULT','player_name',
                            'CLOSEST_DEFENDER1', 'made', 'time_remaining', 'shot_type', 'player', 'CLOSEST_DEFENDER'], axis=1)
    
    print(full_df.dtypes)
    X = full_df.drop('FGM', axis=1)
    y = full_df['FGM']
    
    X_num = X.select_dtypes(include='number')
    X_cat = X.select_dtypes(exclude='number')
    X_num = StandardScaler().set_output(transform='pandas').fit_transform(X_num)
    X_cat = pd.get_dummies(X_cat, drop_first=True)
    X = pd.concat([X_num,X_cat],axis=1)
    print(X.head(3))   
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.8, test_size=.2, random_state=0)
    
    knn = KNeighborsClassifier(n_neighbors=20)
    knn.fit(X_train, y_train)
    
    print(knn.score(X_test, y_test))
    
    


if __name__ == "__main__":
    main()