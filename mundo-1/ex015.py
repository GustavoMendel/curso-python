km = float(input('Qual a quantidade de KM rodados? '))
dias = int(input('Qual a quantidades de dias alugados? '))

KM = 0.15 * km
DIAS = 60 * dias
total = KM + DIAS

print('O valor total foi de RS{:.2f}'.format(total))
