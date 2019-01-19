from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sslify import SSLify
from config import config

from worker0_server.main import main as main_blueprint
from worker0_server.auth import auth as auth_blueprint
#from worker0_server.api import api as api_blueprint


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    if app.config.get('SSL_REDIRECT', False):
        sslify = SSLify(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    #app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
