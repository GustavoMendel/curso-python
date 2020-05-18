import time
import sistema

opcao = 0
while opcao != 3:
    opcao = sistema.recebeOpcao()
    if opcao == 1:
        sistema.lerPessoas()

    elif opcao == 2:
        sistema.adicionaPessoas()

    time.sleep(1.2)

sistema.finalizaSistema()
