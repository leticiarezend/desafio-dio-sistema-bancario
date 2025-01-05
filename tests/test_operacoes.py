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


if __name__ == "__main__":
    unittest.main()
