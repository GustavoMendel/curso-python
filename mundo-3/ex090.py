print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"DICIONÁRIO EM PYTHON":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = '\033[1:32mAprovado\033[m'
else:
    aluno['Situação'] = '\033[1:31mReprovado\033[m'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
