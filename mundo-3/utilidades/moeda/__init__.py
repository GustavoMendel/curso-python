def dobro(n, format=False):
    r = n * 2.0
    return r if format is False else formatar(r)


def metade(n, format=False):
    r = n / 2.0
    return r if format is False else formatar(r)


def aumentar(n, taxa, format=False):
    r = n + n * (taxa / 100)
    return r if format is False else formatar(r)


def diminuir(n, taxa, format=False):
    r = n - n * (taxa / 100)
    return r if format is False else formatar(r)


def formatar(n):
    return f'R$ {n}'


def resumo(valor):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Valor analisado: \t{formatar(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'10% de aumento: \t{aumentar(valor, 10, True)}')
    print(f'20% de redução: \t{diminuir(valor, 20, True)}')
    print('-'*40)