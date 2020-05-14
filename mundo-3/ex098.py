from time import sleep


def line():
    print(f'\033[1m{"-=" * 20}\033[m')


def intro(x):
    print(f'\033[1:33m{"-" * 40:^40}\033[m')
    print(f'\033[1:33m{x:^40}\033[m')
    print(f'\033[1:33m{"-" * 40:^40}\033[m')


def counter(first, last, step):
    if first < last:
        if step < 0:
            step = -step
    print(f'A sua contagem de \033[1:32m{first} até {last}\033[m,'
          f' de \033[1:36m{step} em {step}\033[m: ')
    if step == 0:
        step = 1
    if first > last:
        if step > 0:
            step = -step
        last = last - 1
    elif first < last:
        last = last + 1
    sleep(1)
    for c in range(first, last, step):
        if c == first:
            print("\033[1m<\033[m", f'\033[1:34m{c}\033[m', end=' ')
        else:
            print(f'\033[1:34m{c}\033[m', end=' ')
        sleep(0.5)
    print('\033[1m>\033[m')
    sleep(0.5)
    print('\033[1:31mFIM!\033[m')
    sleep(0.5)
    line()
    sleep(0.5)


intro('FUNÇÃO DE CONTADOR')

counter(1, 10, 1)

counter(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim:    '))
d = int(input('Passo:  '))

counter(a, b, d)
