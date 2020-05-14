from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m  TRATANDO VÁRIOS VALORES - v1.0   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

print('\033[1:34mDigite quantos números você quiser.\033[m')
sleep(1)
print('\033[1:33m[ 999 ] para FINALIZAR O PROGRAMA.\033[m')
sleep(2)

contador = 1
n = int(input('Digite um número: '))
soma = n

while n != 999:
    n = int(input('Digite outro número: '))
    if n != 999:
        soma = soma + n
        contador = contador + 1

sleep(1.7)
print('\033[1:31m[ ... Comando 999 registrado ... FINALIZANDO O PROGRAMA ... ]\033[m')
sleep(2)
print('Foram digitos uma quantidade de \033[1:32m{} números.\033[m'.format(contador))
sleep(2)
print('A soma entra todos estes números é: ')
sleep(1)
print('\033[1:34mSOMA = {}\033[m'.format(soma))
sleep(2)

