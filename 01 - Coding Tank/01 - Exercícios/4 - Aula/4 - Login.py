user = input("Digite seu usuário: ")
senha =  input("Digite sua senha: ")

if user == "admin" and senha == "admin123":
    print("Seja bem vindo,", user)
elif user == "admin" and senha != "admin123":
    print("Senha incorreta")
elif user != "admin":
    print("Acesso negado")