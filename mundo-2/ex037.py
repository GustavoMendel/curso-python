from time import sleep
from sys import exit

print('\033[1:31m-=-\033[m' * 10)
print('\033[1m    ...CONVERSOR DE BASE...\033[m')
print('\033[1:31m-=-\033[m' * 10)

cor = '\033[1:36m'
defaut = '\033[m'

numero = int(input('Digite um número inteiro: '))
print('''Escolhe uma das opções abaixo:
{}[ 2 ]{} para converter para {}BINÁRIO{}
{}[ 8 ]{} para converter para {}OCTAL{}
{}[ 12 ]{} para converter para {}HEXADECIMAL{}'''.format(cor, defaut, cor, defaut, cor, defaut, cor, defaut, cor, defaut,
                                                         cor, defaut))

x = int(input('Digite uma opção: '))
sleep(2)

count = 0
resultado = 0

if x == 2:
    resultado = bin(numero)[2:]
    count = str("BINÁRIO")
elif x == 8:
    resultado = oct(numero)[2:]
    count = str("OCTAL")
elif x == 12:
    resultado = hex(numero)[2:]
    count = str("HEXADECIMAL")
else:
    print('\033[1:31m...OPÇÃO INVÁLIDA...FINALIZANDO O PROGRAMA...\033[m')
    exit()

print('A opção escolhida foi: \033[1:36m[ {} ]\033[m'.format(x))
print('O número será convertido para a base \033[1:36m{}\033[m'.format(count))
sleep(2)
print('''
\033[1:37m...PROCESSANDO...\033[m
''')
sleep(3)

print('O número {} foi convertido para ...'.format(numero))
sleep(2)
print('\033[1:32m{}\033[m'.format(resultado))

sleep(2)

print('\033[1:31m-=-\033[m' * 10)
print('\033[1m    ...FIM DO PROGRAMA...\033[m')
print('\033[1:31m-=-\033[m' * 10)
