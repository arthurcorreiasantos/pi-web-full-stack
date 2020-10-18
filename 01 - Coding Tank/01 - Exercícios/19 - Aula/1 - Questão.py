def inversao (texto):
    texto = list(texto)
    inverso = []
    posição = len(texto)-1
    for i in range(len(texto)):
        inverso.append(texto[posição])
        posição = posição - 1
    return(inverso)

print(inversao('abcdefg'))