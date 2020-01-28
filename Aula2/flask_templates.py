#!/usr/bin/env python3

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():

    dados = {
        'title': 'Titulo jinja',
        'word': 'Eu sei programar',
        'botao': True
    }
    # return flask.render_template('index.html', title = 'Titulo Jinja', index=dados)
    return flask.render_template('principal.html')

app.run(debug=True)
