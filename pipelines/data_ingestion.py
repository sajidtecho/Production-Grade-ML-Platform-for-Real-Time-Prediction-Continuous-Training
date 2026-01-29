import pandas as pd

def load_raw_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = load_raw_data("data/raw/data.csv")
    print(df.head())
