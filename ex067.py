from time import sleep

print('\033[1:31m-=-\033[m' *8)
print('\033[1m     TÁBUADA - v3.0   \033[m')
print('\033[1:31m-=-\033[m' * 8)
sleep(1)

while True:
    n = int(input('Digite um número para saber sua tábuda: '))
    if n >= 0:
        for i in range(0, 11):
            sleep(0.37)
            print(f'{n} x \033[1:31m{i}\033[m = \033[1:32m{n*i}\033[m')
    if n < 0:
        break


sleep(1)
print('\033[1:31m[ ... Comando registrado ... FINALIZANDO O PROGRAMA ... ]')
sleep(1)
