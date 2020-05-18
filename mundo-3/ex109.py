from utilidades import moeda

valor = float(input('Digite o preço: R$ '))

print(f'O dobro de {moeda.formatar(valor)} é \n{moeda.dobro(valor, True)}\n')
print(f'A metade de {moeda.formatar(valor)} é \n{moeda.metade(valor, True)}\n')
print(f'{moeda.formatar(valor)} aumentado em 10% é \n{moeda.aumentar(valor, 10, True)}\n')
print(f'{moeda.formatar(valor)} diminuido em 20% é \n{moeda.diminuir(valor, 20, True)}\n')
