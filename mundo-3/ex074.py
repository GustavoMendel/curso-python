from time import sleep
from random import randint

print('\033[1:31m-=-\033[m' *9)
print('\033[1m    MAIOR E MENOR VALOR  \033[m')
print('\033[1:31m-=-\033[m' *9)
sleep(1)

num = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
maior = 0
menor = 101

for c in range(0, 5):
    if num[c] > maior:
        maior = num[c]
    if num[c] < menor:
        menor = num[c]

print('Os números sorteados foram: ')
sleep(1)
print(f'\033[1:35m{num}\033[m')
sleep(1)
print(f'O MAIOR número foi: \033[1:32m{maior}\033[m')
sleep(1)
print(f'O MENOR número foi: \033[1:31m{menor}\033[m')
sleep(1)
