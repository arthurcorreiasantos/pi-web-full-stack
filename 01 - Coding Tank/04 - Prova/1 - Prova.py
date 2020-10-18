import random
num = random.randint(0, 9) # número aleatório entre 0 e 9.
random.random() #retorna um float aleatorio entre 0 e 1



#Sorteio dos números

def senha(numeros,letras):
    sorteio_num = []
    sorteio_letras = []
    alfabeto = ['a','b','c','d', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letrasorteada = ''
    senha = []
    senhafinal = ''

    for i in range(numeros):
        num = random.randint(0, 9)
        sorteio_num.append(num)


    #Sorteio das letras

    for j in range(letras):
        indice = random.randint(0,len(alfabeto)-1)
        letrasorteada = letrasorteada + alfabeto[indice]


    listaletras = list(letrasorteada)
    aleatorioletras = random.randint(0,letras//2)
    minuscula = listaletras[aleatorioletras]
    maiuscula = minuscula.upper()
    letrasorteada = letrasorteada.replace(minuscula,maiuscula)

    sorteio_num = list(sorteio_num)
    letrasorteada = list(letrasorteada)
    senha = sorteio_num + letrasorteada
    for x in range(len(senha)):
        senhafinal = senhafinal + str(senha[x])
    print('Sua senha é: ', senhafinal)


numeros = int(input('Digite a quantiade de números da sua senha: '))
letras = int(input('Digite a quantidade de letras da sua senha: '))

senha(numeros,letras)