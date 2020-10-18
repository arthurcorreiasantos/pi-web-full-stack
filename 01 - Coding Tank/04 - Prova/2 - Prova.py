import random

def jogo():
    opcoes = ['pedra', 'papel', 'tesoura']
    num = random.randint(0, 2) # número aleatório entre 0 e 9.
    aleatorio = opcoes[num]
    usuario = str(input('pedra, papel ou tesoura? '))

    print(aleatorio)

    dic = {'pedra':'tesoura', 'papel':'pedra', 'tesoura':'papel'}

    if dic[usuario] == aleatorio:
        print('Você ganhou!')
        dec = input('Quer jogar novamente? (s/n)')
        if dec == 's':
            jogo()
        else:
            print('Obrigado por jogar!')
    else:
        print('Você perdeu. =/')
        dec = input('Quer jogar novamente? (s/n)')
        if dec == 's':
            jogo()
        else:
            print('Obrigado por jogar!')

jogo()