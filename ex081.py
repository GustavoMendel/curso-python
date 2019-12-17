print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"EXTRAINDO DADOS DE UMA LISTA":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

lista = list()
status = '.'
count = 0
x = False

while status not in 'nN':
    n = int(input('Digite um número: '))
    count = count + 1
    if n == 5:
        x = True
    lista.append(n)
    status = input('Deseja adicionar outro número? [\033[1:32mS\033[m/\033[1:31mN\033[m]')
    while status not in 'nNsS':
        status = input('Deseja adicionar outro número? [\033[1:32mS\033[m/\033[1:31mN\033[m]')

lista.sort(reverse=True)
print(f'\033[1:34m{"-"*40:^40}\033[m')
print(f'Foram digitados \033[1:36m{count} números.\033[m')
if x is True:
    print(f'\033[1:32mSIM! O número 5 foi digitado!\033[m')
else:
    print('\033[1:31mNÃO! O número 5 não foi digitado!\033[m')
print(f'A lista ordena de forma descrescente é: \033[1:35m{lista}\033[m')
