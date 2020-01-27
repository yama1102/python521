#!/user/bin/env python3

import flask
from blueprints.api_routes import api 

app = flask.Flask(__name__)
app.register_blueprint(api)

@app.route('/')
def index():
    return "Bem vindo, forasteiro"

@app.route('/cadastrar',methods=['POST'])
def cadastrar():
    return "<h5>Bem Vindo a Área de cadastro</h5>"


app.run(debug=True,host='0.0.0.0')