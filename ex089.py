print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"BOLETINS COM LISTA COMPLETA":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

notas = list()
aux = list()
aux1 = list()
status = 'i'
media = aluno = cont = n1 = n2 = 0

while status not in 'nN':
    aux.append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    while n1 < 0 or n1 > 10:
        n1 = float(input('Nota 1: '))
    aux1.append(n1)
    n2 = float(input('Nora 2: '))
    while n2 < 0 or n2 > 10:
        n2 = float(input('Nota 2: '))
    aux1.append(n2)
    aux.append(aux1[:])
    notas.append(aux[:])
    aux.clear()
    aux1.clear()
    status = input('Deseja continuar? [\033[1:32mS\033[m/\033[1:31mN\033[m] ')
    while status not in 'nNsS':
        status = input('Deseja continuar? [\033[1:32mS\033[m/\033[1:31mN\033[m] ')

print(f'\033[1m{"-="*25}\033[m')
print('Nº  NOME', f'{"MÉDIA":>14}')
print(f'\033[1m{"-"*50}\033[m')

for c in range(0, len(notas)):
    media = (notas[c][1][0] + notas[c][1][1]) / 2
    if media >= 5:
        print(c, f'  {notas[c][0]:<14}', '\033[1:32m{:.2f}\033[m'.format(media))
    else:
        print(c, f'  {notas[c][0]:<14}', '\033[1:31m{:.2f}\033[m'.format(media))
    cont = cont + 1
print(f'\033[1m{"-" * 50}\033[m')
print('\033[33m[999 para INTERROMPER]\033[m')

while aluno != 999:
    aluno = int(input('Mostrar nota de qual aluno (Nº)? '))
    while aluno >= cont and aluno != 999:
        aluno = int(input('Mostrar nota de qual aluno (Nº)? '))
    if aluno == 999:
        break
    media = (notas[aluno][1][0] + notas[aluno][1][1]) / 2
    if media >= 5:
        print(f'Notas de \033[1:36m{notas[aluno][0]}\033[m são \033[1:32m{notas[aluno][1]}\033[m.')
    else:
        print(f'Notas de \033[1:36m{notas[aluno][0]}\033[m são \033[1:31m{notas[aluno][1]}\033[m.')
    print(f'\033[1m{"-" * 50}\033[m')
print('\033[1:31mFINALIZANDO ... \033[m')
print('<< VOLTE SEMPRE! >>')
