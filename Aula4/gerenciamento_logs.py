#!/usr/bin/env python3

import logging

logging.basicConfig(
    filename='app.log',
    level = logging.DEBUG,
    format= '%(asctime)s { %(levelname)s ] %(name)s\n'
        +
        "[%(funcName)s] [%(filename)s, %(lineno)s] %(message)s",
        datefmt="[ %d/%m/%Y %H:%M:%S ]"
)

# logging.debug('Mensagem de debug')

def soma(n1,n2):
    try:
        logging.info('Soma efetuada com sucesso')
        return n1 + n2
    except Exception:
        logging.error('Deu erro')

CUSTOM = 49

logging.addLevelName(CUSTOM,"CUSTOM")

def alert(self, message, *args, **kwargs):
    if self.isEnabledFor(CUSTOM):
        self._log(CUSTOM, message, args **kwargs)
    
logging.Logger.custom = alert

logger = logging.getLogger()
logger.custom('Mensagem de logs customizada')

# print(soma(1,1))