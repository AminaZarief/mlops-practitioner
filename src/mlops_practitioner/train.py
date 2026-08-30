from mlops_practitioner.config import model_path

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression

import pickle



def train(train_df, val_df, features):

    train_dicts = train_df[features].to_dict(orient='records')
    val_dicts = val_df[features].to_dict(orient='records')

    # Vectorize categorical and numerical features
    dv = DictVectorizer()
    X_train = dv.fit_transform(train_dicts)
    X_val = dv.transform(val_dicts)

    y_train = train_df['duration'].values
    y_val = val_df['duration'].values

    model = LinearRegression()
    model.fit(X_train, y_train)

    with open(model_path, 'wb') as f_out:
        pickle.dump((dv, model), f_out)

    print(f'Fitted model saved to {model_path}')

    return X_val, y_val
