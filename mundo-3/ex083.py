print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"VALIDANDO EXPRESSÕES MATEMÁTICAS":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

lista = list()

exp = str(input('Digite sua expressão: '))

for i in range(0, len(exp)):
    if exp[i] == '(':
        lista.append('(')
    elif exp[i] == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('\033[1:32m\nSIM! A expressão é VÁLIDA!\033[m')
elif len(lista) != 0:
    print('\033[1:31m\nNÃO! A expressão é INVÁLIDA!\033[m')
