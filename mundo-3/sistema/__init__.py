import sys

def mensagem(msg, nup=True):
    if nup is True:    
        print('-'*50)
        print(f'{msg}'.center(50).upper())
        print('-'*50)
    elif nup is False:
        print('-'*50)
        print(f'{msg}'.center(50))
        print('-'*50)

def recebeOpcao():
    mensagem('Menu Principal')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do Sistema')

    print('-'*50)
    while True:
        try:
            opcao = int(input('Sua Opção: '))
            if opcao in [1,2,3]:
                break
            else:
                print('ERRO! Digite uma opção válida!\n')
        except (TypeError, ValueError):
            print('ERRO! Digite uma opção válida!\n')
        except KeyboardInterrupt:
            print('\nERRO! Entrada cancelada pelo usuário.')
            finalizaSistema()
            sys.exit()
    return opcao


def lerPessoas():
    mensagem('Pessoas Cadastradas')
    try:
        arquivo = open('pessoas.txt', 'r')
    except Exception:
        print('ERRO! Falha ao encontrar arquivo.')
        print('Adicione uma nova pessoa para criar arquivo.')
        return 0
    for linha in arquivo:
        pessoa = arquivo.readline().strip()
        idade = arquivo.readline().strip()
        print(f'{pessoa:<30} {idade:>10} anos')
    arquivo.close()


def adicionaPessoas():
    mensagem('Novo Cadastro')
    arquivo = open('pessoas.txt', 'a')

    while True:
        try:
            novaPessoa = str(input('Nome: '))
            break
        except (ValueError, TypeError):
            print('ERRO! Nome inválido.')
        except KeyboardInterrupt:
            print('\nERRO! Entrada cancelada pelo usuário.')
            finalizaSistema()
            sys.exit()

    while True:
        try:
            novaIdade = int(input('Idade: '))
            break
        except (ValueError, TypeError):
            print('ERRO! idade inválida.')
        except KeyboardInterrupt:
            print('\nERRO! Entrada cancelada pelo usuário.')
            finalizaSistema()
            sys.exit()

    arquivo.write(f'\n{novaPessoa}\n')
    arquivo.write(f'{novaIdade}\n')

    print('\nNovo registro!')
    print(f'{novaPessoa} adicionada com sucesso!')


def finalizaSistema():
    mensagem('Saindo do sistema... Até logo!', False)
