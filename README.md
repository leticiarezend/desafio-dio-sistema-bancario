# Desafio de Programação - Sistema Bancário

Este projeto implementa um sistema bancário simples com funcionalidades de **depósito**, **saque** e **extrato**, seguindo regras de negócio definidas.

O desafio foi proposto no curso ``Dominando Python e suas Estruturas de dados`` da Digital Innovation One - DIO.


## Regras de Negócio

### Depósito
- Deve ser possível realizar **depósitos de valores positivos** na conta bancária.
- Todos os depósitos devem ser armazenados para serem exibidos posteriormente na **operação de extrato**.

### Operação de Saque
- O limite diário é de **3 saques** por dia.
- Cada saque possui um limite máximo de **R$ 500,00**.
- Caso o usuário não possua saldo suficiente, o sistema exibirá uma mensagem informando que a operação não pode ser realizada.
- Todos os saques realizados devem ser armazenados para serem exibidos na **operação de extrato**.

### Extrato
- O extrato exibirá uma lista de **todos os depósitos e saques realizados** na conta.
- No final, será exibido o saldo atual da conta.
- Todos os valores devem ser exibidos no formato **R$ xxx.xx**.

---
## Estrutura de Pastas
O projeto foi organizado da seguinte maneira 
~~~markdown
sistema_bancario/
├── README.md
├── main.py              # Programa principal
├── operacoes/           # Pacote de operações
│   ├── __init__.py
│   ├── operacoes.py
└── tests/
    ├── __init__.py       # Pacote de testes
    ├── test_operacoes.py

~~~
## Funções
## Como Executar