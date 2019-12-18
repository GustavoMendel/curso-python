def intro(x):
    print(f'\033[1:33m{"-" * 40:^40}\033[m')
    print(f'\033[1:33m{x:^40}\033[m')
    print(f'\033[1:33m{"-" * 40:^40}\033[m')


def line():
    print(f'\033[1m{"-=" * 20}\033[m')


def grade(* num, sit=False):
    """
        -> Função para analisar a situação de vários alunos;
    :param num: Nota(s) dos alunos (aceita várias notas também);
    :param sit: Valor Booleano opcional, que indica ou não a situação da turma;
    :return: Um dicionário com as informações da turma.
    """
    player = dict()
    lista = list()
    maior = int(0)
    menor = int(20)
    soma = int(0)
    qnt = len(num)
    for c in range(0, qnt):
        lista.append(float(num[c]))
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
        soma = soma + lista[c]
    player['total'] = qnt
    player['maior'] = maior
    player['menor'] = menor
    player['média'] = soma / qnt
    if sit:
        if 0 <= player['média'] < 5:
            player['situação'] = 'RUIM'
        elif 5 <= player['média'] < 7:
            player['situação'] = 'RAZOÁVEL'
        elif 7 <= player['média'] <= 10:
            player['situação'] = 'ÓTIMA'
    return player


intro('ANALISANDO E GERANDO DICIONÁRIOS')

line()

result = grade(1, 4, 6, 10, sit=True)

for k, v in result.items():
    print(f'{k}: {v:.2f}')

line()
