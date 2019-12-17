from time import sleep
from random import randint

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m      JOGO DO PAR OU ÍMPAR   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

computador = randint(0, 10)
contador = resultado = 0

while True:
    n = int(input('Digite um número: '))
    sleep(0.23)
    jogada = str(input('Par ou Ímpar? [ P / I ] ')).upper()
    sleep(1)
    if jogada != 'P' and jogada != 'I':
        print('\033[1:33m[ ... Jogada inválida ... Tente novamente ... ]\033[m')
        sleep(1)
    soma = n + computador
    if soma % 2 == 0:
        resultado = 'P'
    elif soma % 2 != 0:
        resultado = 'I'

    if resultado == jogada:
        print(f'O computador \033[1:35mjogou {computador}\033[m e você \033[1:33mjogou {n}\033[m')
        sleep(1)
        print(f'\033[1:36mO resultado foi {soma}\033[m')
        sleep(1)
        print('\033[1:32mMeus parabéns, você ganhou !!\033[m')
        sleep(1)
        print('\033[1m[ ... Tente ganhar novamente ... ]\033[m')
        sleep(1)
        contador = contador + 1
    if resultado != jogada:
        if jogada == 'P' or jogada == 'I':
            print(f'O computador \033[1:35mjogou {computador}\033[m e você \033[1:33mjogou {n}\033[m')
            sleep(1)
            print(f'\033[1:36mO resultado foi {soma}\033[m')
            sleep(1)
            sleep(1)
            print('\033[1:31mVOCÊ PERDEU !!\033[m')
            sleep(1)
            print(f'Ganhou {contador} partidas seguidas')
            sleep(2)
            break
