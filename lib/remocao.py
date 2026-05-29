from utils.helpers import cabecalho, buscar_por_id, pausar


def remover_produto(produtos):
    cabecalho('REMOVER PRODUTO')

    if len(produtos) == 0:
        print('Nenhum produto cadastrado.')
        pausar()
        return

    for p in produtos:
        print(f'[{p[0]}] {p[1]} | R$ {p[2]:.2f} | Estoque: {p[3]}')

    try:
        id_produto = int(input('\nID do produto a remover: '))
    except:
        print('ID invalido.')
        pausar()
        return

    produto = buscar_por_id(produtos, id_produto)

    if produto is None:
        print('Produto nao encontrado.')
        pausar()
        return

    confirmar = input(f'Remover "{produto[1]}"? (s/n): ').lower()

    if confirmar == 's':
        produtos.remove(produto)
        print('Produto removido com sucesso!')
    else:
        print('Operacao cancelada.')

    pausar()


def remover_cliente(clientes):
    cabecalho('REMOVER CLIENTE')

    if len(clientes) == 0:
        print('Nenhum cliente cadastrado.')
        pausar()
        return

    for c in clientes:
        print(f'[{c[0]}] {c[1]} | {c[2]} | {c[3]}')

    try:
        id_cliente = int(input('\nID do cliente a remover: '))
    except:
        print('ID invalido.')
        pausar()
        return

    cliente = buscar_por_id(clientes, id_cliente)

    if cliente is None:
        print('Cliente nao encontrado.')
        pausar()
        return

    confirmar = input(f'Remover "{cliente[1]}"? (s/n): ').lower()

    if confirmar == 's':
        clientes.remove(cliente)
        print('Cliente removido com sucesso!')
    else:
        print('Operacao cancelada.')

    pausar()


def remover_pedido(pedidos, produtos):
    cabecalho('REMOVER PEDIDO')

    if len(pedidos) == 0:
        print('Nenhum pedido registrado.')
        pausar()
        return

    for p in pedidos:
        print(f'[{p[0]}] {p[2]} | {p[4]} x{p[5]} | R$ {p[6]:.2f}')

    try:
        id_pedido = int(input('\nID do pedido a remover: '))
    except:
        print('ID invalido.')
        pausar()
        return

    pedido = buscar_por_id(pedidos, id_pedido)

    if pedido is None:
        print('Pedido nao encontrado.')
        pausar()
        return

    confirmar = input(f'Remover pedido #{pedido[0]}? (s/n): ').lower()

    if confirmar == 's':
        produto = buscar_por_id(produtos, pedido[3])
        if produto is not None:
            produto[3] += pedido[5]
        pedidos.remove(pedido)
        print('Pedido removido e estoque estornado.')
    else:
        print('Operacao cancelada.')

    pausar()
