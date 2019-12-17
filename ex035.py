r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da terceira reta: '))
r3 = float(input('Digite o valor da segunda reta: '))

status = 1

if r1 > (r2 + r3):
    status = 0
if r2 > (r1 + r3):
    status = 0
if r3 > (r1 + r2):
    status = 0

if status == 0:
    print('\033[31mIMPOSSÍVEL!! Não é possível formar um triângulo!')

else:
    print('\033[31mÉ possível formar um triângulo!')
