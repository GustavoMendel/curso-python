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
n = -1
m = 10
while c <= 10:
    print('Termo[{}] = \033[1:34m{}\033[m'.format(c, soma))
    soma = soma + razao
    c = c + 1
    sleep(1)
while n != 0:
    n = int(input('\033[1:33mDeseja mais quantos termos? \033[m'))
    m = m + n
    sleep(1)
    while c <= m:
        print('Termo[{}] = \033[1:34m{}\033[m'.format(c, soma))
        soma = soma + razao
        c = c + 1
        sleep(1)

print('\033[1:31m[ ... Comando registrado ... Finalizando programa ... ]\033[m')
sleep(1)
