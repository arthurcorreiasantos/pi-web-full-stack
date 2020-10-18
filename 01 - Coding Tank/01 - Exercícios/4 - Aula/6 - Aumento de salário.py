salario = float(input("salario atual: "))
if salario >= 15000:
    salario_novo = salario * 1.05
    print ("O salário novo é: ", salario_novo)
elif salario < 15000 and salario >= 7000:
    salario_novo = salario * 1.1
    print ("O salário novo é: ", salario_novo)
elif salario < 7000 and salario >= 2800:
    salario_novo = salario * 1.15
    print ("O salário novo é: ", salario_novo)
elif salario < 2800:
    salario_novo * 1.20
    print ("O salário novo é: ", salario_novo)