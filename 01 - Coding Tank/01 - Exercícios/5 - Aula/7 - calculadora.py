num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
operação = input('Digite a operação: "+", "-", "*" ou "/": ')

if operação == '+':
    resultado = num1 + num2
elif operação  == '-':
    resultado = num1 - num2
elif operação == '*':
    resultado = num1 * num2
else:
    resultado = num1 / num2

print('O resultado da operação é: ', resultado)    