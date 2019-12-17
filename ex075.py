from time import sleep
from random import randint

print('\033[1:31m-=-\033[m' *9)
print('\033[1m     ANÁLISE DE DADOS  \033[m')
print('\033[1:31m-=-\033[m' *9)
sleep(1)

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
sleep(1)

n = (n1, n2, n3, n4)
count = 0
count3 = 0
for c in range(0, 4):
    if n[c] % 2 == 0:
        count = count + 1
    if n[c] == 3:
        count3 = 1

print(f'O número 9 apareceu \033[1:35m{n.count(9)} vezes\033[m')
sleep(1)
if count3 == 1:
    print(f'O número 3 foi digitado pela primeira vez na \033[1:32m{n.index(3) + 1}ª posição\033[m')
    sleep(1)
else:
    print('\033[1:33m# O número 3 não foi digitado #\033[m')
    sleep(1)
print('Os números pares digitados foram: ')
for c in range(0, 4):
    if n[c] % 2 == 0:
        sleep(1)
        count = count + 1
        print(f'\033[1:34m{n[c]}\033[m', end=' ')
if count == 0:
    sleep(1)
    print('\033[1:33m# Não foram digitados números pares #\033[m')
