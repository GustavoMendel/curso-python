from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m       ANALISADOR COMPLETO   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

soma = 0
homemVelho = 0
maior = 0
contadorMulheres = 0

for i in range(0, 4):
    nome = str(input('Qual o nome da {}ª pessoa? '.format(i+1)))
    idade = int(input('Qual a idade da {}ª pessoa? '.format(i+1)))
    sexo = str(input('Qual o sexo da {}ª pessoa? '.format(i+1)))

    soma = soma + idade
    if idade > maior and sexo == 'Homem':
        homemVelho = nome
        maior = idade
    if sexo == 'Mulher' and idade < 21:
        contadorMulheres = contadorMulheres + 1
sleep(1.5)
print('\033[1m... AGUARDE ... PROCESSANDO DADOS ...')
sleep(3)

media = soma / 4
print('A média de idade do grupo é de \033[1:34m{} anos\033[m'.format(media))
sleep(2)
print('O homem mais velho é o \033[1:33m{}\033[m'.format(homemVelho))
sleep(2)
print('O número de mulheres com menos de 21 anos é \033[1:31m{} mulheres\033[m'.format(contadorMulheres))
sleep(4)
