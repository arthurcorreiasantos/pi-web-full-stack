idade = int(input())
if 0 < idade <= 10:
  print('vc é uma criança')
elif 11 <= idade <= 12:
  print('vc é pré-adolescente')
elif 13 <= idade <= 17:
  print('vc é adolescente')
elif idade >= 18:
  print('vc já é adulto')