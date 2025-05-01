import pandas as pd
import os
import re
from datetime import datetime

def load_and_process_nba_data(data_path, sample_file = None):
    """
    Load and process NBA shot data from CSV files. This is for the 2001-2022 dataset
    Args:
        data_path (str): Path to the directory containing the CSV files.
        sample_file (str, optional): If provided, only process this specific file.
    Returns:
        pd.DataFrame: Processed DataFrame with all NBA shot data.
    """
    # Get all CSV files in the directory if no sample file is provided
    if sample_file:
        files = [sample_file]
    else:
        files = [f for f in os.listdir(data_path) if f.endswith('.csv')]
        
    dfs = []
    
    for file in files:
        file_path = os.path.join(data_path, file)
        df = pd.read_csv(file_path)
        columns_to_drop = [col for col in df.columns if col == '' or col.startswith('Unnamed')]
        df = df.drop(columns=columns_to_drop)
        
        # * FLOAT TYPES
        df['shotX'] = df['shotX'].astype(float)
        df['shotY'] = df['shotY'].astype(float)
        df['distance'] = df['distance'].astype(float)
        
        # * BOOLEAN TYPES 
        if df['made'].dtype != bool:
            df['made'] = df['made'].astype(bool)
        
        # Process the score column
        df['score'] = df['score'].apply(process_score)
        
        
        # Add a date column based on the filename (YYYYMMDD format)
        date_str = os.path.splitext(file)[0]
        try:
            date = datetime.strptime(date_str, '%Y%m%d')
            df['date'] = date
        except ValueError:
            # If the filename is not in the expected format, use NaT
            df['date'] = pd.NaT
        
        dfs.append(df)
        
    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        return combined_df
    else:
        return pd.DataFrame()


def process_score(score):
    """
    Process the score column to ensure it follows the format 'score-score'.
    If it doesn't, replace with '-1-0'.

    Args:
        score (str): The score string to process.
        
    Returns:
        str: Processed score string.
    """
    
    if not isinstance(score, str):
        return '-1-0'
    
    # Check if the score follows the pattern 'number-number'
    if re.match(r'^\d+-\d+$', score):
        return score
    else:
        return '-1-0'