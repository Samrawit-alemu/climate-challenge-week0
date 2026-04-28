import pandas as pd
import os

def load_data():
    countries = ['ethiopia', 'kenya', 'nigeria', 'sudan', 'tanzania']
    all_dfs = []
    
    for c in countries:
        # We look for files in the data folder relative to the root
        path = f"data/{c}_clean.csv"
        if os.path.exists(path):
            df = pd.read_csv(path)
            df['Country'] = c.capitalize()
            df['Date'] = pd.to_datetime(df['Date'])
            all_dfs.append(df)
    
    return pd.concat(all_dfs, ignore_index=True)