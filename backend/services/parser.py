import pandas as pd

def parse_csv(path):
    df = pd.read_csv(path)
    return df.to_dict(orient="records")