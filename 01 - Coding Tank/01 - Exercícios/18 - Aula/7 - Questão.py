def soma (lista):
    soma = 0
    for i in lista:
        soma = soma + lista[i]
    return soma

lista = [1, 2, 3, 4, 5, 6, 7, 8]

print(soma(lista))