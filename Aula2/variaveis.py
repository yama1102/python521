#!/usr/bin/env python3

import flask

app = flask.Flask(__name__)

# @app.route('/<nome>')
# def index(nome):
#     return f'Estou vivo {nome}'

# @app.route('/user/', defaults={'id':0})
# @app.route('/user/<int:id>')
# @app.route('/user/<username>')
# def id_user(id,username=None):
#     return f'{username}, {id}'

app.run(debug=True)

