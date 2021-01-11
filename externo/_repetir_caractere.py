

"""
Módulo: _repetir_caractere.py

Objetivo:
         executar a repetição de uma string em uma quantidade especificada

Palavra chave: repetir string
"""

def repetir_caractere(caractere, qtd):
    print(f'{caractere}\n' * qtd)

if __name__ == '__main__':
    repetir_caractere('==', 41)
