import os
import sys
from utils.clean import _limpar
from data.produtos import produtos

print("Produtos disponíveis:")
for produto in produtos:
    print(f"{produto['id']}: {produto['nome']} - R${produto['preco']} - Temos {produto['estoque']} em estoque")