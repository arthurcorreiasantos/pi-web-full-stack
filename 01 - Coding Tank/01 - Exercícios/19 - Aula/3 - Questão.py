'''Enunciado
Faça uma função que receba uma lista com uma quantidade indeterminada
de números e informe qual o maior número dessa lista. Não use o max()'''


'''Eu posso percorrer a lista comparando cada elemento com cada um e armazenando em uma variável qual o maior.
Ou posso usar uma função para classificar do maior para o menor e pegar o último valor YOU DAMASS


'''
def maior ()

    num = [ 9, 2, 3, 5, 3, 7]
    maior = 0
    classificado = sorted(num)
    maior = classificado[-1]
    print('O maior número é o: ', maior)

maior()