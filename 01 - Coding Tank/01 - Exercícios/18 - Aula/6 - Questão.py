def parouimar(num):
    if num%2 == 0:
        return 'o número '+ str(num)+ ' é par'
    else:
        return ' o número'+ str(num)+ ' é impar'

num = int(input('Digite um número: '))
print(parouimar(num))