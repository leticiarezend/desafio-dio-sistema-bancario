class ContaBancaria:
    def __init__(self, saldo_inical=0):
        self._saldo = saldo_inical
        self._transacoes = []
        self._saques = 0

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

    def get_saldo(self):
        return self._saldo
