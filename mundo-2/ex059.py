from time import sleep

print('\033[1:31m-=-\033[m' * 10)
print('\033[1m        MENU DE OPÇÕES   \033[m')
print('\033[1:31m-=-\033[m' * 10)
sleep(1)

opcao = 0
maior = 0
menor = 0

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

sleep(1.5)

print('''\033[1:34mMENU DE OPÇÕES: \033[m
\033[1:34m[ 1 ]\033[m Somar os valores;
\033[1:34m[ 2 ]\033[m Multiplicar os valores;
\033[1:34m[ 3 ]\033[m Identificar o maior valor;
\033[1:34m[ 4 ]\033[m Digitar novos valores;
\033[1:34m[ 5 ]\033[m Finalizar o programa.''')

while opcao != 5:
    sleep(1)
    opcao = int(input('\033[1:34mQual opção deseja? \033[m'))

    if opcao == 1:
        sleep(1)
        print('A Soma dos valores \033[1:34m{}\033[m e \033[1:34m{}\033[m é ...'.format(n1, n2))
        sleep(1.5)
        print('\033[1:32m{}\033[m'.format(n1 + n2))
    elif opcao == 2:
        sleep(1)
        print('O produto dos valores \033[1:34m{}\033[m e \033[1:34m{}\033[m é ...'.format(n1, n2))
        sleep(1.5)
        print('\033[1:32m{}\033[m'.format(n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            menor = n2
        elif n2 > n1:
            maior = n2
            menor = n1
        elif n1 == n2:
            sleep(1)
            print('\033[1:33mOs dois valores são iguais !!\033[m')
        if n1 != n2:
            sleep(1)
            print('O maior valor é: \033[1:32m{}\033[m'.format(maior))
            sleep(1)
            print('O menor valor é: \033[1:31m{}\033[m'.format(menor))
    elif opcao == 4:
        n1 = int(input('Digite novamente o primeiro valor: '))
        n2 = int(input('Digite novamente o segundo valor: '))

sleep(0.9)
print('Finalizando o programa ... ')
sleep(1.5)
print('\033[1:31m-=-\033[m' * 10)
print('\033[1m       FIM DO PROGRAMA  \033[m')
print('\033[1:31m-=-\033[m' * 10)
