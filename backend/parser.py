# parser.py

import pandas as pd

def parse_file(file_path):

    # simple CSV parser
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)

    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)

    else:
        # fallback dummy
        return [
            {"date": "2025-01-01", "sales": 1000, "profit": 200},
            {"date": "2025-01-02", "sales": 1200, "profit": 250}
        ]

    return df.to_dict(orient="records")
