import numpy as np
import pandas as pd
from sklearn.externals import joblib
import os
import warnings

warnings.filterwarnings("ignore")

def predict_heart_disease(model_dir, input_data):
    print("Loading model.")
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    print("Done loading model.")
    data = pd.DataFrame.from_dict(input_data)
    output = model.predict(data)
    return output

#input_data = {'age': [63], 'gender': [1], 'chest pain': [3], 'blood pressure': [145], 'cholestrol level': [233], 'max heart rate': [150]}
#input_data = pd.DataFrame.from_dict(input_data)
#predict_heart_disease('/Users/muntazir/Desktop/colg/ai/model/', input_data)