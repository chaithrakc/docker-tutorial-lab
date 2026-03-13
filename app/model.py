"""
This module defines the BankNoteAuthenticationModel class which loads a pre-trained machine learning model 
and provides methods for making predictions based on input data. The model is used to classify bank notes 
as genuine or fake based on features such as variance, skewness, curtosis, and entropy.

The class includes:
- __init__: Initializes the model by loading it from the specified path.
- _load_model: A helper method to load the model using joblib.
- predict_from_list: Takes a list of feature values and returns a prediction.
- predict_from_dataframe: Takes a pandas DataFrame and returns a list of predictions for each row.

The model is expected to be a binary classifier where a prediction of 1 indicates a genuine note and 0 indicates a fake note.

Author: Chaithra Cheluvaiah
Created on: 2026-03-13
"""
import joblib
import pandas as pd
from pathlib import Path

class BankNoteAuthenticationModel:
    def __init__(self, model_path:str):
        self.model_path = Path(model_path)
        self.model = self._load_model()

    def _load_model(self):
        with open(self.model_path, 'rb') as file:
            return joblib.load(file)

    def predict_from_list(self, values:list):
        pred = self.model.predict([values])[0]
        return "Genuine Note" if pred == 1 else "Fake Note"

    def predict_from_dataframe(self, df:pd.DataFrame):
        preds = self.model.predict(df)
        return ["Genuine Note" if pred == 1 else "Fake Note" for pred in preds]