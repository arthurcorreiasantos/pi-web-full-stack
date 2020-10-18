idade = int(input("Digite a idade: "))
if idade >= 18:
    carteira = input("Tem carteira? Digite 'Sim' se tiver carteira e não se 'Não' tiver carteira: ")
    if carteira == "Sim":
        print("Apto para dirigir")
else:
    print('Não apto para dirigir')