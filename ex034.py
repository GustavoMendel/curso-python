salario = int(input('Qual o salário atual do funcionário? R$ '))

if salario <= 1250:
    novoSalario = salario + (salario * 0.15)

else:
    novoSalario = salario + (salario * 0.10)

print('O novo salário deste funcionário será R$ {:.2f}'.format(novoSalario))
