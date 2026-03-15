"""App initialization and factory function. 
Creating the Flask app via a factory function allows for better modularity and 
testing is easy (you can create an app with test config).

Author: Chaithra Cheluvaiah
Created on: 2026-03-12
"""

import logging
from .config import Config
from .routes import register_routes
from fastapi import FastAPI

def create_app(config: Config | None = None) -> FastAPI:
    
    # Create FastAPI app instance
    bank_note_app = FastAPI(
        title="Bank Note Authentication API",
        description="API for classifying bank notes as genuine or fake based on features like variance, skewness, curtosis, and entropy.",
        version="1.0.0"
    )

    # config
    bank_note_app.state.config = config or Config()

    #logging
    logging.basicConfig(level=bank_note_app.state.config.LOG_LEVEL)
    logging.getLogger(__name__).info("App created with configuration: %s", bank_note_app.state.config)

    # routes / blueprints
    register_routes(bank_note_app)

    return bank_note_app