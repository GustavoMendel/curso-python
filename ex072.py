from time import sleep

print('\033[1:31m-=-\033[m' *9)
print('\033[1m    NÚMERO POR EXTENSO  \033[m')
print('\033[1:31m-=-\033[m' *9)
sleep(1)

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    sleep(1)
    if n < 0 or n > 20:
        print('\033[33m... Número inválido ... TENTE NOVAMENTE ...\033[m')
    else:
        break

print(f'O número {n} por extenso é \033[1:32m{contagem[n]}\033[m')
sleep(1)
