from operacoes.operacoes import ContaBancaria, buscar_conta
from usuario.usuario import criar_usuario, filtrar_usuario

operacoes = """
 [nc] - nova conta
 [nu] - novo usuario
 [lc] - listar contas
 [s] - sacar
 [d] - depositar
 [e] - extrato
 [q] - sair
"""
usuarios = []
contas = []

while True:
    print(operacoes)
    operacao_selecionada = input()
    if operacao_selecionada == "s":
        try:
            nconta = input("Insira o numero da conta: ")
            conta = buscar_conta(contas, int(nconta))
            valor = input("Valor do Saque: ")
            valor = float(valor)
            conta.sacar(saque=valor)
        except ValueError as e:
            print(e)

    if operacao_selecionada == "d":
        try:
            nconta = input("Insira o numero da conta: ")
            conta = buscar_conta(contas, int(nconta))
            valor = input("Valor do Deposito: ")
            valor = float(valor)
            conta.depositar(valor)
        except ValueError as e:
            print(e)
    if operacao_selecionada == "nu":
        print("=== Cadastro Novo Usuário ===")
        cpf = input("Insira o CPF do usuario: ")
        usuario_existente = filtrar_usuario(usuarios, cpf)
        if usuario_existente:
            print("Cpf já cadastrado")
        else:
            nome = input("Insira o nome do usuario: ")
            data_nascimento = input(
                "Insira a data de nascimento do usuario (dd/mm/aaaa): "
            )
            endereco = input("Insira o endereco do usuario: ")
            criar_usuario(usuarios, cpf, nome, data_nascimento, endereco)
            print(" Usuário cadastrado com Sucesso!\n=============\n")
    if operacao_selecionada == "nc":
        print("=== Criar Nova Conta ===")
        cpf = input("Insira o CPF do usuario: ")
        usuario = filtrar_usuario(usuarios, cpf)
        if usuario:
            nconta = len(contas) + 1
            ag = "0083"
            conta = ContaBancaria(usuario=usuario, agencia=ag, conta=nconta)
            print(" Conta criada com Sucesso!\n=============\n")
            print(
                f"Agência : {conta.agencia}\nTitular: {conta.usuario.nome}\nConta: {nconta}"
            )
            contas.append(conta)
        else:
            print("Nenhum usuario cadastrado com esse CPF!")
    if operacao_selecionada == "e":
        print("Extrato da conta:")
        nconta = input("Insira o numero da conta: ")
        conta = buscar_conta(contas, int(nconta))
        saldo = conta.get_saldo()
        conta.extrato(saldo)
    if operacao_selecionada == "q":
        print("Saída efetuada!")
        break
