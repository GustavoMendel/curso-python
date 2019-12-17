from time import sleep
from datetime import date

print('\033[1:31m-=-\033[m' * 13)
print('\033[1m  ...CLASSIFICAÇÃO DE ATLETAS...\033[m')
print('\033[1:31m-=-\033[m' * 13)

ano = int(input('Digite o ano de nascimento do atleta: '))
sleep(1.5)
idade = date.today().year - ano

print(
    '''\033[1m...PROCESSANDO DADOS...AGUARDE...
''')
print('''\033[33mObservações:
      A categoria dos atletas está ligado a sua idade;
      Até 9 anos: MIRIM
      Até 14 anos: INFANTIL
      Até 19 anos: JUNIOR
      Até 25 anos: SÊNIOR
      Acima de 25 anos: MASTER\033[m''')
sleep(7)

print('''
''')

print('Idade do atleta: {} anos'.format(idade))
print('Categoria do atleta: ')
sleep(2)

cor = '\033[1:31m'
defaut = '\033[m'

if idade <= 9:
    print('{}MIRIM{}'.format(cor, defaut))
elif idade <= 14:
    print('{}INFANTIL{}'.format(cor, defaut))
elif idade <= 19:
    print('{}JUNIOR{}'.format(cor, defaut))
elif idade <= 25:
    print('{}SÊNIOR{}'.format(cor, defaut))
else:
    print('{}MASTER{}'.format(cor, defaut))
