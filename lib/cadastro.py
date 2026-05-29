from utils.helpers import cabecalho, proximo_id, pausar


def cadastrar_produto(produtos):
    cabecalho('CADASTRAR PRODUTO')

    nome = input('Nome do produto: ')
    preco = input('Preco: R$ ')
    estoque = input('Quantidade em estoque: ')

    try:
        preco = float(preco.replace(',', '.'))
        estoque = int(estoque)
    except:
        print('Valor invalido. Tente novamente.')
        pausar()
        return

    novo_id = proximo_id(produtos)
    produtos.append([novo_id, nome, preco, estoque])

    print(f'\nProduto "{nome}" cadastrado com sucesso! (ID: {novo_id})')
    pausar()


def cadastrar_cliente(clientes):
    cabecalho('CADASTRAR CLIENTE')

    nome = input('Nome: ')
    email = input('Email: ')
    cpf = input('CPF: ')

    novo_id = proximo_id(clientes)
    clientes.append([novo_id, nome, email, cpf])

    print(f'\nCliente "{nome}" cadastrado com sucesso! (ID: {novo_id})')
    pausar()


def cadastrar_pedido(pedidos, clientes, produtos):
    cabecalho('REGISTRAR PEDIDO')

    if len(clientes) == 0:
        print('Nenhum cliente cadastrado.')
        pausar()
        return

    if len(produtos) == 0:
        print('Nenhum produto disponivel.')
        pausar()
        return

    print('\nClientes:')
    for c in clientes:
        print(f'  {c[0]} - {c[1]}')

    id_cliente = input('\nID do cliente: ')

    print('\nProdutos:')
    for p in produtos:
        print(f'  {p[0]} - {p[1]} | R$ {p[2]:.2f} | Estoque: {p[3]}')

    id_produto = input('\nID do produto: ')
    quantidade = input('Quantidade: ')

    try:
        id_cliente = int(id_cliente)
        id_produto = int(id_produto)
        quantidade = int(quantidade)
    except:
        print('Valor invalido.')
        pausar()
        return

    cliente = None
    for c in clientes:
        if c[0] == id_cliente:
            cliente = c

    produto = None
    for p in produtos:
        if p[0] == id_produto:
            produto = p

    if cliente is None:
        print('Cliente nao encontrado.')
        pausar()
        return

    if produto is None:
        print('Produto nao encontrado.')
        pausar()
        return

    if quantidade > produto[3]:
        print(f'Estoque insuficiente. Disponivel: {produto[3]} unidades.')
        pausar()
        return

    total = produto[2] * quantidade
    novo_id = proximo_id(pedidos)

    pedidos.append([novo_id, cliente[0], cliente[1], produto[0], produto[1], quantidade, total])
    produto[3] -= quantidade

    print(f'\nPedido registrado com sucesso!')
    print(f'Cliente: {cliente[1]}')
    print(f'Produto: {produto[1]} x{quantidade}')
    print(f'Total: R$ {total:.2f}')
    pausar()
