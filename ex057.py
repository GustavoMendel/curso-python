from time import sleep

print('\033[1:31m-=-\033[m' * 11)
print('\033[1m       VALIDAÇÃO DE DADOS   \033[m')
print('\033[1:31m-=-\033[m' * 11)
sleep(1)

sexo = str(input('Informe um sexo: [m/f] ')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('\033[1:31mO sexo informado não é válido, tente novamente:  \033[m')).upper()

print('\033[1:32mSUCESSO!! Sexo {} registrado com sucesso.\033[m'.format(sexo))
