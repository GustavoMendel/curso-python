distancia = int(input('Qual é a distância da viagem? '))

print('Você está prestes a começar uma viagem de {} Km'.format(distancia))

if distancia < 200:
    valor = distancia * 0.50

else:
    valor = distancia * 0.45

print('E o preço da sua passagem será R$ {:.2f}'.format(valor))


