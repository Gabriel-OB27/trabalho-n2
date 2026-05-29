from utils.helpers import cabecalho, buscar_por_id, pausar


def atualizar_produto(produtos):
    cabecalho('ATUALIZAR PRODUTO')

    if len(produtos) == 0:
        print('Nenhum produto cadastrado.')
        pausar()
        return

    for p in produtos:
        print(f'[{p[0]}] {p[1]} | R$ {p[2]:.2f} | Estoque: {p[3]}')

    try:
        id_produto = int(input('\nID do produto: '))
    except:
        print('ID invalido.')
        pausar()
        return

    produto = buscar_por_id(produtos, id_produto)

    if produto is None:
        print('Produto nao encontrado.')
        pausar()
        return

    print(f'\nEditando: {produto[1]}')
    print('Deixe em branco para nao alterar.\n')

    novo_nome = input(f'Novo nome [{produto[1]}]: ')
    novo_preco = input(f'Novo preco [{produto[2]}]: ')
    novo_estoque = input(f'Novo estoque [{produto[3]}]: ')

    if novo_nome != '':
        produto[1] = novo_nome

    if novo_preco != '':
        try:
            produto[2] = float(novo_preco.replace(',', '.'))
        except:
            print('Preco invalido, mantido o anterior.')

    if novo_estoque != '':
        try:
            produto[3] = int(novo_estoque)
        except:
            print('Estoque invalido, mantido o anterior.')

    print('\nProduto atualizado com sucesso!')
    pausar()


def atualizar_cliente(clientes):
    cabecalho('ATUALIZAR CLIENTE')

    if len(clientes) == 0:
        print('Nenhum cliente cadastrado.')
        pausar()
        return

    for c in clientes:
        print(f'[{c[0]}] {c[1]} | {c[2]} | {c[3]}')

    try:
        id_cliente = int(input('\nID do cliente: '))
    except:
        print('ID invalido.')
        pausar()
        return

    cliente = buscar_por_id(clientes, id_cliente)

    if cliente is None:
        print('Cliente nao encontrado.')
        pausar()
        return

    print(f'\nEditando: {cliente[1]}')
    print('Deixe em branco para nao alterar.\n')

    novo_nome = input(f'Novo nome [{cliente[1]}]: ')
    novo_email = input(f'Novo email [{cliente[2]}]: ')
    novo_cpf = input(f'Novo CPF [{cliente[3]}]: ')

    if novo_nome != '':
        cliente[1] = novo_nome
    if novo_email != '':
        cliente[2] = novo_email
    if novo_cpf != '':
        cliente[3] = novo_cpf

    print('\nCliente atualizado com sucesso!')
    pausar()
