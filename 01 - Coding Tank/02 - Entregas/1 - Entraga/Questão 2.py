#Diagnóstico

nome = input("Digite seu nome: ")
print('Digite "sim" ou "não" para os sintomas que você sente.')

dor = input("Sente dor no corpo? ")
febre = input("Você tem febre? ")
tosse = input("Você tem tosse? ")
congestao = input("Está com congestão nasal? ")
manchas = input ('Tem manchas no corpo? ')

dor = str(int(dor == "sim"))
febre = str(int(febre == "sim"))
tosse = str(int(tosse == "sim"))
congestao =str(int(congestao == "sim"))
manchas = str(int(manchas == "sim"))

resultado = (dor + febre + tosse + congestao + manchas)

if resultado == "11001":
    print("O(a) ", nome, "suspeita de dengue")
elif resultado == "11110" or resultado == "01110":
    print("O(a) ", nome, "está com gripe")
elif resultado == "10000" or resultado == "00000":
    print("O(a) ", nome, "está sem doença")
else:
    print("Resultado indefinido. Favor procurar um especialista.")