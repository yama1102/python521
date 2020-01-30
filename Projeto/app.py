#!/usr/bin/env python3

import flask

from blueprints.docker_blueprints import docker_routes
from blueprints.jenkins_blueprints import jenkins_routes

app = flask.Flask(__name__)
app.register_blueprint(docker_routes)
app.register_blueprint(jenkins_routes)

@app.route('/')
def index():
    return flask.render_template('index.html')

app.run(debug=True)
