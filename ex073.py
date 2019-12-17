from time import sleep

print('\033[1:31m-=-\033[m' *9)
print('\033[1m      TIMES DE FUTEBOL  \033[m')
print('\033[1:31m-=-\033[m' *9)
sleep(1)

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Corinthians', 'Internacional',
        'Goiás', 'Fortaleza', 'Bahia', 'Vasco', 'Botafogo', 'Atlético-MG', 'Fluminense', 'Ceará', 'Cruzeiro', 'CSA',
        'Chapecoense', 'Avaí')

print('A) Os cinco primeiros colocados do Brasileirão são: ')
sleep(1)
print(f'\033[1:32m{times[0:5]}\033[m')
sleep(1)
print('B) Os quatro últimos colocados do Brasileirão são: ')
sleep(1)
print(f'\033[1:31m{times[-4:]}\033[m')
sleep(1)
print('C) Os times em ordem alfabética são: ')
sleep(1)
print(f'\033[1:34m{sorted(times)}\033[m')
sleep(1)
print(f'D) O Chapecoense está na seguinte posição do Brasileirão: ')
sleep(1)
print(f'\033[1:35m{times.index("Chapecoense")+1}ª posição\033[m')
sleep(1)
