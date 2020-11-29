bilangan = input("Masukan tiga bilangan berturut-turut : ").split(" ")

try:
  bilangan = sorted([int(angka) for angka in bilangan])

  if bilangan[0]**2 + bilangan[1] ** 2 == bilangan[2] ** 2:
    print(bilangan, " adalah bilangan pythagoras")
  else:
    print(bilangan, " bukan bilangan pythagoras")

except:
  print("hanya menerima angka!")