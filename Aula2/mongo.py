#!/usr/bin/env python3

from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['app']
except Exception as e:
    print(e)

# usuario = db.usuarios.insert_one(
#     {
#         'nome':'Paulo',
#         'sobrenome':'Souza'
#     }
# )

# print(db.usuarios.find_one(parametros do objeto)){"nome" : "daniel"}
# lista_de_usuarios = [x for x in db.usuarios.find()]
# print(lista_de_usuarios)

# for item in db.usuarios.find():
#     print(item["nome"])

# user = db.usuarios.update_one(
#     {
#         "name":"Daniel",
#         "sobrenome":"Silva"
#     },
#     {
#         "$set":{
#             "nome":"Júlio"
#         }
#     }
# )

# assert user.modified_count == 1, "Não foram modificados registros"
# print(user.matched_count, user.modified_count)

deleted = db.usuarios.delete_one(
    {
        "nome":"Paulo"
    }
)

assert deleted.deleted_count == 1, "Não encontrou registros"