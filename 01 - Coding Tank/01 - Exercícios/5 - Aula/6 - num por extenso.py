num = int(input("Digite um número inteiro de 0 à 10: "))
if num >= 0 and num <= 10:
    alg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ext = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
    indice = alg.index(num)
    print(ext[indice])
else:
    print("Digite um número inteiro válido")