from utils.clean import _limpar


def cabecalho(titulo):
    _limpar()
    print('-' * 35)
    print(titulo.center(35))
    print('-' * 35)


def proximo_id(lista):
    if len(lista) == 0:
        return 1
    maior = lista[0][0]
    for item in lista:
        if item[0] > maior:
            maior = item[0]
    return maior + 1


def buscar_por_id(lista, id_busca):
    for item in lista:
        if item[0] == id_busca:
            return item
    return None


def pausar():
    input('\nPressione ENTER para continuar...')
