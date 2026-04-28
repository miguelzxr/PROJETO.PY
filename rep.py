usuarios = []
senhas = []
while True:
    entrar = input("LOGIN ENTRAR: [E] | SAIR [S] | NOVO USER [NEW]: | ADMIN (ADM) ").upper()
    if entrar == "S":
        break
    if entrar == "E":
        user = input("DIGITE O USUARIO: ")
        senha1 = input("DIGITE A SENHA: ")
    if entrar == "NEW":
        user = input("digite seu nome de usuario: ")
        senha1 = input("digite sua senha: ")
        senha2 = input("confirme a sua senha: ")
        if senha1 == senha2:
            print("bem vindo cliente")
            usuarios.append(user)
            senhas.append(senha1)
        else:
            print("digite novamente!!!!!!!!!!!!!!!!!!!")
    if entrar == "ADM":
        user_adm = input("digite seu usuario: ")
        senha_adm = input("digite sua senha adm: ")
        if user_adm == "ADMIN" and senha_adm == "A1D2M3I4N5":
            print("BEM VINDO ADMMMMMMMMMMMMMMMMMMM")
         


              
# and user == "ADMIN" and senha1 == "A1D2M3I4N5"



# usuarios = []


# if (usuarios[0][2]) == "ADM":
#     print("==========================================")
#     print("              bem vindo adm             ")