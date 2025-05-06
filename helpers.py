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
    
def load_and_process_nba_height_data(data_path, file_name='NBA_Height.csv'):
    """
    Load and process NBA height data from CSV file.
    
    Args:
        data_path (str): Path to the directory containing the CSV file.
        file_name (str): Name of the CSV file.
        
    Returns:
        pd.DataFrame: Processed DataFrame with NBA height data.
    """
    file_path = os.path.join(data_path, file_name)
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return pd.DataFrame()
    
    
    df = pd.read_csv(file_path)
    
   
    df['SHOT_DIST'] = df['SHOT_DIST'].astype(float)
    df['TOUCH_TIME'] = df['TOUCH_TIME'].astype(float)
    df['DRIBBLES'] = df['DRIBBLES'].astype(int)
    df['CLOSE_DEF_DIST'] = df['CLOSE_DEF_DIST'].astype(float)
    df['SHOOTER_height'] = df['SHOOTER_height'].astype(float)
    df['DEFENDER_height'] = df['DEFENDER_height'].astype(float)
    
    df['FGM'] = df['FGM'].astype(bool)    
    df['made'] = df['SHOT_RESULT'].apply(lambda x: True if x.lower() == 'made' else False)
    
    # Example: "12/30/1899 12:23:45 AM" -> "12:23:45"
    df['time_remaining'] = df['GAME_CLOCK'].str.extract(r'(\d+:\d+:\d+)')
    df['quarter'] = df['PERIOD'].astype(str)
    
    
    bins = [0, 3, 10, 16, 23, 100]
    labels = ['0-3 ft', '3-10 ft', '10-16 ft', '16-23 ft', '23+ ft']
    df['distance_bin'] = pd.cut(df['SHOT_DIST'], bins=bins, labels=labels)
    
    def_bins = [0, 2, 4, 6, 100]
    def_labels = ['Tight (0-2 ft)', 'Close (2-4 ft)', 'Open (4-6 ft)', 'Wide Open (6+ ft)']
    df['defender_distance_bin'] = pd.cut(df['CLOSE_DEF_DIST'], bins=def_bins, labels=def_labels)
    
    df['height_diff'] = df['SHOOTER_height'] - df['DEFENDER_height']
    # (e.g., "GSW vs. MIA" -> "GSW", "MIA")
    df[['team', 'opp']] = df['MATCHUP'].str.extract(r'([A-Z]{3}) [vV][sS][.] ([A-Z]{3})')
    df['shot_type'] = df['PTS_TYPE'].apply(lambda x: '3PT Field Goal' if x == 3 else '2PT Field Goal')
    df['player'] = df['player_name']
    
    
    return df
    
    

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
    
    if df['date'].dtype == 'object':
        try:
            summary['start_date'] = pd.to_datetime(df['date'].min()).strftime('%Y-%m-%d')
            summary['end_date'] = pd.to_datetime(df['date'].max()).strftime('%Y-%m-%d')
        except Exception as e:
            print(f"Warning: Could not format date range - {e}")
            summary['start_date'] = str(df['date'].min())
            summary['end_date'] = str(df['date'].max())
    else:
        summary['start_date'] = df['date'].min().strftime('%Y-%m-%d')
        summary['end_date'] = df['date'].max().strftime('%Y-%m-%d')
    
    return summary

def get_height_dataset_summary(df):
    """
    Generate a summary of the NBA height dataset for the assignment.
    
    Args:
        df (pd.DataFrame): The processed NBA height data.
        
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
    
    # Defender distance stats
    summary['defender_distance'] = {
        'min': df['CLOSE_DEF_DIST'].min(),
        'max': df['CLOSE_DEF_DIST'].max(),
        'mean': df['CLOSE_DEF_DIST'].mean(),
        'median': df['CLOSE_DEF_DIST'].median()
    }
    
    # Height stats
    summary['shooter_height'] = {
        'min': df['SHOOTER_height'].min(),
        'max': df['SHOOTER_height'].max(),
        'mean': df['SHOOTER_height'].mean(),
        'median': df['SHOOTER_height'].median()
    }
    
    summary['defender_height'] = {
        'min': df['DEFENDER_height'].min(),
        'max': df['DEFENDER_height'].max(),
        'mean': df['DEFENDER_height'].mean(),
        'median': df['DEFENDER_height'].median()
    }
    
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
        
    if 'defender_distance' in summary:
        dd = summary['defender_distance']
        print("\nDefender distance (feet):")
        print(f"  - Range: {dd['min']:.1f} to {dd['max']:.1f}")
        print(f"  - Mean: {dd['mean']:.2f}")
        print(f"  - Median: {dd['median']:.2f}")
    
    if 'shooter_height' in summary:
        sh = summary['shooter_height']
        print("\nShooter height (inches):")
        print(f"  - Range: {sh['min']:.1f} to {sh['max']:.1f}")
        print(f"  - Mean: {sh['mean']:.2f}")
        print(f"  - Median: {sh['median']:.2f}")
        
        
def analyze_shot_distance(df):
    """Analyze how shot success probability changes with distance"""
    print("\nAnalyzing shot success rate by distance...")