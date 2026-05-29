from utils.helpers import cabecalho, pausar


def listar_produtos(produtos):
    cabecalho('PRODUTOS')

    if len(produtos) == 0:
        print('Nenhum produto cadastrado.')
        pausar()
        return

    for p in produtos:
        print(f'[{p[0]}] {p[1]} | R$ {p[2]:.2f} | Estoque: {p[3]}')

    pausar()


def listar_clientes(clientes):
    cabecalho('CLIENTES')

    if len(clientes) == 0:
        print('Nenhum cliente cadastrado.')
        pausar()
        return

    for c in clientes:
        print(f'[{c[0]}] {c[1]} | {c[2]} | {c[3]}')

    pausar()


def listar_pedidos(pedidos):
    cabecalho('PEDIDOS')

    if len(pedidos) == 0:
        print('Nenhum pedido registrado.')
        pausar()
        return

    for p in pedidos:
        print(f'[{p[0]}] {p[2]} | {p[4]} x{p[5]} | R$ {p[6]:.2f}')

    pausar()
