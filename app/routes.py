"""
This module defines the routes for the Bank Note Authentication API. 
It includes endpoints for predicting the authenticity of bank notes based on input features, 
as well as an endpoint for batch predictions using a CSV file.

Author: Chaithra Cheluvaiah
Created on: 2026-03-13
"""
from fastapi import Depends, FastAPI, status, UploadFile, File
from fastapi.responses import JSONResponse
from .model import BankNoteAuthenticationModel
from .schemas import BankNoteFeatures
import pandas as pd

def register_routes(app: FastAPI):
    bank_note_auth_model = BankNoteAuthenticationModel(app.state.config.MODEL_PATH)

    @app.get('/')
    async def home():
        welcome_message = ("Welcome to the Bank Note Authentication API! "
                   "Use the /predict endpoint to classify bank notes. "
                   "Example: /predict?variance=2.3&skewness=1.5&curtosis=0.5&entropy=-1.2 "
                   "Or you can POST a CSV file to /predict_file with the same columns (variance, skewness, curtosis, entropy).")
        return JSONResponse(content={ "message": welcome_message }, status_code=status.HTTP_200_OK)
    
    @app.get('/predict')
    async def predict(bank_note_features: BankNoteFeatures = Depends()):
        """Predict the authenticity of a bank note based on input features."""

        # input validation is handled by Pydantic via the BankNoteFeatures schema
        values = [
                bank_note_features.variance,
                bank_note_features.skewness,
                bank_note_features.curtosis,
                bank_note_features.entropy
            ]
        result = bank_note_auth_model.predict_from_list(values)
        return JSONResponse(content={ "prediction": result }, status_code=status.HTTP_200_OK)

    @app.post('/predict_file')
    async def predict_file(input_csv: UploadFile = File(...)):
        if input_csv.content_type != 'text/csv':
            return JSONResponse(content={ "error": "Invalid file type. Please upload a CSV file." }, status_code=status.HTTP_400_BAD_REQUEST)
        
        input_df = pd.read_csv(input_csv.file)

        # enforce expected columns
        expected_columns = {'variance', 'skewness', 'curtosis', 'entropy'}
        if set(input_df.columns) != expected_columns:
            return JSONResponse(content={ "error": f"Invalid CSV format. Expected columns: {expected_columns}" }, status_code=status.HTTP_400_BAD_REQUEST)
        
        records = input_df.to_dict(orient='records')
        validated = [BankNoteFeatures(**record) for record in records]  # this will raise validation errors if any record is invalid
        if not validated:
            return JSONResponse(content={ "error": "One or more records in the CSV are invalid." }, status_code=status.HTTP_400_BAD_REQUEST)
        
        predictions = bank_note_auth_model.predict_from_dataframe(input_df)
        return JSONResponse(content={ "predictions": predictions }, status_code=status.HTTP_200_OK)