from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m      PROGRESSÃO ARITMÉTICA   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

a1 = int(input('Qual o primeiro terno da PA? '))
razao = int(input('Qual a razão da PA? '))
an = a1 + razao * 10

sleep(1)

j = 1
for i in range(a1, an, razao):
    print('a{} = \033[1:32m{}\033[m'.format(j, i))
    j = j+1
    sleep(1)
sleep(3)

