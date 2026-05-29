# Sistema de Loja — CRUD em Python

Sistema de gerenciamento de loja desenvolvido em Python para o terminal,
como trabalho da disciplina de Lógica de Programação.

---

## Como executar

```bash
python main.py
```

Requer Python 3.10 ou superior (para o `match/case`).

---

## Estrutura do projeto

```
projetoN2/
│
├── main.py               # Ponto de entrada
│
├── data/
│   ├── produtos.py       # Lista de produtos iniciais
│   ├── clientes.py       # Lista de clientes iniciais
│   └── pedidos.py        # Lista de pedidos (inicia vazia)
│
├── lib/
│   ├── cadastro.py       # Funções de cadastro
│   ├── listagem.py       # Funções de listagem e busca
│   ├── atualizacao.py    # Funções de atualização
│   └── remocao.py        # Funções de remoção
│
└── utils/
    ├── clean.py          # Limpar tela
    ├── helpers.py        # Validações e funções auxiliares
    └── menu.py           # Menu principal e submenus
```

---

## Funcionalidades

### Produtos
- Listar todos os produtos com preço e estoque
- Buscar produto por nome (busca parcial)
- Cadastrar novo produto
- Atualizar nome, preço ou estoque
- Repor estoque rapidamente
- Remover produto

### Clientes
- Listar todos os clientes
- Buscar por nome ou CPF
- Cadastrar novo cliente (com validação de CPF e e-mail)
- Atualizar dados do cliente
- Remover cliente

### Pedidos
- Listar todos os pedidos com total
- Detalhar um pedido específico
- Registrar novo pedido (desconta estoque automaticamente)
- Remover pedido (com opção de estornar estoque)

---

## Estrutura dos dados (listas)

Todos os dados ficam em memória durante a execução, sem arquivos externos.

```python
produto  = [id, nome, preco, estoque]
cliente  = [id, nome, email, cpf]
pedido   = [id, id_cliente, nome_cliente, id_produto, nome_produto, quantidade, total]
```

---

## Tecnologias utilizadas

- Python 3.10+
- Apenas recursos da linguagem padrão
- Sem bibliotecas externas, banco de dados ou POO
