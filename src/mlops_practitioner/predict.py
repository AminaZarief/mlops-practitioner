import pickle

import numpy as np

from mlops_practitioner.config import model_path


def predict(input_data:list[dict]) -> np.ndarray:
    with open(model_path,'rb') as f:
        model, dv = pickle.load(f)

    input_data= dv.transform(input_data)
    y_pred = model.predict(input_data)

    return y_pred
