from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m        SOMAS DOS PARES   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

soma = 0
for i in range(0, 6):
    valor = int(input('Digite o {}º valor: '.format(i+1)))
    if valor % 2 == 0:
        soma += valor

print('A soma de todos os números pares é: ')
sleep(2)
print('\033[1:32m{}\033[m'.format(soma))
