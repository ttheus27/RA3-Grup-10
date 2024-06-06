import time

file = open("./menu.txt", "r+", encoding="utf-8")
content = file.readlines()

class menuItem:
    def __init__(self, category, subCategory, name, value):
        self.category = category
        self.subCategory = subCategory
        self.name = name
        self.value = value


menuContents = []
for line in content:
    context = line.split()
    menuContents.append(menuItem(context[0].replace("-", " "), context[1].replace("-", " "), context[2].replace("-", " "), float(context[3])))

while(True):
    print("1) Adicionar itens ao cardápio")
    print("2) Excluir itens do cardápio")
    print("3) Alterar itens do cardápio")
    print("4) Buscar itens do cardápio")
    print("5) Listar todos os itens do cardápio")
    print("0) Sair\n")

    choice = int(input("Eschola uma opção:\n"))
    print()

    if choice == 1:
        temp = {item.category for item in menuContents}
        while(True):
            for i, item in enumerate(temp):
                print(f"{i + 1}) {item}")
            print("0) Sair\n")

            catChoice = int(input("Escholha uma categoria:\n"))
            print()

            if catChoice == 0:
                break

            if not (selectedCategory := next((item for index, item in enumerate(temp) if index + 1 == catChoice), None)):
                print("Opção inválida\n")
                time.sleep(.5)
                continue

            tempSub = {item.subCategory for item in menuContents if item.category == selectedCategory}
            while(True):
                for i, item in enumerate(tempSub):
                    print(f"{i + 1}) {item}")
                print("0) Sair\n")

                subCatChoice = int(input("Eschola uma sub-categoria:\n"))
                print()

                if subCatChoice == 0:
                    break

                if not (selectedSubCategory := next((item for index, item in enumerate(tempSub) if index + 1 == subCatChoice), None)):
                    print("Opção inválida\n")
                    time.sleep(1)
                    continue

                veri = [item.name for item in menuContents]
                while(True):
                    name = str(input("Digite o nome do novo item:\n"))
                    if name in veri:
                        print("Nome já existente!")
                        time.sleep(1)
                    else:
                        menuContents.append(menuItem(selectedCategory, selectedSubCategory, name, float(input("Digite o valor do novo item:\n"))))
                        print("Item adicionado com sucesso!\n")
                        time.sleep(1)
                        break

    elif choice == 2:
        temp = {item.category for item in menuContents}
        while(True):
            for i, item in enumerate(temp):
                print(f"{i + 1}) {item}")
            print("0) Sair\n")

            catChoice = int(input("Escolha uma categoria:\n"))
            print()

            if catChoice == 0:
                break

            if not (selectedCategory := next((item for index, item in enumerate(temp) if index + 1 == catChoice), None)):
                print("Opção inválida\n")
                time.sleep(.5)
                continue

            tempSub = {item.subCategory for item in menuContents if item.category == selectedCategory}
            while (True):
                for i, item in enumerate(tempSub):
                    print(f"{i + 1}) {item}")
                print("0) Sair\n")

                subCatChoice = int(input("Eschola uma sub-categoria:\n"))
                print()

                if subCatChoice == 0:
                    break

                if not (selectedSubCategory := next((item for index, item in enumerate(tempSub) if index + 1 == subCatChoice), None)):
                    print("Opção inválida\n")
                    time.sleep(1)
                    continue

                veri = [item for item in menuContents if item.category == selectedCategory and item.subCategory == selectedSubCategory]
                while(True):
                    for i, item in enumerate(veri):
                        print(f"{i + 1}) Nome: {item.name} | Valor: R${item.value}")
                    print("0) Sair\n")

                    contextItem = int(input("Escolha uma opção:\n"))
                    print()
                    if contextItem == 0:
                        break
                    if not (contextItem := next((item for index, item in enumerate(veri) if index + 1 == contextItem), None)):
                        print("Opção Inválida\n")
                        time.sleep(1)
                        continue

                    menuContents = [item for item in menuContents if item != contextItem]
                    print("Item excluído com sucesso!\n")
                    time.sleep(1)
                    break

    elif choice == 3:
        temp = {item.category for item in menuContents}
        while (True):
            for i, item in enumerate(temp):
                print(f"{i + 1}) {item}")
            print("0) Sair\n")

            catChoice = int(input("Escolha uma categoria:\n"))
            print()

            if catChoice == 0:
                break

            if not (selectedCategory := next((item for index, item in enumerate(temp) if index + 1 == catChoice), None)):
                print("Opção inválida\n")
                time.sleep(.5)
                continue

            tempSub = {item.subCategory for item in menuContents if item.category == selectedCategory}
            while (True):
                for i, item in enumerate(tempSub):
                    print(f"{i + 1}) {item}")
                print("0) Sair\n")

                subCatChoice = int(input("Eschola uma sub-categoria:\n"))
                print()

                if subCatChoice == 0:
                    break

                if not (selectedSubCategory := next((item for index, item in enumerate(tempSub) if index + 1 == subCatChoice), None)):
                    print("Opção inválida\n")
                    time.sleep(1)
                    continue

                veri = [item for item in menuContents if item.category == selectedCategory and item.subCategory == selectedSubCategory]
                while(True):
                    for i, item in enumerate(veri):
                        print(f"{i + 1}) Nome: {item.name} | Valor: R${item.value}")
                    print("0) Sair\n")

                    contextItem = int(input("Escolha uma opção:\n"))
                    print()
                    if contextItem == 0:
                        break
                    if not (contextItem := next((item for index, item in enumerate(veri) if index + 1 == contextItem), None)):
                        print("Opção inválida\n")
                        time.sleep(1)
                        continue

                    while(True):
                        print("1) Deseja alterar o nome do item")
                        print("2) Deseja alterar o valor do item")
                        print("0) Sair\n")

                        altChoice = int(input("Escolha uma opção:\n"))
                        print()

                        if altChoice == 0:
                            break

                        if altChoice == 1:
                            contextItem.name = str(input("Digite o novo nome do item:\n"))
                            print("Nome alterado com sucesso!\n")
                            time.sleep(1)
                        elif altChoice == 2:
                            contextItem.value = float(input("Digite o novo valor do item:\n"))
                            print("Valor alterado com sucesso!\n")
                            time.sleep(1)
                        else:
                            print("Opção inválida\n")
                            time.sleep(1)

    elif choice == 4:
        while(True):
            name = str(input("Digite o nome do item que deseja encontrar:\n"))
            if not (contextItem := next((item for item in menuContents if item.name == name), None)):
                print("Item não encontrado ou não existente")
                time.sleep(1)
                continue

            print(f"Categoria: {contextItem.category} | Sub-Categoria: {contextItem.subCategory} | Nome: {contextItem.name} | Valor: R${contextItem.value}\n")
            time.sleep(1)

            while(True):
                print("1) Continuar")
                print("0) Sair\n")

                flagShould = int(input("Escolha uma opção:\n"))

                if flagShould == 1 or flagShould == 0:
                    break

            if not flagShould:
                print()
                break

    elif choice == 5:
        sortedMenu = sorted(menuContents, key=lambda x: (x.category, x.subCategory))
        tempCat = sortedMenu[0].category
        for item in sortedMenu:
            if item.category != tempCat:
                print()

            print(f"Categoria: {item.category} | Sub-Categoria: {item.subCategory} | Nome: {item.name} | Valor: {item.value}")
            tempCat = item.category
        print()
    elif choice == 0:
        break
    else:
        print("Opção inválida\n")
        time.sleep(1)

file.seek(0)
file.truncate()

for i, item in enumerate(menuContents):
        if i + 1 == len(menuContents):
            file.write(f"{item.category.replace(' ', '-')} {item.subCategory.replace(' ', '-')} {item.name.replace(' ', '-')} {item.value}")
        else:
            file.write(f"{item.category.replace(' ', '-')} {item.subCategory.replace(' ', '-')} {item.name.replace(' ', '-')} {item.value}\n")

file.close()