"""App initialization and factory function. 
Creating the Flask app via a factory function allows for better modularity and 
testing is easy (you can create an app with test config).

Author: Chaithra Cheluvaiah
Created on: 2026-03-12
"""

import logging
from flask import Flask
from .config import Config
from .routes import register_routes

def create_app(config: Config | None = None) -> Flask:
    app = Flask(__name__)

    # config
    app.config.from_object(config or Config())

    #logging
    logging.basicConfig(level=app.config['LOG_LEVEL'])
    logging.getLogger(__name__).info("App created with configuration: %s", app.config)

    # routes / blueprints
    register_routes(app)

    return app