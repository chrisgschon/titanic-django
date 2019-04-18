import dill as pickle
import pandas as pd

def classify_passenger(model, data):
    df = pd.read_json(data)
    pred = model.predict(df)
    return(pred)

def load_model(path):
    with open(path,'rb') as f:
        model = pickle.load(f)
    return(model)

