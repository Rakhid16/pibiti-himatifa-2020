from math import sqrt

def prima(angka):
  if angka > 2:
    if angka % 3 == 0 or angka % 2 == 0 or str(sqrt(angka)).split(".")[1] == '0':
      print(angka, "bukanlah bilangan prima")
    else:
      print(angka, "adalah bilangan prima")
  elif angka == 2 or angka <= 1:
    print(angka, "adalah bilangan prima")