from time import sleep

print('\033[1:31m-=-\033[m' * 13)
print('\033[1m        ÍNDICE DE MASSA CORPORAL   \033[m')
print('\033[1:31m-=-\033[m' * 13)

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual sua altura? (metros) '))

imc = peso / pow(altura, 2)
sleep(2)
print('\033[1m... PROCESSANDO DADOS ... AGUARDE ...')
sleep(3)

print('Seu índice de massa corporal (IMC) é {:.1f}'.format(imc))
sleep(2)
print('Seu status é: ...')
sleep(2)

if imc < 18.5:
    print('\033[1:36m[ ABAIXO DO PESO ]\033[m')
elif imc < 25:
    print('\033[1:32m[ PESO IDEAL ]\033[m')
elif imc < 30:
    print('\033[1:35m[ SOBREPESO ]\033[m')
elif imc < 40:
    print('\033[1:33m[ OBESIDADE ]\033[m')
else:
    print('\033[1:31m[ OBESIDADE MÓRBIDA ]\033[m')

sleep(3)

print('''
''')
print('\033[1:31m-=-\033[m' * 13)
print('\033[1m        ...FIM DO PROGRAMA...\033[m')
print('\033[1:31m-=-\033[m' * 13)

