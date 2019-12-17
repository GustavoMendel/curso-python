from time import sleep

print('\033[1:31m-=-\033[m' *11)
print('\033[1m    ESTATÍSTICAS EM PRODUTOS  \033[m')
print('\033[1:31m-=-\033[m' *11)
sleep(1)

option = 'a'
menor = 100000
menor1 = 'a'
count = count2 = 0

while True:
    print('\033[1m~~~\033[m' * 8)
    print('\033[1m  CADASTRE UM PRODUTO\033[m')
    print('\033[1m~~~\033[m' * 8)
    nome = str(input('Nome: '))
    valor = float(input('Preço: R$ '))
    count = count + valor
    if valor > 1000:
        count2 = count2 + 1
    if valor < menor:
        menor = valor
        menor1 = nome
    print('\033[1m~~~\033[m' * 8)
    while option != 'S' and option != 'N':
        option = str(input('Quer continuar? [S/N] ')).upper()
    if option == 'N':
        break
    option = 'a'

sleep(1)
print('A) Qual o total gasto na compra? ')
sleep(1.38)
print('\033[1:32mR$ {:.2f}\033[m'.format(count))
sleep(1)
print('B) Quantos produtos custam mais de R$ 1000.00 ?')
sleep(1.38)
print(f'\033[1:34m{count2} produtos\033[m')
sleep(1)
print('C) Qual é o produto mais barato? ')
sleep(1.38)
print('\033[1:35m{}\033[m que custa \033[1:32mR$ {:.2f}\033[m'.format(menor1, menor))
sleep(1)
