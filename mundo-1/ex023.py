from math import floor

num = int(input('Digite um número: '))

milhar = floor(num / 1000)
centena = floor((num - milhar*1000) / 100)
dezena = floor((num - milhar*1000 - centena*100) / 10)
unidade = floor((num - milhar*1000 - centena*100 - dezena*10) / 1)

print('''Milhares: {}
Centenas: {}
Dezenas: {}
Unidades: {}'''.format(milhar, centena, dezena, unidade))

