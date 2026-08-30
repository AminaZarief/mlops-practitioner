from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from mlops_practitioner.config import model_path
import pickle
def predict(input_data):
    with open(model_path,'rb') as f:
        model, dv = pickle.load(f)

    input_data= dv.transform(input_data)
    y_pred = model.predict(input_data)

    return y_pred
