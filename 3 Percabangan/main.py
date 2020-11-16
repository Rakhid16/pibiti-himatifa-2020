angka = input("Masukan angka : ")

if int(angka) % 2 == 0:
  print("Itu angka genap")
else:
  print("Itu angka ganjil")

# EMPAT BARIS KODE DI ATAS BISA DIGANTI DENGAN 1 BARIS KODE DI BAWAH
print("Itu angka genap") if int(angka) % 2 == 0 else print("Itu angka ganjil")

# ELIF dan Nested branch

if int(angka) % 2 == 0 and int(angka) % 3 == 0:
  print("Itu angka habis dibagi dua dan tiga")
  if int(angka) > 10:
    print("lebih dari 10")
  else:
    print("kurang dari 10")
elif int(angka) % 2 == 0:
  print("Itu bukan hanya habis dibagi dua")
else:
  print("Itu angka hanya habis dibagi tiga")