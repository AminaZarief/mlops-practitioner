from mlops_practitioner.data import get_data
from mlops_practitioner.train import train


def run()-> None:
    train_df, val_df, features = get_data()
    _X_val, _y_val = train(train_df, val_df, features)


if __name__ == '__main__':
   run()
