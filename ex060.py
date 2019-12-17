from time import sleep

print('\033[1:31m-=-\033[m' * 6)
print('\033[1m     FATORIAL   \033[m')
print('\033[1:31m-=-\033[m' * 6)
sleep(1)

numero = int(input('\033[1:33mDigite um número: \033[m'))

c = numero - 1
fatorial = numero

while c > 0:
    fatorial = fatorial * c
    c = c - 1

sleep(1)
print('O fatorial de {} é ...'.format(numero))
sleep(1)
print('{}! = \033[1:32m{}\033[m'.format(numero, fatorial))
sleep(1)
