import pandas as pd

def merge_parts(dfs):
    """
    Merge multiple part DataFrames into one ward DataFrame.
    """
    if not dfs:
        return pd.DataFrame()
    return pd.concat(dfs, ignore_index=True)
