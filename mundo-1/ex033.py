n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

maior = 0
menor = 10000

if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n1 < menor:
    menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
