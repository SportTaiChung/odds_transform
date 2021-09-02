# coding: utf-8
from flask import Flask
import yaml
from app.main import main
from app.api import api


def create_app():
    app = Flask(__name__)
    app.config.from_file('../config.yml', load=yaml.safe_load)
    app.register_blueprint(main, url_prefix='/') 
    app.register_blueprint(api, url_prefix='/api') 
    return app
