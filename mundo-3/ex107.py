from utilidades import moeda

valor = float(input('Digite o preço: R$ '))

print(f'O dobro de R$ {valor} é \nR$ {moeda.dobro(valor)}\n')
print(f'A metade de R$ {valor} é \nR$ {moeda.metade(valor)}\n')
print(f'R$ {valor} aumentado em 10% é \nR$ {moeda.aumentar(valor, 10)}\n')
print(f'R$ {valor} diminuido em 20% é \nR$ {moeda.diminuir(valor, 20)}\n')
