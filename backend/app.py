import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
processed_height_path = os.path.join('backend', 'data', 'processed_nba_height.csv')
sample_file = '20001031.csv'

def main():
    # Get and print the summary for the sample
    print(f"Processing sample file: {sample_file}")
    sample_df = load_and_process_nba_data(general_data_path, sample_file=sample_file)
    print("\nFirst few rows:")
    print(sample_df.head(3))
    print("\nSummary stats for sample file:")
    sample_summary = get_dataset_summary(sample_df)
    print_dataset_summary(sample_summary)
    
    
    # # Get and print the summary for the full dataset
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
    height_df = None
    if os.path.exists(processed_height_path):
        print(f"\nLoading processed height data from {processed_height_path}...")
        height_df = pd.read_csv(processed_height_path)
        print("\nSummary stats for loaded height data:")
        height_summary = get_height_dataset_summary(height_df)
        print_dataset_summary(height_summary)
    else:
        height_df = load_and_process_nba_height_data(height2014_data_path)
        print("\nFirst few rows of height data:")
        print(height_df.head(3))
        print("\nSummary stats for NBA Height data:")
        height_summary = get_height_dataset_summary(height_df)
        print_dataset_summary(height_summary)


if __name__ == "__main__":
    main()