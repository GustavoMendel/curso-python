print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"UNINDO DICIONÁRIOS E LISTAS":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

status = 'o'
person = dict()
people = list()
girls = list()
totalPerson = somaIdade = 0

while status not in 'nN':
    totalPerson = totalPerson + 1
    person['Nome'] = str(input('Nome: '))
    person['Sexo'] = input('Sexo: [\033[1:34mM\033[m/\033[1:31mF\033[m] ')
    while person['Sexo'] not in 'mMfF':
        person['Sexo'] = input('Sexo: [\033[1:34mM\033[m/\033[1:31mF\033[m] ')
    person['Idade'] = int(input('Idade: '))
    people.append(person.copy())
    person.clear()
    status = input('Deseja continuar? [\033[1:32mS\033[m/\033[1:31mN\033[m] ')
    while status not in 'nNsS':
        status = input('Deseja continuar? [\033[1:32mS\033[m/\033[1:31mN\033[m] ')

for k in range(0, len(people)):
    somaIdade = somaIdade + people[k]['Idade']

media = float(somaIdade / totalPerson)

for i in range(0, len(people)):
    if people[i]['Sexo'] in 'fF':
        girls.append(people[i]['Nome'])

print(f'\033[1m{"-=" * 40}\033[m')
print(f'> O grupo é formado por \033[1:34m{totalPerson} pessoas\033[m.')
print(f'> A média de idade é de \033[1:35m{media:.1f} anos\033[m.')
print(f'> As mulheres cadastradas foram: ', end='')

for i in range(0, len(girls)):
    if len(girls) >= 2:
        if i == len(girls) - 1:
            print(f'\033[1:31m{girls[i]}\033[m.')
        elif i == len(girls) - 2:
            print(f'\033[1:31m{girls[i]}\033[m e', end=' ')
        else:
            print(f'\033[1:31m{girls[i]}\033[m,', end=' ')
    else:
        print(f'\033[1:31m{girls[i]}\033[m.')
print(f'\033[1m{"-=" * 40}\033[m')
print(f'> Lista das pessoas que estão acima da média:')
for i in range(0, len(people)):
    if people[i]['Idade'] > media:
        print(f'    <>', end=' ')
        for k, v in people[i].items():
            if k == 'Sexo':
                if v in 'mM':
                    print(f'\033[1m{k}\033[1m = \033[1:34m{v.upper()}\033[m; ', end='')
                elif v in 'fF':
                    print(f'\033[1m{k}\033[m = \033[1:31m{v.upper()}\033[m; ', end='')
            elif k == 'Nome':
                print(f'\033[1m{k}\033[m = \033[1:32m{v}\033[m; ', end='')
            elif k == 'Idade':
                print(f'\033[1m{k}\033[m = \033[1:33m{v}\033[m; ', end='')
        print()
print(f'\033[1m{"-=" * 40}\033[m')
print()
print(f'\033[33m{"< < < < < < < < < <-- ENCERRADO --> > > > > > > > > >":^80}\033[m')
