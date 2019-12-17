print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"MAIOR E MENOR VALOR NUMA LISTA":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

lista = list()
maior = 0
menor = 1000000
pos_maior = 0
pos_menor = 0

for i in range(0, 5):
    lista.append(int(input(f'Digite o {i+1}º valor: ')))
    if lista[i] > maior:
        maior = lista[i]
        pos_maior = i
    if lista[i] < menor:
        menor = lista[i]
        pos_menor = i

print(f'O maior valor encontrado foi \033[1:32m{maior}\033[m na posição \033[1:32m{pos_maior}\033[m')
print(f'O menor valor encontrado foi \033[1:31m{menor}\033[m na posição \033[1:31m{pos_menor}\033[m')
