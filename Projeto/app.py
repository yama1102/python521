#!/usr/bin/env python3

import flask

from blueprints.docker_blueprints import docker_routes
from blueprints.jenkins_blueprints import jenkins_routes
from blueprints.ldap_blueprints import ldap_routes
from blueprints.gitlab_blueprints import gitlab_routes

app = flask.Flask(__name__)
app.secret_key = 'chave'

app.register_blueprint(docker_routes)
app.register_blueprint(jenkins_routes)
app.register_blueprint(ldap_routes)
app.register_blueprint(gitlab_routes)

@app.route('/')
def index():
    if 'logged' in flask.session and flask.session['logged']:
        session = True
    else:
        session = False
    return flask.render_template('index.html',flask = session)
app.run(debug=True)
