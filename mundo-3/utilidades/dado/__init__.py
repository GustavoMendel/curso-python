def leiaDinheiro():
    valido = False
    while not valido:
        valor = input('Digite o preço: R$ ').replace(',', '.').strip()
        if valor.isalpha() or valor.strip() == '':
            print(f'ERRO: \\ {valor} \\ é um preço inválido!')
        else:
            valido = True
            return float(valor)
