from mlops_practitioner.model import DurationPredictor
from mlops_practitioner.config import model_path

p = DurationPredictor()
p.load(model_path)
p.predict_one({'PU_DO': '1_1', 'trip_distance':2.0})