file = open("Menu.txt", "r+", encoding="utf-8")
cardapio = file.readlines()

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

bebidas = []
entradas = []
pratos = []
sobremesas = []

for i, line in enumerate(cardapio):
    if i <= 4:
        context = line.split()
        bebidas.append(Item(context[0].replace("-", " "), float(context[1])))
    elif 4 < i <= 9:
        context = line.split()
        entradas.append(Item(context[0].replace("-", " "), float(context[1])))
    elif 9 < i <= 14:
        context = line.split()
        pratos.append(Item(context[0].replace("-", " "), float(context[1])))
    else:
        context = line.split()
        sobremesas.append(Item(context[0].replace("-", " "), float(context[1])))

while(True):
    print("1) Adicionar item ao cardápio")
    print("2) Excluir item do cardápio")
    print("3) Alterar item do cardápio")
    print("4) Buscar item do cardápio")
    print("5) Listar todos os itens do cardápio")
    print("0) Sair")
    
    choice = int(input("Escolha uma opção:\n"))
    
    if choice == 1:
        while(True):
            print("1) Bebida")
            print("2) Entrada")
            print("3) Prato Principal")
            print("4) Sobremesa")
            print("0) Sair")
            
            subChoice = int(input("Escolha uma opção:\n"))
            
            if subChoice == 1:
                bebidas.append(Item(str(input("Digite o nome da bebida:\n")), float(input("Digite o valor da bebida:\n"))))
                print("Bebida Adicionada!")
                break
            elif subChoice == 2:
                entradas.append(Item(str("Digite o nome da entrada:\n")), float(input("Digite o valor da entrada:\n")))
                print("Entrada Adicionada!")
                break
            elif subChoice == 3:
                pratos.append(Item(str(input("Digite o nome do prato:\n")), float(input("Digite o valor do prato:\n"))))
                print("Prato Adicionado!")
                break
            elif subChoice == 4:
                sobremesas.append(Item(str(input("Digite o nome da sobremesa:\n")), float(input("Digite o valor da sobremesa"))))
                print("Sobremesa Adicionada!")
                break
            elif subChoice == 0:
                break
            else:
                print("Opção inválida")
    elif choice == 2:
        while(True):
            print("1) Bebida")
            print("2) Entrada")
            print("3) Prato Principal")
            print("4) Sobremesa")
            print("0) Sair")
            
            subChoice = int(input("Eschola uma opção"))
            
            if subChoice == 1:
                name = str(input("Digite o nome da bebida:\n"))
                for bebida in bebidas:
                    if bebida.name == name:
                        del bebida
                        print("Bebida excluída")
                        break
                    else:
                        print("Bebida não encontrada")
            elif subChoice == 2:
                name = str(input("Digite o nome da entrada:\n"))
                for entrada in entradas:
                    if entrada.name == name:
                        del entrada
                        break
                    else:
                        print("Entrada não encontrada")
            elif subChoice == 3:
                name = str(input("Digite o nome do prato:\n"))
                for prato in pratos:
                    if prato.name == name:
                        del prato
                        print("Prato excluído")
                        break
                    else:
                        print("Prato não encontrado")
            elif subChoice == 4:
                name = str(input("Digite o nome da sobremesa:\n"))
                for sobremesa in sobremesas:
                    if sobremesa.name == name:
                        del sobremesa
                        print("Sobremesa excluída")
                        break
                    else:
                        print("Sobremesa não encontrada")
            elif subChoice == 0:
                break
            else:
                print("Opção inválida")
    elif choice == 3:
        while(True):
            print("1) Bebida")
            print("2) Entrada")
            print("3) Prato Principal")
            print("4) Sobremesa")
            print("0) Sair")
            
            subChoice = int(input("Eschola uma opção:\n"))
            
            if subChoice == 1:
                str(input("Digite o nome da bebida:\n"))
                for bebida in bebidas:
                    if bebida.name == name:
                        while(True):
                            print("O que você quer alterar:")
                            print("1) Nome")
                            print("2) Valor")
                            print("0) Sair")
                            
                            subSubChoice = int(input("Escolha uma opção:\n"))
                            
                            if subSubChoice == 1:
                                bebida.name = str(input("Digite o novo nome:\n"))
                                print("Bebida alterada!")
                                break
                            elif subSubChoice == 2:
                                bebida.value == int(input("Digite o novo valor:\n"))
                                print("Bebida alterada!")
                                break
        