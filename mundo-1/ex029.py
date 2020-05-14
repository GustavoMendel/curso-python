velocidade = int(input('Digite a sua velocidade: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('PARE! Você está acima do limite permitido!')
    print('Você está a {}Km/h, ultrapassou {}Km/h do limite!'.format(velocidade, velocidade - 80))
    print('Por isso, tomou uma multa de R$ {:.2f}'.format(multa))

print('Tenha um bom dia!')
