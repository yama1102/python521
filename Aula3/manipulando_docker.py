#!/usr/bin/env python3

import docker
# client = docker.Docker('tcp://localhost:2376') #Só para conexão remota 
try:
    client = docker.from_env() #conexão local
except Exception:
    exit(1)

# print(client.containers.run('python','python3 --help'))

#Listar todos os containers
# for container in client.containers.list():
#     print(container.name)
#     print(container.status)
#     print(container.image)

# print(client.containers.run('ubuntu','bash', detach=True))

# print(client.containers.list())

container_ubuntu = client.containers.get('e612267709')

print(dir(container_ubuntu))

try:
    container_ubuntu.stop()
    print('Container parado com sucesso!')
except Exception as e:
    print(e)
    