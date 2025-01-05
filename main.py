from operacoes.operacoes import ContaBancaria


conta = ContaBancaria()
conta.depositar(200)
print("saldo:", conta.get_saldo())
