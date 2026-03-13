import os

class Config:
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    MODEL_PATH = os.getenv('MODEL_PATH', 'models/bank_note_rf_model.pkl')
    HOST = '0.0.0.0'
    PORT = 5001