x = int(input())
while x >=0:
    if x >= 0 and x <= 10:
        x = x**2
        break
    elif x > 10 and x <= 20:
        x = x**3
        break
    elif x > 20:
        x = -1
        break
    else:
        break
 
print(x)