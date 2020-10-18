idade = int(input("Digite a idade: "))
while idade <= 0 and idade >= 150:
    idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário"))
while salario <= 0:
    salario = float(input("Digite o salário"))
genero = input("Digite o gênero (M, F ou Outro): ")
while genero != 'M' and genero != 'F' and genero != 'Outro':
    genero = input("Digite o gênero (M, F ou Outro): ")