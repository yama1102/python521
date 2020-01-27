#!/usr/bin/env python3

import requests as r
###### Requisições do tipo get
# API de usuários: https://gen-net.herokuapp.com/api/users
# API de endereços: viacep.com.br/ws/01001000/json/

# cep = input('Digite seu cep: ')

# url_api = f'https://viacep.com.br/ws/{cep}/json/'

# res = r.get(url_api)
# print(res.status_code)
# assert res.status_code == 200, 'Não consegui chegar na pagina'
# endereco = res.json()

# for k,v in endereco.items(): # k = key, v = value funcionam para dicionarios
#     print(f'{k} - {v}')

# print(endereco['logradouro'])

# print(type(res.json()))
# print(res.json().keys())

# print(res.__dir__())
# print(dir(res))

# print(res.json())
# usuarios = res.json()
# print(type(usuarios))
# print(len(usuarios))
 
##### Requisições do tipo post

# cadastrar um usuário na API

def cadastra(name:str,email:str,password:str) -> int:
    '''Cadastra usuários na API

    só chamar com nome, email e senha que cadastra :-)
    '''
    dados = {
        'name': name,
        'email': email,
        'password': password
    }
    res = r.post('https://gen-net.herokuapp.com/api/users', data=dados)
    assert res.status_code == 200
    return res.json()['id']



def ler_usuario(id: int) -> dict:  # dict = dictionary
    res = r.get(f'https://gen-net.herokuapp.com/api/users/{id}')
    return res.json()

print(ler_usuario(299))

# print(cadastra('Test2','test2@4linux.com.br','123456'))
