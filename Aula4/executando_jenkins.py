#!/usr/bin/env python3

import jenkins

try:
    client = jenkins.jenkins('http://localhost:8080', username='tsubasa', password='yama1102')
except Exception as e:
    print(e)
    exit(1)

# Pegar o atributos do usuario logado na plataforma
user =client.get_whoami()

# Pegar o versao do servidor
version = client.get_version()
print(version)

# Pegar quantidade de jobs criados
print(client.jobs_count())

#Pegar configuração de um job
try:
    client.get_job_config('job_vazio2')
except Exception as e:
    print(e)
#c Criar jobs
    client.create_job('job_vazio2',jenkins.EMPTY_CONFIG_XML)

print(client.jobs_count())

# Build em um job
client.build_job('Meu Deploy')

# Desabilitar um job
client.disable_job('Meu Deploy')

# Deletar um job
client.delete_job('job_vazio')

# habilitar um job
client.enable_job('Meu Deploy')

# Reconfigurar um job
client.reconfig_job('job_vazio2', jenkins.RECONFIG_XML)

# Copiar um job
client.copy_job('job_vazio2', 'job_vazio')

# Pegar informações de um job
print(client.get_job_info('Meu Deploy'))

# Trabalhar com plugins
# Pegar as informações dos plugins
print(client.get_plugins())

# Pegar as informações de um plugin em específico
print(client.get_plugin_info('Email Extension Plugin'))

# Tempo para o jenkins estar preparado
if client.wait_for_normal_op(30):
    print('Rodando normal')
else:
    raise Exception('Deu ruim')