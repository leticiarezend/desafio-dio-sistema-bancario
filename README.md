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
## Classe ContaBancaria
-> A classe ContaBancaria localizada em ``sistema_bancario/operacoes/operacoes.py`` engloba metodos e atributos que são exigidos nas regras de negócio.
- ``_saldo``: Saldo da conta.
- ``_transacoes``: Histórico de transações com tipo e valor para exibir no extrato.
- ``limite_saques``: Atributo para verificar se o limite diário de 3 saques foi excedido.
---
Os métodos são:
### ``depositar``:
- **Descrição**: Realiza um depósito na conta bancária.
- **Parâmetros**:
  - `deposito` (float): O valor do depósito (deve ser positivo).
- **Comportamento**:
  - Adiciona o valor ao saldo da conta.
  - Armazena a transação na lista de operações para o extrato.


### ``sacar``:
- **Descrição**: Realiza um saque na conta bancária.
- **Parâmetros**:
  - `saque` (float): O valor do saque.
- **Comportamento**:
  - Verifica se o saldo é suficiente para o saque.
  - Verifica se o limite diário de saques ou o valor por saque foi excedido.
  - Deduz o valor do saldo caso a operação seja bem-sucedida.
  - Armazena a transação na lista de operações para o extrato.

### ``extrato`` :
- **Descrição**: Exibir lista de operações e saldo.
- **Parâmetros**:
  - Não possui parametros.
- **Comportamento**:
   - Percorre cada transação da lista de operações e exibe tipo e valor.
   - Exibe saldo final
### ``registrar_transacao`` :
- **Descrição**: Armazena transação no atributo de operações.
- **Parâmetros**:
  - ``transacao`` (dict):  Dicionário contendo o tipo e o valor da transação.
- **Comportamento**:
   - Adiciona a transação ao final da lista de operações.
   
