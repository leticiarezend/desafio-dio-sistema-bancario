import unittest
from operacoes.operacoes import ContaBancaria


class TestContaBancaria(unittest.TestCase):
    def test_deposito_100(self):
        conta = ContaBancaria()
        conta.depositar(100)
        self.assertEqual(conta.get_saldo(), 100)

    def test_deposito_negativo(self):
        conta = ContaBancaria()
        conta.depositar(-50)
        self.assertEqual(conta.get_saldo(), 0)

    def test_saque(self):
        conta = ContaBancaria(50)
        conta.sacar(20)
        self.assertEqual(conta.get_saldo(), 30)

    def test_saque_negativo(self):
        conta = ContaBancaria(100)
        with self.assertRaises(ValueError) as context:
            conta.sacar(-50)
        self.assertEqual(str(context.exception), "Valor do saque deve ser maior que 0!")
        self.assertEqual(conta.get_saldo(), 100)

    def test_saque_maior_que_saldo(self):
        conta = ContaBancaria(100)
        with self.assertRaises(ValueError) as context:
            conta.sacar(150)
        self.assertEqual(
            str(context.exception),
            f"Saldo insuficiente para saque de 150. Seu saldo atual é de {conta.get_saldo()}",
        )
        self.assertEqual(conta.get_saldo(), 100)

    def test_valor_limite(self):
        conta = ContaBancaria(100)
        with self.assertRaises(ValueError) as context:
            conta.sacar(500)
        self.assertEqual(
            str(context.exception),
            "Valor limite de saque de R$ 500,00 excedido. Saque um valor inferior",
        )
        self.assertEqual(conta.get_saldo(), 100)


if __name__ == "__main__":
    unittest.main()
