usuarios = []
animais = []
produtos_adicionais = []
lojinha = []
leite = 0
data_ret = []
animais_venda = []

ADMIN_USUARIO = "admin" 
ADMIN_SENHA = 'adm123'



while True:  #MENU PRINCIPAL
    print("[E] Entrar")
    print("[NEW] Novo usuário")
    print("[ADM] Administrador")
    print("[S] Sair")

    opcao = input("Escolha: ").upper()

    if opcao == "S":
        print("Encerrando programa")
        break

    elif opcao == "NEW":   #NOVO USUÁRIO 
        user = input("Novo usuário: ")

        if user in [u[0] for u in usuarios]:
            print("Usuário já existe.")
            continue

        senha1 = input("Senha: ")
        senha2 = input("Confirme a senha: ")

        if senha1 == senha2:
            usuarios.append([user, senha2])
            print("Usuário criado com sucesso!")
        else:
            print("As senhas não coincidem.")

    
    elif opcao == "ADM":    #ADMINISTRADOR
        user = input("Usuário: ")
        senha = input("Senha: ")

        if user != ADMIN_USUARIO or senha != ADMIN_SENHA:
            print("Acesso Negado!")

        else:
            print('Acesso Aprovado!')

      

        
            while True:    # MENU ADM 
                print("===== MENU ADM =====")
                print("[CA] Cadastrar Animal")
                print("[LISTA] Lista de Animais")
                print('[Lista_u]Lista de usúario')
                print("[AT] Atualizar Animal")
                print("[R] Remover Animal")
                print("[MP] Menu de Produtos")
                print("[V] Voltar")

                opcao_2 = input('Escolha: ').upper()

                if opcao_2 == 'V':
                    break

                
                elif opcao_2 == 'LISTA_U':    # LISTA USUÁRIOS
                    print('-' * 50)
                    for u in usuarios:
                            print(u[0], '-', u[1])
                
                
                elif opcao_2 == 'CA':   # CADASTRAR ANIMAL
                    status = input('Status: (em lactação [lac], para engorda [gorda], disponível para venda [venda])').upper()
                    
                    if status == "VENDA":
                        peso_animal = float(input("qual o peso do animal: "))
                        arroba_animal = float(input("qual o valor da arroba: "))
                        valor_animal = (peso_animal / 15) * arroba_animal #a cada 15 kg uma arroba

                        tipo = input('Tipo do animal:   (Bovino de Leite, Caprino, Ovino, Suíno/Leitão)')
                        identificacao = input('Identificação:    (brinco[A-Z]/número[0-9])')

                        animais_venda.append([tipo, identificacao, status, valor_animal])
                        print("Animal cadastrado!")
                        break
                    
                    
                    tipo = input('Tipo do animal:   (Bovino de Leite, Caprino, Ovino, Suíno/Leitão)')
                    identificacao = input('Identificação:    (brinco[A-Z]/número[0-9])')
                    animais.append([tipo, identificacao, status])
                    print("Animal cadastrado!")




                elif opcao_2 == 'LISTA':  #LISTA ANIMAIS
                    print('=' * 50)
                    for a in animais:
                        print(a[0], '-', a[1], '-', a[2])
                    print('=' * 50)

                elif opcao_2 == 'AT':  #ATUALIZAR ANIMAL
                    ident = input("Digite a identificação do animal: ")

                    for i in range(len(animais)):
                        if animais[i][1] == ident:
                            tipo = input("Novo tipo:   (Bovino de Leite, Caprino, Ovino, Suíno/Leitão)")
                            identificacao = input("Nova identificação:   (brinco[A-Z]/número[0-9])")
                            status = input("Novo status:   (em lactação, para engorda, disponível para venda")

                            peso_animal = float(input("qual o peso do animal: "))
                            arroba_animal = float(input("qual o valor da arroba: "))

                            valor_animal = (peso_animal / 15) * arroba_animal                           
                            animais[i] = [tipo, identificacao, status, valor_animal]

                            print("Atualizado com sucesso!")
                            break
                    else:
                        print("Animal não encontrado.")



                elif opcao_2 == 'R':   # REMOVER ANIMAL 
                    ident = input("Digite a identificação do animal: ")

                    for i in range(len(animais)):
                        if animais[i][1] == ident:
                            animais.pop(i)
                            print("Removido com sucesso!")
                            break
                    else:
                        print("Animal não encontrado.")

                elif opcao_2 == "MP":   # MENU PRODUTOS
                        while True:
                            print("===== MENU DE PRODUÇÃO =====")
                            print("[1] Cadastrar produção de leite")
                            print("[2] Estoque de leite")
                            print("[3] Cadastrar produto")
                            print("[4] Estoque de produtos")
                            print("[0] Voltar")

                            opcao_3 = input("Escolha: ")

                            if opcao_3 == "0":
                                break

                            elif opcao_3 == "1":  #PRODUÇÃO LEITE
                                producao = float(input("Litros de leite: "))
                                leite += producao
                                

                            elif opcao_3 == "2":  #ESTOQUE LEITE
                                print('-' * 50)
                                print(f"{leite} litros de leite")
                                continue


                                
                            elif opcao_3 == "3":  #CADASTRAR PRODUTO
                                kg = float(input('Quantidade (kg): '))
                                leite_q = float(input("qual a quantidade de leite por KG: "))
                                leite_t = kg * leite_q
                                leite -= leite_t
                                
                                if leite > leite_t:
                                    nome = input('Produto: ')
                                    valor = float(input('Valor por kg: '))
                                    estoque = float(input("Quantidade em estoque: "))                               
                                    produtos_adicionais.append([nome, kg, valor,estoque])
                                    print("Produto cadastrado!")
                                
                                else:
                                    print("estoque insuficiente de leite!!")


                            elif opcao_3 == "4":   #ESTOQUE PRODUTOS
                                print('-' * 50)
                                for p in produtos_adicionais:
                                    print(p[0], p[1],'kg(s)',p[2],'R$')

                            
                            else:
                                print("Opção inválida.")

    
    elif opcao == "E":   #CLIENTE
        user = input("Usuário: ")
        senha = input("Senha: ")
        for u in usuarios:
            if u[0] != user or u[1] != senha:
                 print("Login inválido.")  
                
            else:
                print(f"Bem-vindo, {user}!")

                while True:   #  MENU CLIENTE 
                    print("--- MENU CLIENTE ---")
                    print("[1] Ver produtos")
                    print("[2] Comprar")
                    print("[3] Agendar retirada")
                    print("[4] Lista de datas")
                    print("[0] Sair")
                
                    opcao_4 = (input('Escolha: '))

                    if opcao_4 == "0":
                        print("VOLTE SEMPRE!!!!")
                        break

                    elif opcao_4 == "1":   # VER PRODUTOS
                        print('-' * 50)
                        for p in produtos_adicionais:
                            print(p[0], p[1],'kg(s)',p[2],'R$')
                        for an in animais_venda:
                            print("tipo: ", an[0], "identificacao: ", an[1], "status: ", an[2], "valor: ", an[3])
                        
                    
                    elif opcao_4 == "2":   #COMPRAR
                        print("===== PRODUTOS =====")
                        for p in produtos_adicionais:
                                print(p[0], p[1],'kg(s)',p[2],'R$')
                        for an in animais_venda:
                            print("tipo: ", an[0], "identificacao: ", an[1], "status: ", an[2], "valor: ", an[3])

                        lojinha1 = input("Qual produto deseja comprar: [PRODUTOS[1]] | [ANIMAIS[2]] ")


                        if lojinha1 == "1":
                            for p in produtos_adicionais:
                                if p[0].upper() == lojinha1.upper():
                                    quantidade = float(input("Quantos KG: "))

                                    if quantidade <= p[3]:
                                        total = quantidade * p[2]

                                        p[3] -= quantidade

                                        print("Compra realizada com sucesso!")

                                     # NOTA FISCAL

                                        print("=" * 40)
                                        print("NOTINHA")
                                        print("=" * 40)
                                        print(f"Cliente: {user}")
                                        print("Produto:", p[0])
                                        print("Quantidade:", quantidade)
                                        print("Valor unitário: R$", p[2])
                                        print("Total: R$", total)
                                        print("=" * 40)
                        if lojinha1 == "2":
                            for an in animais_venda:
                                if an[0].upper() == animais.upper():
                                    identificacao_an = float(input("identificação do animal: "))
                                    if identificacao_an == an[1]:
                                        print("Compra realizada com sucesso!")

                                     # NOTA FISCAL
                                        print("=" * 40)
                                        print("NOTINHA DO CLIENTE")
                                        print("=" * 40)
                                        print(f"Cliente: {user}")
                                        print("Produto:", an[0])
                                        print("identificação do animal:", identificacao_an)
                                        print("Valor unitário: R$", an[3])
                                        print("Total: R$", an[opcao_3])
                                        print("=" * 40)                                        
                                        animais_venda.pop(quantidade)

                    elif opcao_4 == "3":   # AGENDAR RETIRADA =================

                        data = input("digite a data: dd/mm/aa")

                        dataFormatada = data.split("/")

                        dia = dataFormatada[0]
                        mes = dataFormatada[1]
                        ano = dataFormatada[2]

                        if dia > 31 and mes < 12 and ano >= 2026:
                            dataFormatada.append(data_ret)

                            print("Data agendada com sucesso!!")
                        else:
                            print("Data inválida!")    

                    
                    elif opcao_4 == "4":  # LISTA AGENDAMENTO
                        print("===== DATAS AGENDADAS =====")
                        
                        for d in data_ret:
                            print(d)
    else:
        print("Opção inválida.")