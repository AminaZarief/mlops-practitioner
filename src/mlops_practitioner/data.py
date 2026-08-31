import pandas as pd
from sklearn.model_selection import train_test_split

from mlops_practitioner.config import parquet_path
from mlops_practitioner.features import add_features


def get_data() -> tuple[pd.DataFrame, pd.DataFrame,list[str]]:

    df = pd.read_parquet(parquet_path)
    df, features = add_features(df)
    train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

    return train_df, val_df, features

