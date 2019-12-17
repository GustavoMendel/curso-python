from time import sleep
from random import randint


def intro(x):
    print(f'\033[1:33m{"-" * 40:^40}\033[m')
    print(f'\033[1:33m{x:^40}\033[m')
    print(f'\033[1:33m{"-" * 40:^40}\033[m')


def line():
    print(f'\033[1m{"-=" * 20}\033[m')


def sort(list):
    print('Sorteando 5 valores da lista: ')
    sleep(0.6)
    print('\033[1m<\033[m', end=' ')
    sleep(0.6)
    for c in range(0, 5):
        h = randint(0, 10)
        list.append(h)
        print(f'\033[1:34m{h}\033[m', end=' ')
        sleep(0.6)
    print('\033[1m>\033[m')
    sleep(0.6)
    line()
    sleep(0.6)


def sumPair(list):
    soma = 0
    for c in list:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de ')
    sleep(0.6)
    print('[', end='')
    for c in range(0, 5):
        sleep(0.6)
        if c == 4:
            if list[c] % 2 == 0:
                print(f'\033[1:32m{list[c]}\033[m', end='')
            else:
                print(f'\033[1m{list[c]}\033[m', end='')
        else:
            if list[c] % 2 == 0:
                print(f'\033[1:32m{list[c]}\033[m', end=', ')
            else:
                print(f'\033[1m{list[c]}\033[m', end=', ')
    sleep(0.6)
    print(']')
    sleep(0.6)
    print(f'Temos um \033[1:31mtotal de {soma}!\033[m')
    sleep(0.6)
    line()


intro('FUNÇÕES PARA SORTEAR E SOMAR')

sleep(0.6)

numbers = list()

sort(numbers)

sumPair(numbers)
