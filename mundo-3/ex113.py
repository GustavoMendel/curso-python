def intro(x):
    print(f'{"-" * 40:^40}')
    print(f'{x:^40}\033[m')
    print(f'{"-" * 40:^40}')


def line():
    print(f'{"-=" * 20}')


def readInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            break
        except (TypeError, ValueError):
            print(f'ERRO! Por favor digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida! ...')
            return 0
    return numero


def readFloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            break
        except (TypeError, ValueError):
            print(f'ERRO! Por favor digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida! ...')
            return 0
    return numero


intro('Erros e Exceções em Python')

nint = readInt('Digite um número inteiro: ')
nfloat = readFloat('Digite um número real: ')
line()
print(f'O número inteiro foi \t{nint}')
print(f'O número   real  foi \t{nfloat}')
line()
