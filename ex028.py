from random import randint

n1 = int(randint(0, 5))
n2 = int(input('Digite sua aposta: '))

if n1 == n2:
    print('Meus parabéns, você acertou!')
else:
    print('Você errou! O número que eu pensei foi {}'.format(n1))
