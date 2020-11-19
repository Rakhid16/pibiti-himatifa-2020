angka_dibagi = int(input("Masukan angka yang hendak dibagi : "))
angka_pembagi = int(input("Masukan angka pembagi : "))

# print("Hasilnya adalah", angka_dibagi/angka_pembagi)

try:
  print("Hasilnya adalah", angka_dibagi/angka_pembagi)
except:
  print("Ndak bisa dibagi sama 0")

a = 80
b = "Wandenreich"

try:
  print("Hasilnya adalah", a + b)
except:
  print("Tipe data harus sama!")