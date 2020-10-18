listapreço = []
listaquantidade = []
total = 0.0

for i in range(10):
    preço = float(input('Digite o preço do produto: '))
    listapreço.append(preço)
    total = total + preço
    quantidade = int(input('Digite a quantidade do produto: '))
    listaquantidade.append(quantidade)
print('O valor total é:', total)
for j in range(10):
    print('O valor do produto', j,'é', listapreço[j])