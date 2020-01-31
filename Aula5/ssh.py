import paramiko

client = paramiko.client.SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

## Configurar o servidor de ssh para liberar tty /ect/ssh/sshd_config
try:
    client.connect('127.0.0.1',username='developer',password='4linux')

    stdin, stdout, stderr = client.exec_command('read variavel \n echo $variavel')
    stdin.write('Valor digitado')
    stdin.flush()

    if stdout.channel.recv_exit_status() ==0:
        print(stdout.read().decode('utf-8'))
    else:
        # print(stderr.read().decode('utf-8'))
        pass
except Exception as e:
    print(e)
