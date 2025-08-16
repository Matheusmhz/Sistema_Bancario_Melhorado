# Criando um Sistema Bancário Melhorado com Python

Este projeto é uma versão aprimorada de um sistema bancário simples, criado com o objetivo de praticar e aplicar conceitos de **funções em Python**, **modularização**, **validação de dados**, e **estruturas de controle**.

A versão 2 do sistema permite criar usuários, abrir contas, realizar depósitos, saques, consultar extrato e listar todas as contas cadastradas.

---

## Funcionalidades


- ✅ **Criar usuário com CPF único**
- ✅ **Criar conta corrente vinculada a um usuário existente**
- ✅ **Realizar depósitos e saques com validações**
- ✅ **Emitir extrato bancário**
- ✅ **Listar contas existentes**
- ✅ **Controle de limite de saque diário (valor e quantidade)**
- ✅ **Menu interativo via terminal**
- ✅ **Código organizado com funções puras e boas práticas**


---

## Tecnologias utilizadas

- Linguagem: **Python 3.11+**
- Execução: Terminal (modo interativo)
- Estrutura: Código 100% modularizado com funções

---

## Organização do Código

| Função             | Responsabilidade                                                        |
|--------------------|---------------------------------------------------------------------------|
| `menu()`           | Exibe o menu interativo                                                  |
| `depositar()`      | Realiza depósitos (só aceita valores positivos, args por posição)        |
| `sacar()`          | Realiza saques com limite diário de valor e quantidade                   |
| `exibir_extrato()` | Exibe o histórico de operações e o saldo atual                           |
| `criar_usuario()`  | Cadastra um novo usuário com CPF único                                   |
| `filtrar_usuario()`| Busca um usuário na lista com base no CPF                                |
| `criar_conta()`    | Cria uma nova conta vinculada a um usuário existente                     |
| `listar_contas()`  | Lista todas as contas cadastradas                                        |

---
