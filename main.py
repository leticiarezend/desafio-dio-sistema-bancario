from operacoes.operacoes import ContaBancaria

operacoes = """
 [s] - sacar
 [d] - depositar
 [e] - extrato
 [q] - sair
"""
conta = ContaBancaria()
while True:
    print(operacoes)
    operacao_selecionada = input()
    if operacao_selecionada == "s":
        try:
            valor = input("Valor do Saque: ")
            valor = float(valor)
            conta.sacar(saque=valor)
        except ValueError as e:
            print(e)

    if operacao_selecionada == "d":
        try:
            valor = input("Valor do Deposito: ")
            valor = float(valor)
            conta.depositar(valor)
        except ValueError as e:
            print(e)
    if operacao_selecionada == "e":
        print("Extrato da conta:")
        saldo = conta.get_saldo()
        conta.extrato(saldo)
    if operacao_selecionada == "q":
        print("Saída efetuada!")
        break
