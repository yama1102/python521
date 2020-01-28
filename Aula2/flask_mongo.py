#!/usr/bin/env python3

import flask
import pymongo
from bson.json_util import dumps

app = flask.Flask(__name__)
client = pymongo.MongoClient()
db = client.app

@app.route('/')
def index():
    users = db.usuarios.find()
    return flask.Response(dumps(users), status=200, content_type= "application/json")

@app.route('/nome/<nome>')
def get_nome(nome):
    user = db.usuarios.find_one(
        {
            "nome":nome
        }
    )
    return flask.Response(dumps(user), status=200, content_type= "application/json")

# @app.route('/delete/<nome>')
# def delete_nome(nome):
#     deleted = db.usuarios.delete_one(
#         {
#             "nome":nome
#         }        
#     )
#     if deleted.deleted_count == 0:
#         return "Não encontrou registros"
#     else:
#         return f"{nome} deleted"  # tem risco que mostrar essa mensagem mesmo que tem outros tipos de erro

@app.route('/delete/<username>')
def delete_user(username):
    try:
        deleted_user = db.usuarios.delete_one(
        {
            "nome": username
        }        
        )
        assert deleted_user.deleted_count == 1, 'usuário não encontrado'
        return flask.jsonify(
            {
                "status" : f'Usuário {username} deletado com sucesso'
            }
        )
    except pymongo.errors.ConnectionFailure:
        return 'Reveja os dados de conexão com o banco'


app.run(debug=True)
