#!/usr/bin/env python3

def vermelho(texto):
    def altera(texto):
        return f'\033[91m{texto}\033[0m'  # Pegar da tabela ANSI
    return altera

@vermelho
def texto(fala: str) -> str:
    return fala

print(texto('Oi'))