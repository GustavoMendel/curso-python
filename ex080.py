print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"LISTA ORDENADA SEM REPETIÇÕES":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

lista = list()
maior = menor = n = x = 0


for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0:
        x = 0
    elif n > lista[len(lista)-1]:
        x = len(lista)
    else:
        for j in range(0, len(lista)):
            if n <= lista[j]:
                x = j
                break
    lista.insert(x, n)
    print(f'O valor \033[1:34m{n}\033[m foi adicionado na posição \033[1:33m{x}\033[m')

print('\nA sua lista em ordem crescente é: ')
print(f'\033[1:32m{lista}\033[m')

