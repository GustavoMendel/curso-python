from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m      TÁBUADA DE UM NÚMERO   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

valor = int(input('Digite um valor: '))

for i in range(0, 11):
    print('\033[1m{} x {} = \033[m\033[1:32m{}\033[m'.format(valor, i, valor*i))
