"""
App for bank note authentication

Author: Chaithra Cheluvaiah
Created on: 2024-06-01
"""

from flask import Flask, request
import pickle
import logging

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask(__name__)

# Load the trained model
bank_note_rf_classifier = pickle.load(open('./models/bank_note_rf_model.pkl', 'rb'))

@app.route('/')
def home_page():
    return "Welcome to the Bank Note Authentication API! Use the /predict endpoint to classify bank notes."

@app.route('/predict', methods=['GET'])
def predict():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    logger.info(f"Received input - Variance: {variance}, Skewness: {skewness}, Curtosis: {curtosis}, Entropy: {entropy}")

    prediction = bank_note_rf_classifier.predict([[variance, skewness, curtosis, entropy]])
    logger.info(f"Predicted value :  { 'Fake Note' if prediction[0] == 0 else 'Genuine Note' }")

    if prediction[0] == 0:
        return "The bank note is classified as: Fake Note"
    else:
        return "The bank note is classified as: Genuine Note"


if __name__ == "__main__":
    app.run()