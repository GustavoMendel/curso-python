from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m      MAIOR E MENOR VALORES   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

maior = 0
menor = 10000
contador = 1

n = int(input('Digite um valor: '))
soma = n
p = 1
if n > maior:
    maior = n
if n < menor:
    menor = n
print('Digite [ 0 ] para parar ou [ 1 ] para continuar')

while p != 0:
    p = int(input('\033[1:33m[ 0 / 1 ] \033[m'))
    if p == 1:
        n = int(input('Digite outro valor: '))
        contador = contador + 1
        soma = soma + n
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if p != 1 and p != 0:
        sleep(1)
        print('\033[1:33m[ Opção inváida ... Digite ou 0 ou 1 ... ]\033[m')
    if p == 0:
        sleep(1)
        print('\033[1:31m[ ... Comando ZERO registrado ... Finalizando o programa ... ]\033[m')
        print('')

sleep(1.7)
media = soma / contador
sleep(1)
print('Foram digitados \033[1:32m{} números.\033[m'.format(contador))
sleep(1)
print('A média entre todos os números é: ')
sleep(1)
print('\033[1:34mMÉDIA = {:.2f}\033[m'.format(media))
sleep(1)
print('O maior número digitado foi: {}'.format(maior))
sleep(1)
print('O menor número digitado foi: {}'.format(menor))
sleep(2)
