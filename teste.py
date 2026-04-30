leite = []
while True:
    print("===== MENU DE PRODUÇÃO =====")
    print("[C] Cadastrar Produção De leite")
    print("[A] Estoque do leite")
    print("[S] sair")

    opcao_3 = input("Digite sua escolha: ")

    if opcao_3 == "S":
        print("programa encerrado!!!!!!!!!!!!")
        break
    
    

    if opcao_3 == "C":
        l = float(input("Produção de leite: [L]"))
        leite.append(l)
        print("leite cadastrado")
    

    if opcao_3 == "EST":
        print('-' * 50)
        for ll in leite:
            print(ll[0])
            break
        