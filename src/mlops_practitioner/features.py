import pandas as pd


def add_features(df: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:

    # Calculate duration in minutes
    df['duration'] = (df['lpep_dropoff_datetime'] - df['lpep_pickup_datetime']).dt.total_seconds() / 60.0

    # Filter outlier durations (keep trips between 1 and 60 minutes)
    df = df[(df['duration'] >= 1) & (df['duration'] <= 60)].copy()

    # 3. Engineer features: PU_DO (pickup-dropoff pair) and trip_distance
    df['PU_DO'] = df['PULocationID'].astype(str) + '_' + df['DOLocationID'].astype(str)
    features = ['PU_DO', 'trip_distance']

    return df, features

