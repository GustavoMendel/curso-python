from time import sleep
from sys import exit

print('\033[1:31m-=-\033[m' * 13)
print('\033[1m      GERENCIADOR DE PAGAMENTOS   \033[m')
print('\033[1:31m-=-\033[m' * 13)

sleep(1)
compras = float(input('Valor das compras: R$ '))
sleep(1)

print('''FORMAS DE PAGAMENTO:
[ 0 ] à vista dinheiro/cheque
[ 1 ] à vista cartão
[ 2 ] parcelado 2x no cartão
[ 3 ] parcelado 3x ou mais no cartão''')
x = int(input('Qual é a forma de pagamento? '))


status = 0
desconto = 0
parcelas = 0
valor = 0
valorParcela = 0

if x < 0 or x > 3:
    print('\033[1:31m... OPÇÃO INVÁLIDA ... FINALIZANDO PROGRAMA  ...\033[m')
    exit()
if x == 0:
    valor = compras - (compras * 0.10)
    status = '[ À VISTA NO DINHEIRO CHEQUE ]'
    desconto = '[ DESCONTO DE 10% ]'
elif x == 1:
    valor = compras - (compras * 0.05)
    status = '[ À VISTA NO CARTÂO ]'
    desconto = '[ DESCONTO DE 5% ]'
elif x == 2:
    valor = compras
    status = '[ PARCELADO EM 2X sem juros ]'
    desconto = '[ VALOR ORIGINAL ]'
elif x == 3:
    parcelas = int(input('Quantas parcelas? '))
    valor = compras + (compras * 0.20)
    valorParcela = valor / parcelas
    status = '[ PARCELADO EM 3X OU MAIS com juros ]'
    desconto = '[ JUROS DE 20% ]'
sleep(1)
print('''
\033[1m... AGUARDE ... PROCESSANDO DADOS ...\033[m
''')
sleep(3)

print('O valor das compras foi: \033[1:36mR$ {:.2f}\033[m'.format(compras))
sleep(2)
print('A forma de pagamento escolhida foi: \033[1:33m{}\033[m'.format(status))
sleep(2)
print('Mudança no valor do pagamento: \033[1:31m{}\033[m'.format(desconto))
sleep(3)

if x == 3:
    print('O número de parcelas escolhida foi: {} parcelas'.format(parcelas))
    sleep(2)
    print('O valor de cada parcela será: \033[1:34mR$ {:.2f}\033[m'.format(valorParcela))
    sleep(3)
elif x == 2:
    print('O valor de cada parcela será: \033[1:34mR$ {:.2f}\033[m'.format(valor/2))
    sleep(3)
print('''
''')
print('O cliente deverá pagar no total: \033[1:32mR$ {:.2f}\033[m'.format(valor))

print('''
''')
sleep(3)
print('\033[1:31m-=-\033[m' * 13)
print('\033[1m        ...FIM DO PROGRAMA...\033[m')
print('\033[1:31m-=-\033[m' * 13)
