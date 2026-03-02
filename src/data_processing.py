# src/data_processing.py

import pandas as pd

def load_data(path="../data/salaries.csv"):
    df = pd.read_csv(path)
    return df

def preprocess_data(df):
    # Keep only relevant columns
    df = df[['experience_level','employment_type','job_title','remote_ratio','company_location','salary']]
    
    # Drop missing values if any
    df = df.dropna()
    
    # Convert categorical columns to string (optional)
    categorical_cols = ['experience_level','employment_type','job_title','company_location']
    for col in categorical_cols:
        df[col] = df[col].astype(str)
    
    return df

if __name__ == "__main__":
    df = load_data()
    df = preprocess_data(df)
    print(df.head())