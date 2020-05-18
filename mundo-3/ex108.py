from utilidades import moeda

valor = float(input('Digite o preço: R$ '))

print(f'O dobro de {moeda.formatar(valor)} é \n{moeda.formatar(moeda.dobro(valor))}\n')
print(f'A metade de {moeda.formatar(valor)} é \n{moeda.formatar(moeda.metade(valor))}\n')
print(f'{moeda.formatar(valor)} aumentado em 10% é \n{moeda.formatar(moeda.aumentar(valor, 10))}\n')
print(f'{moeda.formatar(valor)} diminuido em 20% é \n{moeda.formatar(moeda.diminuir(valor, 20))}\n')
