usuarios = []
animais = []
produtos_adicionais = []
lojinha = []
leite = 0
data_retirada = []
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
                            print("usuario: ", u[0], '-', "senha: ", u[1])
                
                
                elif opcao_2 == 'CA':   # CADASTRAR ANIMAL
                    status = input('Status: (em lactação [lac], para engorda [gorda], disponível para venda [venda]): ').upper()
                    
                    if status == "VENDA":
                        peso_animal = float(input("qual o peso do animal: "))
                        arroba_animal = float(input("qual o valor da arroba: "))
                        valor_animal = (peso_animal / 15) * arroba_animal #a cada 15 kg uma arroba

                        tipo = input('Tipo do animal:   (Bovino de Leite, Caprino, Ovino, Suíno/Leitão): ')
                        identificacao = input('Identificação:    (brinco[A-Z]/número[0-9]): ')

                        animais_venda.append([tipo, identificacao, status, valor_animal])
                        print("Animal cadastrado!")
                        continue
                      
                    
                    
                    tipo = input('Tipo do animal:   (Bovino de Leite, Caprino, Ovino, Suíno/Leitão): ')
                    identificacao = input('Identificação:    (brinco[A-Z]/número[0-9]): ')

                    animais.append([tipo, identificacao, status])
                    print("Animal cadastrado!")




                elif opcao_2 == 'LISTA':  #LISTA ANIMAIS
                    print('=' * 50)
                    for av in animais_venda:
                        print(av[0], '-', av[1], '-', av[2])
                    print('=' * 50)

                    for a in animais:
                        print(a[0], '-', a[1], '-', a[2])
                    print('=' * 50)

                  

                elif opcao_2 == 'AT':  #ATUALIZAR ANIMAL
                    ident = input("Digite a identificação do animal: ")

                    for i in range(len(animais)):
                        if animais[i][1] == ident:
                            tipo = input("Novo tipo:   (Bovino de Leite, Caprino, Ovino, Suíno/Leitão): ")
                            identificacao = input("Nova identificação:   (brinco[A-Z]/número[0-9]): ")
                            status = input("Novo status:   (em lactação, para engorda, disponível para venda: ")

                            peso_animal = float(input("qual o peso do animal: "))
                            arroba_animal = float(input("qual o valor da arroba: "))

                            valor_animal = (peso_animal / 15) * arroba_animal                           
                            animais[i] = [tipo, identificacao, status, valor_animal]

                            print("Atualizado com sucesso!")
                            continue
                        else:
                            print("Animal não encontrado.")
                            

                    for iv in range(len(animais_venda)):        
                        if animais_venda[iv][1] == ident:
                            tipo = input("Novo tipo:   (Bovino de Leite, Caprino, Ovino, Suíno/Leitão): ")
                            identificacao = input("Nova identificação:   (brinco[A-Z]/número[0-9]): ")
                            status = input("Novo status:   (em lactação, para engorda, disponível para venda: ")

                            peso_animal = float(input("qual o peso do animal: "))
                            arroba_animal = float(input("qual o valor da arroba: "))

                            valor_animal = (peso_animal / 15) * arroba_animal                           
                            animais_venda[iv] = [tipo, identificacao, status, valor_animal]

                            print("Atualizado com sucesso!")
                            continue    
                           
                        else:
                            print("Animal não encontrado.")



                elif opcao_2 == 'R':   # REMOVER ANIMAL 
                    ident = input("Digite a identificação do animal: ")

                    for i in range(len(animais)):
                        if animais[i][1] == ident:
                            animais.pop(i)
                            print("Removido com sucesso!")
                            continue

                        else:
                            print("Animal não encontrado.")

                    for iv in range(len(animais_venda)):
                        if animais_venda[iv][1] == ident:
                            animais_venda.pop(iv)
                            print("Removido com sucesso!")
                            continue

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
                                
                                if leite > leite_t:
                                    nome = input('Produto: ')
                                    valor = float(input('Valor por kg: '))
                                    produtos_adicionais.append([nome, kg, valor])
                                    leite -= leite_t
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
                                print(p[0], p[1],'kg(s)',p[2],'R$')
                                compra_f = input("Qual produto gostaria de comprar: ").lower()
                                if p[0] == compra_f:
                                    quantidade = float(input("Quantos KG: "))

                                    if p[1] >= quantidade:
                                        total = quantidade * p[2]

                                        p[1] -= quantidade

                                        print("Compra realizada com sucesso!")
                                     # NOTA FISCAL
                                        print("=" * 40)
                                        print("NOTINHA")
                                        print("=" * 40)
                                        print("Produto:", p[0])
                                        print("Quantidade:", quantidade)
                                        print("Total: R$", total)
                                        print("=" * 40)
                                    else:
                                        print("não temos estoque")
                                        break 

                        if lojinha1 == "2":
                            for an in animais_venda:
                                print("tipo: ", an[0], "identificacao: ", an[1], "status: ", an[2], "valor: ", an[3])
                                compra_f = input("identificação do animal: ").lower()
                                if an[1] == compra_f:
                                    print("Obrigado pela preferencia, volte sempre!!")

                                    total = an[3]
                                    animais_venda.pop()
                                    print("Compra realizada com sucesso!")
                                     # NOTA FISCAL
                                    print("=" * 40)
                                    print("NOTINHA")
                                    print("=" * 40)
                                    print("Tipo animal:", an[0])
                                    print("Total: R$", total)
                                    print("=" * 40)
                                else:
                                    print("não temos estoque")
                                
                                    break 

                    elif opcao_4 == "3":   # AGENDAR RETIRADA
                        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

                        dia = int(input("Qual dia da retirada: "))
                        mes = int(input("Qual mês da retirada (1-12): "))
                        ano = int(input("Qual ano da retirada: "))
                        nome_cliente = input('Nome para contato: ')

                        if mes < 1 or mes > 12:
                            print("Mês inválido.")
                        elif ano < 2026:
                            print("Ano inválido.")
                        elif dia < 1 or dia > dias_mes[mes - 1]:
                            print("Dia inválido para o mês informado.")
                        else:
                            print("Data registrada com sucesso!!!")
                            data_retirada.append([dia, mes, ano, nome_cliente ])
                           
                    elif opcao_4 == "4":  # LISTA AGENDAMENTO
                        print("-" * 50)
                        for d in data_retirada:
                            print(d[0], '/', d[1], '/', d[2], 'cliente:',d[3])
                        print("-" * 50)
                        
    else:
        print("Opção inválida.") #final
