import flask
import ldap3
from hashlib import md5
from binascii import b2a_base64

ldap_routes = flask.Blueprint(name='ldap',import_name=__name__,url_prefix='/login')

@ldap_routes.route('/')
def index():
    return flask.render_template('login.html')

@ldap_routes.route('/',methods=['POST'])
def login():
    email = flask.request.form['email']
    password = flask.request.form['password']
    username = 'admin'

    try:
        server = ldap3.Server('ldap://localhost:389')
        client = ldap3.Connection(server,f'cn={username},dc=example,dc=org',password='admin')
        client.bind()

        dn = f'uid={email},dc=example,dc=org'

        client.search(dn,'(objectclass=person)',attributes=['cn','sn','userPassword'])

        resultado = {
            'nome' : client.entries[0].cn.value,
            'sobrenome': client.entries[0].sn.value
        }

        pass_md5 = md5(password.encode('utf-8')).digest()
        pass_md5 = '{MD5}' + b2a_base64(pass_md5).decode('utf-8')

        if(pass_md5 == client.entries[0].userPassword.value.decode('utf-8')):
            flask.session['logged'] = True
            return flask.redirect(flask.url_for('index'))
        else:
            raise Exception('Usuário não encontrado')
    except Exception as e:
        return flask.redirect(flask.url_for('ldap.index'))