lista = [1, 4, 5, 0, 9, 10]
lista2 = [lista]
lista3 = [lista]
menor = 0
for i in range(len(lista2)):
    for j in range(len(lista3[i])):
        if lista2[i] < lista3[j]:
            menor = lista2[i]
            lista3.append(menor)
        
print(lista3)   