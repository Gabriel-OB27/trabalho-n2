def _menu():
    from main import _limpar
    from data.produtos import produtos
    from data.clientes import clientes
    
    while True:
        _limpar()
        print(f"{'-'*30}\n{'MENU PRINCIPAL':^30}\n{'-'*30}")
        print(f"Para iniciar, selecione uma opção:")
        print("1 - Ver produtos disponíveis")
        print("2 - Ver clientes cadastrados")
        print("3 - Sobre nós")
        print("0 - Sair do sistema")
        opcao = input("\nDigite o número da opção desejada: ")
        
        match opcao:
            case "1":
                _limpar()
                print(f"{'-'*30}\n{'PRODUTOS DISPONÍVEIS':^30}\n{'-'*30}")
                for produto in produtos:
                    print(f"{produto['id']}: {produto['nome']} - R${produto['preco']:.2f} - Estoque: {produto['estoque']}")
                input("\nPressione ENTER para voltar ao menu...")
                
            case "2":
                _limpar()
                print(f"{'-'*30}\n{'CLIENTES CADASTRADOS':^30}\n{'-'*30}")
                for cliente in clientes:
                    print(f"{cliente['id']}: {cliente['nome']} - {cliente['email']} - CPF: {cliente['cpf']}")
                input("\nPressione ENTER para voltar ao menu...")
                
            case "3":
                _limpar()
                _sobre()
                input("\nPressione ENTER para voltar ao menu...")
                
            case "0":
                _limpar()
                print("Obrigado por usar nosso sistema! Até logo!")
                break
                
            case _:
                print("Opção inválida! Digite um número entre 0 e 3.")
                input("Pressione ENTER para tentar novamente...")


def _sobre():
    print(f"{'-'*30}\n{'SOBRE NÓS':^30}\n{'-'*30}")
    print('''Somos uma loja de tecnologia especializada em periféricos e componentes para computadores.
Oferecemos uma ampla variedade de produtos, desde fones de ouvido Bluetooth até
placas de vídeo de última geração. Nossa missão é fornecer aos nossos clientes os melhores
produtos com preços competitivos e um atendimento excepcional. Explore nosso catálogo e
encontre o que você precisa para aprimorar sua experiência tecnológica!''')


if __name__ == "__main__":
    _menu()