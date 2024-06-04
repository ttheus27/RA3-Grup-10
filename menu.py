while True:
    print("-----MENU-----\n 1.Bebidas \n 2.Lanches \n 3.Sobremesas")
    x = int(input("Ecolha um para entrar: "))
    if x == 1:
        print("-----REFRIGERENTES-----\n 1.Coca \n 2.Guarana \n-----SUCOS----- \n 1.Limao \n 2. Laranja")
        escolha = int(input("Escolha um Bebida: "))
        if escolha == 1:
            repitida = int(input("quantas vao ser?"))
            if repitida > 1:
                print("Voce add", repitida , "cocas")
            else:
                 print("Coca add no carrinho")
            break