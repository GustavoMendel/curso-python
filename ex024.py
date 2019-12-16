nome = str(input('Em qual cidade você nasceu? '))

nome = nome.strip()
nome = nome.lower()
nome = nome.split()[0]
status = 'santo' in nome

print('A sua cidade começa com a palavra -Santo- ?')

if status:
    print('Sim, sua cidade começa com a palavra -Santo-')

else:
    print('Não, sua cidade não começa com a palavra -Santo-')
