from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m    VÁRIOS NÚMEROS COM FLAG   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

n = int(input('''\033[1:33m[ 999 ] para parar\033[m
Digite um número: '''))
contador = 1
soma = n

while True:
    n = int(input('''\033[1:33m[ 999 ] para parar\033[m
Digite um número: '''))
    if n != 999:
        contador = contador + 1
        soma = soma + n
    else:
        break

sleep(2)
print(f'\033[1:35mNÚMEROS DIGITADOS = {contador} números\033[m')
sleep(1)
print(f'\033[1:36mSOMA = {soma}\033[m')
sleep(2)
