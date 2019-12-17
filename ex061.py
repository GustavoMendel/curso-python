from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m   PROGRESSÃO ARITMÉTICA - v2.0   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

a1 = int(input('\033[1:33mDigite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: \033[m'))
soma = a1
sleep(1)

c = 1
while c <= 10:
    print('Termo[{}] = \033[1:34m{}\033[m'.format(c, soma))
    soma = soma + razao
    c = c + 1
    sleep(1)

sleep(1)
