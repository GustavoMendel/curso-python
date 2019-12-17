from time import sleep

print('\033[1:31m-=-\033[m' *11)
print('\033[1m    ANALÍSE DE DADOS DE GRUPO  \033[m')
print('\033[1:31m-=-\033[m' *11)
sleep(1)
sexo = option = 'a'
idade = -1
count1 = count2 = count3 = 0

while True:
    print('\033[1m~~~\033[m' * 8)
    print('\033[1m  CADASTRE UMA PESSOA\033[m')
    print('\033[1m~~~\033[m' * 8)
    while 0 > idade < 200:
        idade = int(input('Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).upper()
    print('\033[1m~~~\033[m' * 8)
    if idade > 18:
        count1 = count1 + 1
    if sexo == 'M':
        count2 = count2 + 1
    if sexo == 'F' and idade < 20:
        count3 = count3 + 1
    while option != 'S' and option != 'N':
        option = str(input('Quer continuar? [S/N]')).upper()
    if option == 'N':
        break
    sexo = option ='a'
    idade = -1


sleep(1)
print('A) Quantas pessoas tem mais de 18 anos?')
sleep(1.5)
print(f'\033[1:32m{count1} pessoas\033[m')
sleep(1)
print('B) Quantos homens foram cadastrados? ')
sleep(1.5)
print(f'\033[1:36m{count2} homens\033[m')
sleep(1)
print('C) Quantas mulheres tem menos de 20 anos? ')
sleep(1.5)
print(f'\033[1:35m{count3} mulheres\033[m')
sleep(1)
