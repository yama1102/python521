import flask

api = flask.Blueprint("api",__name__,url_prefix="/api")

@api.route('/') # api/users foi retirado
def index():
    dados = {
        "nome": "Tsubasa",
        "sobrenome": "Yamauchi"
    }
    return flask.jsonify(dados)

@api.route('\users')
def users():
    return'Listagem de usuários aki'