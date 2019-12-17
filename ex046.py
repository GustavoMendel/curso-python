from time import sleep

print('\033[1:31m-=-\033[m' * 13)
print('\033[1m          FOGOS DE ARTIFÍCIO   \033[m')
print('\033[1:31m-=-\033[m' * 13)

sleep(1)

print('\033[1mVamos nos preparar para a contagem regressiva para o ANO NOVO\033[m')

sleep(2)

for i in range(10, -1, -1):
    print('\033[1:32m{}...\033[m'.format(i))
    sleep(1)

sleep(1)
print('\033[1:31m... FELIZ ANO NOVO!!!! ...\033[m')
sleep(1)
print('\033[1:33m... POW POW POW POW POW BOOM ...\033[m')
