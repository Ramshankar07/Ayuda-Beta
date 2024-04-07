from flask import Flask
from .database.db import get_mongodb

def create_app():
    app = Flask(__name__)
    # configure app here with app.config settings

    # Initialize MongoDB
    mongo = get_mongodb(app)

    # Store the mongo instance in app for global access, if necessary
    app.mongo = mongo

    # Importing API modules
    from app.api import user_api, auth_api

    # Register Blueprints or add routes from your API
    app.register_blueprint(user_api.blueprint)
    app.register_blueprint(auth_api.blueprint)

    return app
