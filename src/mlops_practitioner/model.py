import pickle

from mlops_practitioner.decorator import timed


class DurationPredictor:
    def __init__(self):
        self._dv, self._model = None, None 
        self._loaded = False

    def load(self, model_path: str) -> None:
        with open(model_path,'rb') as f:
            self._dv,self._model = pickle.load(f)
        self._loaded = True
        
    @timed
    def predict_one(self, features: dict) -> float:
        if not self._loaded:
            raise RuntimeError("Model not loaded. Call .load() first.")
            
        X = self._dv.transform([features])
        prediction = self._model.predict(X)
        return float(prediction[0])
        
    @timed       
    def predict_batch(self, features: list[dict]) -> list[float]:
        if not self._loaded:
            raise RuntimeError("Model not loaded. Call .load() first.")
            
        X = self._dv.transform(features)
        return self._model.predict(X).tolist()
        
        #return [self.predict_one(i) for i in features]
    
