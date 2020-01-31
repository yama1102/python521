#!/usr/bin/env python3

import requests
import json

private_token = "5A7zAHPKwaqjEygc-ore"
url = 'http://192.168.200.172/api/v4/'

payload = {"private_token": private_token}

#Listagem dos projetos
projetos = requests.get(url + 'projects',params=payload)

# print(projetos.url)
# print(json.dumps(projetos.json(), indent=4))

# Adicionar um projeto

payload = {
    'name':'flask-app'
}

projeto = requests.post(url + 'projects?private_token=' + private_token, payload)
print(json.dumps(projeto.json(),indent=4))

#Listando usuários
payload = {"private_token": private_token}
usuarios = requests.get(url + 'users',params =payload)
print(json.dumps(usuarios.json(),indent=4))

#Adicionando usuário

new_user = {
    'email': 'tsubasa@4linux.com.br',
    'username': 'tsubasa4linux',
    'name': 'Tsubasa 4linux',
    'password': '4linuxTsubasa'
}
# usuario = requests.post(url +'user?private_token=' + private_token, new_user)
# print(json.dumps(usuarios.json(),indent=4))
