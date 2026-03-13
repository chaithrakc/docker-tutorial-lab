"""
This module defines the routes for the Bank Note Authentication API. 
It includes endpoints for predicting the authenticity of bank notes based on input features, 
as well as an endpoint for batch predictions using a CSV file.

Author: Chaithra Cheluvaiah
Created on: 2026-03-13
"""

from flask import Flask, jsonify, request
from .model import BankNoteAuthenticationModel
import pandas as pd

def register_routes(app: Flask):
    bank_note_auth_obj = BankNoteAuthenticationModel(app.config['MODEL_PATH'])

    @app.route('/')
    def home():
        return jsonify({
            "message": "Welcome to the Bank Note Authentication API! "
            "Use the /predict endpoint to classify bank notes."
            "Example: /predict?variance=2.3&skewness=1.5&curtosis=0.5&entropy=-1.2"
            "Or you can POST a CSV file to /predict_file with the same columns (variance, skewness, curtosis, entropy)."
        }), 200
    
    @app.route('/predict', methods=['GET'])
    def predict():
        try:
            values = [float(request.args.get(param)) for param in ['variance', 'skewness', 'curtosis', 'entropy']]
        except KeyError as e:
            app.logger.error(f"Missing query parameter: {e}")
            return jsonify({"error": f"Missing query parameter: {e.args[0]}"}), 400
        except ValueError as e:
            app.logger.error(f"Invalid query parameter value: {e}")
            return jsonify({"error": f"All inputs must be numeric"}), 400
        

        result = bank_note_auth_obj.predict_from_list(values)
        return jsonify({"prediction": result}), 200
    
    @app.route('/predict_file', methods=['POST'])
    def predict_file():
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded in the request"}), 400
        
        val_df = pd.read_csv(request.files.get("file"))
        predictions = bank_note_auth_obj.predict_from_dataframe(val_df)
        return jsonify({"predictions": predictions}), 200