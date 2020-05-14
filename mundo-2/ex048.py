from time import sleep

print('\033[1:31m-=-\033[m' * 13)
print('\033[1m  SOMA DE ÍMPARES E MÚLTIPLOS DE TRÊS   \033[m')
print('\033[1:31m-=-\033[m' * 13)
sleep(1)

soma = 0

for i in range(1, 501):
    if i %2 == 1 and i %3 == 0:
        soma += i

print('A soma de todos os números ímpares e múltiplos de três é: ...')
sleep(2)
print('\033[1:32m{}\033[m'.format(soma))
