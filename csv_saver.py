import pandas as pd

def save(filename, column, data):
    df = pd.DataFrame(data, columns=[column]) 
    df.to_csv(filename, index=False)
    return df