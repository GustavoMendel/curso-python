from time import sleep


def intro(x):
    print(f'\033[1:33m{"-" * 40:^40}\033[m')
    print(f'\033[1:33m{x:^40}\033[m')
    print(f'\033[1:33m{"-" * 40:^40}\033[m')


def line():
    print(f'\033[1m{"-=" * 20}\033[m')


def biggest(* number):
    maior = 0
    quantity = len(number)
    for h in number:
        if h > maior:
            maior = h
    print('\033[1m<\033[m', end=' ')
    sleep(0.5)
    for c in number:
        print(f'\033[1:34m{c}\033[m', end=' ')
        sleep(0.5)
    print('\033[1m>\033[m')
    sleep(0.5)
    print(f'Foram informado \033[1:31m{quantity} números\033[m ao todo!')
    sleep(1)
    print(f'O maior valor digitado foi \033[1:32m{maior}\033[m')
    sleep(1)
    line()
    sleep(1)


intro('FUNÇÃO PARA ACHAR O MAIOR')

sleep(0.5)

biggest(2, 9, 4, 5, 7, 1)

biggest(4, 7, 0)

biggest(1, 2)

biggest(6)

biggest()
