from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m         LENDO PALÍNDROMOS   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

frase = str(input('Digite uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = ''

j = 0
for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
    j = j + 1

sleep(2)
print('\033[1m... VERIFICANDO ... AGUARDE ...\033[m')
sleep(3)

print('O seu texto é \033[1:33m{}\033[m'.format(junto))
sleep(2)
print('E o inverso é \033[1:34m{}\033[m'.format(inverso))
sleep(2)
print('Ou seja...')
sleep(3)
if inverso == junto:
    print('\033[1:32mÉ UM PALÍNDROMO !!\033[m')
else:
    print('\033[1:31mNÃO É UM PALÍNDROMO !!\033[m')
sleep(4)
