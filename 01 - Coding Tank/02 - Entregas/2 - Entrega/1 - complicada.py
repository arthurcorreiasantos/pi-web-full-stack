nomes = ['Maria da Silva', 'Ana Santos', 'Maria Santos', 'Ana Ferreira', 'João Santana', 'José Silva', 'Maria Antônia', 'Carlos Ricardo', 'Alan Dias', 'Silvana Sampaio']
idades = [23, 45, 34, 67, 19, 32, 43, 44, 70, 27]        
alturas = [1.78, 1.77, 1.65, 1.60, 1.87, 1.78, 1.75, 1.68, 1.9, 1.67]

i = 0
media = 0.0
while i<10:
    print(nomes[i],', ', idades[i], ', ', alturas[i],'m')
    media = media + alturas[i]
    i = i+1
print('A media de altura é de: ',media/len(alturas))