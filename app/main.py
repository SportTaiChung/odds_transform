# coding: utf-8
from flask import jsonify, Blueprint


main = Blueprint('main', __name__)


@main.route('/')
def hello():
    return jsonify({'service': 'handicap odds transform api'})
