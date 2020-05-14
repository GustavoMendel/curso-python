from datetime import date

ano = int(input('Em que ano você está? Digite 0 se você deseja analisar seu ano atual. '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 != 0:
        print('O ano {} NÃO é BISSEXTO!'.format(ano))
    else:
        print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))
