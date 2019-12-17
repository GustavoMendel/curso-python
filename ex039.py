from datetime import date
from time import sleep

print('\033[1:31m-=-\033[m' * 10)
print('\033[1m  ...ALISTAMENTO MILITAR...\033[m')
print('\033[1:31m-=-\033[m' * 10)

ano = int(input('Em que ano você nasceu? '))
today = date.today().year
dif = today - ano

sleep(2)
print('''\033[1m...PROCESSANDO...AGUARDE...
      ''')
sleep(3)

if dif < 18:
    status = -1
elif dif > 18:
    status = 1
else:
    status = 0

if status == -1:
    print('Ano de nascimento do candidato: {}'.format(ano))
    print('Ano do dia atual: {}'.format(today))
    print('O candidato tem {} anos'.format(dif))
    print('O candidato ainda não está apto a se alistar.')
    print('Se alistará no ano {}'.format(today + (18-dif)))
if status == 0:
    print('Ano de nascimento do candidato: {}'.format(ano))
    print('Ano do dia atual: {}'.format(today))
    print('O candidato tem {} anos'.format(dif))
    print('O candida deve se alistar IMEDIATAMENTE')
if status == 1:
    print('Ano de nascimento do candidato: {}'.format(ano))
    print('Ano do dia atual: {}'.format(today))
    print('O candidato tem {} anos'.format(dif))
    print('O candidato já passou da hora de se alistar')
    print('Se alistou no ano {}'.format(today - (dif-18)))
