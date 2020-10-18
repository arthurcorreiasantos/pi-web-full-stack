num = int(input('Digite um número inteiro de 1 à 7: '))
if num > 1 and num < 7:
    dias = ['domingo','segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']
    print('O dia da semana é: ', dias[num-1])
else:
    print('Número inválido')