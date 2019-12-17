from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m  SEQUÊNCIA DE FIBUNACCI - v1.0   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

limite = int(input('Digite um limite de termos: [ -1 para infinito ] ')) + 1

a = 1
b = 1

sleep(0.25)
print('\033[1mFibonacci[0] = \033[1:32m0 ...\033[m')
sleep(0.25)
print('\033[1mFibonacci[1] = \033[1:32m1 ...\033[m')
sleep(0.25)
print('\033[1mFibonacci[2] = \033[1:32m1 ...\033[m')
sleep(0.25)
d = 3
c = 1
while d != limite:
     c = a + b
     print('\033[1mFibonacci[{}] = \033[1:32m{} ...\033[m'.format(d, c))
     sleep(0.25)
     b = a
     a = c
     d = d + 1
