import pandas as pd

def load(filename, column):
    df = pd.read_csv(filename)
    data = df[column].tolist()
    return data