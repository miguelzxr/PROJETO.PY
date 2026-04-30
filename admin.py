usuarios = []
senhas = []
while True:
    print("CADASTRO [1]") 
    print("BUSCAR [1]")
    print("LISTA [2]") 
    print("ALTERAR [3]")
    print("APAGAR [4]")
    print("SAIR [0]")
    opcao = input("Digite a opção: ")
    
    if opcao == 0:
        break

    elif opcao == 1:
        nome = input("Digite seu usuario: ")
        if u[0] == nome:
            print("=" * 50)
            print(u[0], ':', u[1])
            print("=" * 50)
    elif opcao == 2:
        print("=" * 50)
        for u in usuarios:
            print(u[0], u[1])
        print("=" * 50)
    elif opcao == 3:
        print("para alterar informe os dados abaixo: ")
        for posicao in range(len(usuarios)):
            if usuarios[posicao][0] == user:
                user = input("Digite seu novo usuario: ")
                senha = input("Digite sua nova senha: ")
                usuarios[posicao] = [user, [senha]]
                print("=" * 50)
                print("usuario alterado com sucesso!!!!")
                print("=" * 50)
    elif opcao == 4:
        print("para apagar informe os dados abaixo: ")
        user = input("Digite seu usuario: ")
        for posicao in range(len(usuarios)):
            if usuarios[posicao][0] == user:
                usuarios.pop(0)
                print("=" * 50)
                print("Usuario removido com sucesso!!!")
                print("=" * 50)
                break

    

