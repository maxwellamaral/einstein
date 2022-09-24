#  -*- coding: utf-8 -*-
"""
Realiza a 'advinhação' de uma resposta para uma pergunta.
Por enquanto funciona somente em Python > 3.0 para Windows
Adaptado de https://github.com/asweigart/pwinput/blob/main/src/pwinput/__init__.py
"""
import random
import sys
import os
from msvcrt import getch


def processa_pergunta(pergunta) -> str:
    """
    Processa a pergunta e retorna uma resposta, mascarando a resposta com a pergunta aleatória.
    :param pergunta:
    :return: str
    """
    resposta_inserida = []
    index_pergunta = 0
    while index_pergunta < len(pergunta):
        key = ord(getch())
        if key == 13:  # Quando a tecla ENTER é pressionada
            input('')
            sys.stdout.write('\n')
            return ''.join(resposta_inserida)
        elif key in (8, 127):  # A tecla Backspace/Del apaga a saída anterior.
            if len(resposta_inserida) > 0:
                # Erasing the previous character.
                # Apaga o caractere anterior.
                sys.stdout.write('\b \b')  # \b não apaga o caractere, apenas move o cursor para trás.
                sys.stdout.flush()
                resposta_inserida = resposta_inserida[:-1]
        elif 0 <= key <= 31:
            # Não faça nada por caracteres não imprimíveis.
            pass
        else:
            # Key is part of the password; display the mask character.
            caractere = chr(key)
            sys.stdout.write(pergunta[index_pergunta])
            sys.stdout.flush()
            resposta_inserida.append(caractere)
            index_pergunta += 1


if __name__ == '__main__':
    lista_perguntas = [
        'Oh grande máquina de pensar, teus mistérios são insondáveis,',
        'Oh iminente e poderoso computador, tu és meu oráculo iminencial, ',
        'Oh grande e poderoso computador, nem Einstein nem Newton te superam, ',
        'Oh vossa eminência computadorizada, vossa sabedoria é insondável, ',
        'Oh sapiência computacional, nem Issac Newton nem Albert Einstein te superam,',
    ]
    os.system('cls')
    print('\n\n')
    print('---------------------------------------------------------------------------------')
    print('------------- Olá, sou Einsten, apesar de morto, meu espírito vive --------------')
    print('-------------- Sei o que vejo, e às vezes sei até o que não vejo ----------------')
    print('------------ Vou tentar responder a pergunta que você vai me fazer. -------------')
    print('---------------------------------------------------------------------------------')
    print('\n\n')
    print('Faça em uma pergunta e pressione ENTER para continuar.\n\n')

    texto = processa_pergunta(random.choice(lista_perguntas))

    print(texto)
    key = ord(getch())
    if key == 13:
        os.system('cls')
