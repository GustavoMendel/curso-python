from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m   MAIOR E MENOR DA SEQUÊNCIA   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

maior = 0
menor = 1000
pessoaMenor = 0
pessoaMaior = 0

for i in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i+1)))
    if peso > maior:
        maior = peso
        pessoaMaior = i
    if peso < menor:
        menor = peso
        pessoaMenor = i

print('\033[1m... AGUARDE ... PROCESSANDO DADOS ...\033[m')
sleep(3)

print('O MENOR peso da sequência foi: \033[1:32m{:.1f} Kg\033[m\nQue foi o peso da {}ª pessoa'.format(menor,
                                                                                                      pessoaMenor+1))
sleep(3)
print('O MAIOR peso da sequência foi: \033[1:31m{:.1f} Kg\033[m\nQue foi o peso da {}ª pessoa'.format(maior,
                                                                                                      pessoaMaior+1))
sleep(3)
