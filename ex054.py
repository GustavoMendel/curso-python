from time import sleep
from datetime import date

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m       GRUPO DE MAIORIDADE   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

numMaior = 0
numMenor = 0
anoAtual = date.today().year

for i in range(0, 7):
    anoPessoa = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i+1)))
    if anoAtual - anoPessoa >= 21:
        numMaior = numMaior + 1
    else:
        numMenor = numMenor + 1

print('\033[1m... AGUARDE ... PROCESSANDO DADOS ...\033[m')
sleep(3)


print('O número de pessoas que são de MENOR: \033[1:31m{} pessoas\033[m'.format(numMenor))
sleep(2)
print('O número de pessoas que são de MAIOR: \033[1:32m{} pessoas\033[m'.format(numMaior))
sleep(3)

