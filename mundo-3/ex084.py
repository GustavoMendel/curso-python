print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"LISTA COMPOSTA E ANÁLISE DE DADOS":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

pessoas = list()
aux = list()
status = 'o'
pesadas = list()
leves = list()
peso = 0
peso1 = 10000

while status not in 'nN':
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))
    pessoas.append(aux[:])
    aux.clear()
    status = input('Deseja adicionar outra pessoa? [\033[1:32mS\033[m/\033[1:31mN\033[m] ')
    while status not in 'nNsS':
        status = input('Deseja adicionar outra pessoa? [\033[1:32mS\033[m/\033[1:31mN\033[m] ')

for c in range(0, len(pessoas)):
    if c == 0:
        pesadas.append(pessoas[c])
        peso = pessoas[c][1]
        leves.append(pessoas[c])
        peso1 = pessoas[c][1]
    else:
        if pessoas[c][1] > peso:
            peso = pessoas[c][1]
            pesadas.clear()
            pesadas.append(pessoas[c])
        elif pessoas[c][1] == peso:
            pesadas.append(pessoas[c])
        if pessoas[c][1] < peso1:
            peso1 = pessoas[c][1]
            leves.clear()
            leves.append(pessoas[c])
        elif pessoas[c][1] == peso1:
            leves.append(pessoas[c])


print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'Foram cadastradas \033[1:32m{len(pessoas)} pessoas.\033[m')
print(f'O maior peso registrado foi \033[1:31m{pesadas[0][1]:.2f} Kg\033[m. Peso de ', end='')
for p in range(0, len(pesadas)):
    if p == len(pesadas) - 1:
        print(f'\033[1:31m{pesadas[p][0]}\033[m.')
    elif p == len(pesadas) - 2:
        print(f'\033[1:31m{pesadas[p][0]}\033[m e ', end='')
    else:
        print(f'\033[1:31m{pesadas[p][0]}\033[m, ', end='')
print(f'O menor peso registrado foi \033[1:36m{leves[0][1]:.2f} Kg\033[m. Peso de ', end='')
for l in range(0, len(leves)):
    if l == len(leves) - 1:
        print(f'\033[1:36m{leves[l][0]}\033[m.')
    elif l == len(leves) - 2:
        print(f'\033[1:36m{leves[l][0]}\033[m e ', end='')
    else:
        print(f'\033[1:36m{leves[l][0]}\033[m, ', end='')
