usuarios = []
animais = []
leite = []

ADMIN_USUARIO = "ADMIN"
ADMIN_SENHA = 'ADM123'

while True:
    print("===== MENU =====")
    print("[E] Entrar")
    print("[NEW] Novo usuário")
    print('[LISTA]Lista de usuários')
    print("[ADM] Admin")
    print("[S] Sair")

    opcao = input("Escolha: ").upper()

    if opcao == "S":
        print("OBRIGADO, VOLTE SEMPRE!!")
        break

    elif opcao == "NEW":
        user = input("Novo usuário: ")

        if user in usuarios:
            print(" Usuário já existe.")
            continue

        senha1 = input("Senha: ")
        senha2 = input("Confirme a senha: ")

        if senha1 == senha2:
            print('usúario criado')

        usuarios.append([user, senha2 ])

    elif opcao == 'LISTA':
        print('-' * 50)
        for u in usuarios:
            print(u[0], '-' , u[1])

    elif opcao == "E":
        user = input("Usuário: ")
        senha = input("Senha: ")

        for u in usuarios:
            if u[0] == user and u[1] == senha:
                print(f"Bem-vindo, {user}!")
                break
        else:
            print("Login inválido.")

    elif opcao == "ADM":
        user = input("Usuário: ")
        senha = input("Senha: ")

        if user == ADMIN_USUARIO and senha == ADMIN_SENHA:
            print(" Acesso liberado")


        print("===== MENU ADM =====")
        print("[CA] Cadastrar Animal")
        print('[LISTA]Lista de Animais')
        print("[AT]Atualizar Animais")
        print('[R]Remover Aniamis')
        print("[S] Sair")
        print("[P] Painel de produção")
        
        opcao_2 = input('Digite sua escolha: ').upper()

        if opcao_2 == 's':
            print("Encerrando programa")
            break

        elif opcao_2 == 'CA':
            tipo_do_animal = input('Digite o tipo do Animal:   (Bovino de Leite, Caprino, Ovino, Suíno/Leitão)')
            identificação = input('Digite qual a identificação do animal:   (brinco[A-Z]/número[0-9])')
            status = input('Digite o status do animal:   (em lactação, para engorda, disponível para venda)')
            
            print('Animais cadastrados com sucesso! ')

            animais.append([tipo_do_animal, identificação , status] )
            continue
           
        elif opcao_2 == 'LISTA':
             print('-' * 50)
             for a in animais:
                 print(a[0], '-' , a[1], '-' , a[2])
                 continue

        
        elif opcao_2 == 'AT':
               print("para alterar as informações informe os dados abaixo: ")
               for posicao in range(len(animais)):
                    if animais[posicao][0] == animais:
                        tipo_do_animal = input("Digite o novo tipo de animal: ")
                        identificação = input("Digite a nova identificação: ")
                        status = input("Digite o novo status: ")
                
                        animais[posicao] = [tipo_do_animal, identificação , status]
                        print("=" * 50)
                        print("Informações alteradas com sucesso!")
                        print("=" * 50)
                        continue

        elif opcao_2 == 'R':
             print("para apagar informe os dados abaixo: ")
        identificação = input("Digite sua identifição: ")
        for posicao in range(len(animais)):
            if animais[posicao][1] == identificação:
                animais.pop(1)
                print("=" * 50)
                print("Usuario removido com sucesso!!!")
                print("=" * 50)
    
        if opcao_2 == "P":
            print("===== MENU DE PRODUÇÃO =====")
            print("[1] Cadastrar Produção De leite")
            print("[2] Estoque do leite")


            opcao_3 = input("Digite sua escolha: ")

            if opcao_3 == 0:
                break

            elif opcao_3 == 1:
                l = float(input("Produção de leite: [L]"))
                leite.append(l)
                continue
            elif opcao_3 == 2:
                print('-' * 50)
                for u in usuarios:
                    print(u[0], 'litros de leite')
                    continue

            

