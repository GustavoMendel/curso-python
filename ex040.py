from time import sleep
from sys import exit

print('\033[1:31m-=-\033[m' * 13)
print('\033[1m  ...VERIFICAÇÃO DE APRENDIZAGEM...\033[m')
print('\033[1:31m-=-\033[m' * 13)

print('''
''')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

if(nota1 > 10 or nota2 > 10):
    sleep(1.5)
    print('\033[1:31m...NOTA INVÁLIDA...FINALIZANDO PROGRAMA...\033[m')
    exit()

media = (nota1 + nota2) / 2

sleep(1)
print('\033[1m...PROCESSANDO NOTAS...AGUARDE...\033[m')
sleep(0.5)
print('''\033[33mObservações:
O aluno deve ter uma nota igual ou superior a 7.0 pontos para ser APROVADO;
Se o aluno obtiver uma nota entre 5.0 e 6.9 pontos, irá para RECUPERAÇÃO;
Se o aluno obtiver uma nota abaixo de 5.0, ele será REPROVADO.\033[m
''')
sleep(6.5)

print('Nota do aluno: \033[1:37m{:.2f}\033[m pontos'.format(media))
print('A situação do aluno é...')
sleep(3)
if media >= 7:
    print('\033[1:32mAPROVADO!\033[m')
    if media == 10:
        print('\033[1:32mMeus parabéns!\033[m')
elif media >= 5 and media < 7:
    print('\033[1:36mRECUPERAÇÃO!\033[m')
elif media < 5:
    print('\033[1:31mREPROVADO!\033[m')

sleep(3)
print('\033[1:31m-=-\033[m' * 10)
print('\033[1m    ...FIM DO PROGRAMA...\033[m')
print('\033[1:31m-=-\033[m' * 10)


