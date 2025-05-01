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
    
import pandas as pd
import os
import re
from datetime import datetime

def load_and_process_nba_data(data_path, sample_file=None):
    """
    Load and process NBA shot data from CSV files.
    
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
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Drop the first empty column and unnamed columns
        columns_to_drop = [col for col in df.columns if col == '' or col.startswith('Unnamed')]
        df = df.drop(columns=columns_to_drop)
        
        # Convert data types
        df['shotX'] = df['shotX'].astype(float)
        df['shotY'] = df['shotY'].astype(float)
        df['distance'] = df['distance'].astype(float)
        
        # Convert 'made' to boolean if it's not already
        if df['made'].dtype != bool:
            df['made'] = df['made'].astype(bool)
        
        # Process the score column
        df['score'] = df['score'].apply(process_score)
        
        # Add a date column based on the filename (YYYYMMDD format)
        date_str = os.path.splitext(file)[0]  # Remove file extension
        try:
            date = datetime.strptime(date_str, '%Y%m%d')
            df['date'] = date
        except ValueError:
            # If the filename is not in the expected format, use NaT
            df['date'] = pd.NaT
        
        dfs.append(df)
    
    # Combine all dataframes
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

def get_dataset_summary(df):
    """
    Generate a summary of the dataset for the assignment.
    
    Args:
        df (pd.DataFrame): The processed NBA shot data.
        
    Returns:
        dict: A dictionary containing dataset summary statistics.
    """
    summary = {}
    summary['total_examples'] = len(df)
    summary['problem_type'] = 'Regression'
    summary['target'] = 'Shot probability (0.0-1.0)'
    
    
    made_shots = df['made'].sum()
    missed_shots = len(df) - made_shots
    summary['made_shots'] = int(made_shots)
    summary['missed_shots'] = int(missed_shots)
    summary['made_percentage'] = round(made_shots / len(df) * 100, 2) if len(df) > 0 else 0
    
    if len(df) > 0:
        summary['target_distribution'] = {
            'min': 0.0,
            'max': 1.0,
            'mean': summary['made_percentage'] / 100,
        }

    summary['shot_types'] = df['shot_type'].value_counts().to_dict()
    summary['teams'] = df['team'].nunique()
    summary['players'] = df['player'].nunique()
    
    
    if 'date' in df.columns and not df['date'].isna().all():
        summary['start_date'] = df['date'].min().strftime('%Y-%m-%d')
        summary['end_date'] = df['date'].max().strftime('%Y-%m-%d')
    
    return summary


def print_dataset_summary(summary):
    """
    Print a formatted summary of the dataset.
    
    Args:
        summary (dict): The dataset summary dictionary.
    """
    print("\n=== NBA SHOT DATASET SUMMARY ===")
    print(f"Total examples: {summary['total_examples']:,}")
    print(f"Problem type: {summary['problem_type']} (predicting {summary['target']})")
    print(f"Target distribution:")
    print(f"  - Made shots: {summary['made_shots']:,} ({summary['made_percentage']}%)")
    print(f"  - Missed shots: {summary['missed_shots']:,} ({100 - summary['made_percentage']:.2f}%)")
    
    if 'target_distribution' in summary:
        td = summary['target_distribution']
        print(f"Target probability range: {td['min']:.1f} to {td['max']:.1f} (mean: {td['mean']:.3f})")
    
    if 'shot_types' in summary:
        print("\nShot types distribution:")
        for shot_type, count in summary['shot_types'].items():
            print(f"  - {shot_type}: {count:,}")
    
    print(f"\nUnique teams: {summary.get('teams', 'N/A')}")
    print(f"Unique players: {summary.get('players', 'N/A')}")
    
    if 'start_date' in summary and 'end_date' in summary:
        print(f"\nDate range: {summary['start_date']} to {summary['end_date']}")