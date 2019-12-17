from time import sleep
from random import randint

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m   JOGO DA ADVINHAÇÃO - v2.0   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

print('''Computador: Acabei de pensar em um número entre 0 e 10 !
Consegue advinhar qual é?
''')
num = randint(0, 10)
sleep(1.5)

palpite = int(input('Qual o seu palpite? '))
contador = 1

sleep(1)

while palpite != num:
    if palpite < num:
        palpite = int(input('\033[1:31mVOCÊ ERROU!\033[m É MAIS\033[1:31m ... Tente novamente ... \033[m'))
        contador = contador + 1
        sleep(0.5)
    elif palpite > num:
        palpite = int(input('\033[1:31mVOCÊ ERROU!\033[m É MENOS\033[1:31m ... Tente novamente ... \033[m'))
        contador = contador + 1
        sleep(0.5)

sleep(1)
print('\033[1:32mMEUS PARABÉNS!! Você acertou!!\033[m')
sleep(1)
if contador == 1:
    print('ACERTOU DE PRIMEIRA, MEUS PARABÉNS!')
else:
    print('Teve um total de {} tentativas.'.format(contador))
