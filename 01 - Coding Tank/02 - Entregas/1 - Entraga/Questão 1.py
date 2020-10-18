#Quem matou?

nome = input("Digite o seu nome: ")
print('Responda "Sim" ou "Não" para as perguntas abaixo: ')

vizinho = input("Mora perto da vítima? ")
trabalho = input("Já trabalhou com a vítima? ")
telefone = input("Já telefonou para a vítima? ")
local = input("Esteve no local do crima? ")
deve = input("Devia para a vitma? ")

vizinho = (vizinho == "Sim")
trabalho = (trabalho == "Sim")
telefone = (telefone == "Sim")
local = (local == "Sim")
deve = (deve == "Sim")

resultado = (vizinho + trabalho + telefone + local + deve)

if resultado >= 5:
    print('O(a) ', nome, ' é assassino')
elif resultado < 5 and resultado >= 3:
    print('O(a) ', nome, ' é cúmplice')
elif resultado < 2 and resultado >= 1:
    print('O(a) ', nome, ' é suspeito')
else:
    print('O(a) ', nome, 'está liberado')