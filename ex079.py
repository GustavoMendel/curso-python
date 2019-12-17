print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"MAIOR E MENOR VALOR NUMA LISTA":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

lista = list()
status = '-'
x = 1

while status not in 'nN':
    n = int(input('Digite um número: '))
    for i in range(0, len(lista)):
        if lista[i] == n:
            x = 0
    if x == 1:
        lista.append(n)
        print('\033[1:32mNúmero adicionado com sucesso!\033[m')
    else:
        print('\033[1:31mNúmero inválido, não adicionado!\033[m')
    x = 1
    status = str(input('Deseja adicionar outro número? [\033[1:32mS\033[m/\033[1:31mN\033[m]'))
    while status not in 'nNsS':
        status = str(input('Deseja adicionar outro número? [\033[1:32mS\033[m/\033[1:31mN\033[m]'))

print('')
print('Os números digitados em ordem CRESCENTE: ')
lista.sort()
print(f'\033[1:35m{lista}\033[m')
