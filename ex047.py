from time import sleep

print('\033[1:31m-=-\033[m' * 13)
print('\033[1m         CONTAGEM DE PARES   \033[m')
print('\033[1:31m-=-\033[m' * 13)

for i in range(1, 51):
    if i % 2 == 0:
        sleep(1)
        print('\033[1:32m{}...\033[m'.format(i))
