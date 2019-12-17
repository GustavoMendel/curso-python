from time import sleep

print('\033[1:31m-=-\033[m' *9)
print('\033[1m      CAIXA ELETRÔNICO  \033[m')
print('\033[1:31m-=-\033[m' *9)
sleep(1)

n = int(input('Qual valor quer sacar? R$ '))

x50 = int(n / 50)
x20 = int((n - x50 * 50) / 20)
x10 = int((n - x50*50 - x20*20) / 10)
x1 = int(n - x50*50 - x20*20 - x10*10)

sleep(1)
if x50 != 0:
    print(f'\033[1:32m{x50} notas de R$ 50.00\033[m')
    sleep(1)
if x20 != 0:
    print(f'\033[1:34m{x20} notas de R$ 20.00\033[m')
    sleep(1)
if x10 != 0:
    print(f'\033[1:35m{x10} notas de R$ 10.00\033[m')
    sleep(1)
if x1 != 0:
    print(f'\033[1:36m{x1} notas de R$ 1.00\033[m')
    sleep(1)
