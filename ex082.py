print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"PARES E ÍMPARES EM UMA LISTA":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

lista = list()
pares = list()
impares = list()
status = '0'

while status not in 'nN':
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)
    status = input('Deseja adicionar outro número? [\033[1:32mS\033[m/\033[1:31mN\033[m]')
    while status not in 'sSnN':
        status = input('Deseja adicionar outro número? [\033[1:32mS\033[m/\033[1:31mN\033[m]')

print(f'\033[1:34m{"-"*40:^40}\033[m')
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: \033[31m{pares}\033[m')
print(f'A lista de ímpares é: \033[32m{impares}\033[m')
