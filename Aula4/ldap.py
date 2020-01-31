import os

import ldap3
import dotenv
import hashlib
import binascii

dotenv.load_dotenv()

username = os.getenv('LDAP_USER')
password = os.getenv('LDAP_PASSWORD')
server = os.getenv('LDAP_SERVER')

server = ldap3.Server(server)

client = ldap3.Connection(server,f'cn={username},dc=example,dc=org',password=password)

client.bind()
# print(client)

#Inserindo um usuário
md5json = hashlib.md5('senhaSuperSegura'.encode('utf-8')).digest()

# print(md5json)

user = {
    'cn':'sys',
    'sn':'admin',
    'mail':'sys.admin@4linux.com.br',
    'uidNumber':'1000',
    'gidNumber':'1000',
    'uid':'sys.admin',
    'homeDirectory':'/home/sys',
    'userPassword':'{MD5}' + binascii.b2a_base64(md5json).decode('utf-8')
}

object_class = ['top','person','organizationalPerson','inetOrgPerson','posixAccount']

cn = f'uid={user["mail"]},dc=example,dc=org'

print(client.add(cn,object_class,user))

#Buscando um usuário

email = 'sys.admin@4linux.com.br'
dn = f'uid={user["mail"]},dc=example,dc=org'

client.search(dn,'(objectclass=person)',attributes=['cn','sn'])

print(client.entries)

#alterar um usuarios

changes = {
    'cn': [(ldap3.MODIFY_REPLACE,['sys'])],
    'sn': [(ldap3.MODIFY_REPLACE,['admin'])]
}

client.modify(dn,changes)
print(client.result)

client.search(dn,'(objectclass=person)',attributes=['cn','sn'])
print(client.entries)

#deletar
# print(client.delete(dn))