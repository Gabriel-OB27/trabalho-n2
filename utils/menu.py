from utils.clean import _limpar
from utils.helpers import cabecalho, pausar

from data.produtos import produtos
from data.clientes import clientes
from data.pedidos import pedidos

from lib.cadastro import cadastrar_produto, cadastrar_cliente, cadastrar_pedido
from lib.listagem import listar_produtos, listar_clientes, listar_pedidos
from lib.atualizacao import atualizar_produto, atualizar_cliente
from lib.remocao import remover_produto, remover_cliente, remover_pedido


def _menu_produtos():
    while True:
        cabecalho('PRODUTOS')
        print('1 - Listar produtos')
        print('2 - Cadastrar produto')
        print('3 - Atualizar produto')
        print('4 - Remover produto')
        print('0 - Voltar')

        opcao = input('\nOpcao: ')

        match opcao:
            case '1':
                listar_produtos(produtos)
            case '2':
                cadastrar_produto(produtos)
            case '3':
                atualizar_produto(produtos)
            case '4':
                remover_produto(produtos)
            case '0':
                break
            case _:
                print('Opcao invalida.')
                pausar()


def _menu_clientes():
    while True:
        cabecalho('CLIENTES')
        print('1 - Listar clientes')
        print('2 - Cadastrar cliente')
        print('3 - Atualizar cliente')
        print('4 - Remover cliente')
        print('0 - Voltar')

        opcao = input('\nOpcao: ')

        match opcao:
            case '1':
                listar_clientes(clientes)
            case '2':
                cadastrar_cliente(clientes)
            case '3':
                atualizar_cliente(clientes)
            case '4':
                remover_cliente(clientes)
            case '0':
                break
            case _:
                print('Opcao invalida.')
                pausar()


def _menu_pedidos():
    while True:
        cabecalho('PEDIDOS')
        print('1 - Listar pedidos')
        print('2 - Registrar pedido')
        print('3 - Remover pedido')
        print('0 - Voltar')

        opcao = input('\nOpcao: ')

        match opcao:
            case '1':
                listar_pedidos(pedidos)
            case '2':
                cadastrar_pedido(pedidos, clientes, produtos)
            case '3':
                remover_pedido(pedidos, produtos)
            case '0':
                break
            case _:
                print('Opcao invalida.')
                pausar()


def _sobre():
    cabecalho('SOBRE NOS')
    print('Loja de tecnologia especializada em')
    print('perifericos e componentes para computadores.')
    print('\nSistema desenvolvido para fins academicos.')
    print('Disciplina: Logica de Programacao')
    pausar()


def _menu():
    while True:
        cabecalho('MENU PRINCIPAL')
        print('1 - Produtos')
        print('2 - Clientes')
        print('3 - Pedidos')
        print('4 - Sobre nos')
        print('0 - Sair')

        opcao = input('\nOpcao: ')

        match opcao:
            case '1':
                _menu_produtos()
            case '2':
                _menu_clientes()
            case '3':
                _menu_pedidos()
            case '4':
                _sobre()
            case '0':
                _limpar()
                print('Ate logo!')
                break
            case _:
                print('Opcao invalida.')
                pausar()
