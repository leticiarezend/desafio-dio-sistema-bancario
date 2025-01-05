import unittest
from operacoes.operacoes import ContaBancaria


class TestContaBancaria(unittest.TestCase):
    def test_deposito_100(self):
        conta = ContaBancaria()
        conta.depositar(100)
        self.assertEqual(conta.get_saldo(), 100)


if __name__ == "__main__":
    unittest.main()
