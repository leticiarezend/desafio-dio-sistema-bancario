class ContaBancaria:
    def __init__(self, usuario, agencia, conta, saldo_inical=0.0):
        self.conta = conta
        self.agencia = agencia
        self._saldo = saldo_inical
        self._transacoes = []
        self._saques = 0
        self.limite_saques = 3
        self.usuario = usuario

    def depositar(self, deposito):
        if deposito <= 0:
            raise ValueError("Depósito deve ser maior que 0!")
        self._saldo += deposito
        self.registrar_transacao({"tipo": "Depósito", "valor": deposito})

    def registrar_transacao(self, transacao):
        self._transacoes.append(transacao)

    def sacar(self, *, saque):
        if saque <= 0:
            raise ValueError("Valor do saque deve ser maior que 0!")
        if saque >= 500:
            raise ValueError(
                "Valor limite de saque de R$ 500,00 excedido. Saque um valor inferior"
            )
        if saque > self._saldo:
            raise ValueError(
                f"Saldo insuficiente para saque de {saque}. Seu saldo atual é de {self._saldo}"
            )
        if self.limite_saques <= 0:
            raise ValueError("Limite diário de 3 saques atingido.")
        self._saldo -= saque
        self.registrar_transacao({"tipo": "Saque", "valor": saque})
        self.limite_saques -= 1

    def extrato(self, saldo, /):
        for transacao in self._transacoes:
            print(f"Transação: {transacao["tipo"]} - valor: {transacao["valor"]}")
        print("________________________")
        print(f"Saldo R${saldo}")

    def get_saldo(self):
        return self._saldo


def buscar_conta(contas, nconta):
    for conta in contas:
        if conta.conta == nconta:
            return conta
