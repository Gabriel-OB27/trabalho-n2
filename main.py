import os
import sys
from time import sleep
from utils.clean import _limpar
from data.produtos import produtos
from utils.menu import _menu, _sobre


_limpar()
sleep(2)
print(f"{'-'*30}\n{'BEM-VINDO A NOSSA LOJA':^30}\n{'-'*30}")

_menu()


