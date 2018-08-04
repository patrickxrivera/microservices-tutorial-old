import os

from flask import Flask  # new
from flask_sqlalchemy import SQLAlchemy
import psycopg2

# instantiate the db
db = SQLAlchemy()

# new
def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@users-db:5432/users_dev'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # psycopg2.connect(database='users-db', user='postgres', password='postgres')

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
