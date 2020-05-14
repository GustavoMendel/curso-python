from datetime import datetime

print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"CADASTRO DE TRABALHADOR EM PYTHON":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

person = dict()

person['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
person['Idade'] = datetime.today().year - nascimento
person['Carteira de Trabalho'] = int(input('Carteira de Trabalho: '))

if person['Carteira de Trabalho'] == 0:

    print(f'\033[1m{"-=" * 25}\033[m')

    for k, v in person.items():
        if k == 'Nome':
            print(f'Seu {k} é {v}')
        elif k == 'Idade':
            print(f'Sua {k} é {v}')
        else:
            print(f'Ainda não possui {k}.')

    print(f'\033[1m{"-=" * 25}\033[m')

else:
    person['Ano de Contratação'] = int(input('Ano de Contratação: '))
    person['Salário'] = float(input('Salário: '))
    person['Idade para aposentar'] = (person['Ano de Contratação'] + 35) - nascimento

    print(f'\033[1m{"-=" * 25}\033[m')

    for k, v in person.items():
        if k == 'Nome':
            print(f'Seu {k} é \033[1:32m{v}\033[m')
        elif k == 'Ano de Contratação':
            print(f'Você entrou no mercado de trabalho em \033[1:34m{v}\033[m')
        elif k == 'Carteira de Trabalho':
            print(f'{k}: \033[1:33m{v}\033[m')
        elif k == 'Idade':
            print(f'Sua {k} é \033[1:35m{v}\033[m')
        elif k == 'Salário':
            print(f'Seu {k} é de \033[1:36mR$ {v:.2f}\033[m')
        else:
            print(f'Você irá se aposentar com \033[1:31m{v} anos de idade.\033[m')

    print(f'\033[1m{"-=" * 25}\033[m')
