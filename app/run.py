"""
This is the entry point for the Bank Note Authentication API. It creates and runs the Flask application.
Author: Chaithra Cheluvaiah
Created on: 2026-03-13
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])