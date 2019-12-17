frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A letra A apareceu pela primera vez na pocição {}'.format(frase.find('a') + 1))
print('A letra A apareceu pela última vez na pocição {}'.format(frase.rfind('a') + 1))


