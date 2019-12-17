from time import sleep
from sys import exit

print('\033[1:31m-=-\033[m' * 13)
print('\033[1m  ...ANALISANDO TRIÂNGULOS v2.0...\033[m')
print('\033[1:31m-=-\033[m' * 13)
sleep(1)
n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceito segmento: '))
sleep(1)
print('''
... PROCESSANDO ... AGUARDE ....
''')
sleep(3)
status = 1
if n1 > (n2 + n3):
    print('\033[1:31m[ ... NÃO É POSSÍVEL FORMAR TRIÂNGULO ... FINALIZANDO O PROGRAMA ... ]\033[m')
    exit()
elif n2 > (n1 + n3):
    print('\033[1:31m[ ... NÃO É POSSÍVEL FORMAR TRIÂNGULO ... FINALIZANDO O PROGRAMA ... ]\033[m')
    exit()
elif n3 > (n2 + n1):
    print('\033[1:31m[ ... NÃO É POSSÍVEL FORMAR TRIÂNGULO ... FINALIZANDO O PROGRAMA ... ]\033[m')
    exit()
else:
    print('\033[1:32m[ É POSSÍVEL FORMAR TRIÂNGULO ]\033[m')

sleep(2)
print('Tipo do triângulo: ')
sleep(3)
if n1 == n2 and n2 == n3:
    print('\033[1:36m[ EQUILÁTERO ]\033[m')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('\033[1:36m[ ISÓSCELES ]\033[m')
else:
    print('\033[1:36m[ ESCALENO ]\033[m')

sleep(3)

print('''
''')
print('\033[1:31m-=-\033[m' * 13)
print('\033[1m        ...FIM DO PROGRAMA...\033[m')
print('\033[1:31m-=-\033[m' * 13)


