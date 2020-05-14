from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m         NÚMEROS PRIMOS   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

status = 0
count = 0

numero = int(input('Digite um número: '))

for i in range(1, numero + 1):
    sleep(0.25)
    if (numero % i) == 0:
        count = count + 1
        print('\033[1:32m{}\033[m'.format(i), end=' ')
    else:
        print('\033[1:31m{}\033[m'.format(i), end=' ')
print('\n')
sleep(2)

print('O número {} foi divisível {} vezes, por isso ...'.format(numero, count))
sleep(3)

if count > 2:
    print('\033[1:31m... NÃO É PRIMO ...\033[m')
else:
    print('\033[1:32m... É PRIMO ...\033[m')
