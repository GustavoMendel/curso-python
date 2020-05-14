valorCasa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestação = valorCasa / (anos * 12)

from time import sleep

if prestação > salario * 0.30:
    status = 0
else:
    status = 1

sleep(3)

print('''O valor da casa é R$ {:.2f}
O tempo para financiamento é de {} anos
Portanto, as prestações terão valor de \033[1:35mR$ {:.2f}\033[m
Sendo assim, seu financiamento foi ...'''.format(valorCasa, anos, prestação))
sleep(3)

if status == 0:
    print('\033[1:31mNEGADO!!\033[m')
else:
    print('\033[1:32mAPROVADO!!\033[m')
