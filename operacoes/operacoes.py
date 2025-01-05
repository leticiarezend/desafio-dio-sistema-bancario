class ContaBancaria:
    def __init__(self, saldo_inical=0):
        self._saldo = saldo_inical
        self._transacoes = []
        self._saques = 0
        self.limite_saques = 3

    def depositar(self, deposito):
        try:
            if deposito <= 0:
                raise ValueError("Depósito deve ser maior que 0!")
            self._saldo += deposito
            self.registrar_transacao({"tipo": "Depósito", "valor": deposito})
        except ValueError as e:
            return e

    def registrar_transacao(self, transacao):
        self._transacoes.append(transacao)

    def sacar(self, saque):
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

    def get_saldo(self):
        return self._saldo
