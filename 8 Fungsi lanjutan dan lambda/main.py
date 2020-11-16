def pangkat_tiga(angka):
  return angka ** 3

                        # argumen                 # nilai kembalian
pangkat_tiga_1 = lambda angka_1, angka_2, larik : [angka_1 ** 3 if angka_1 % 3 == 0 else angka_1 + 3,
                                                  angka_2 ** 2,
                                                  [elemen * 2 for elemen in larik]]

print(pangkat_tiga(3))
print(pangkat_tiga_1(4, 4, [2,3,4]))

# Fungsi sebagai argumen/parameter
def bagi_dua(hasil_pangkat_tiga):
  return hasil_pangkat_tiga / 2

print(bagi_dua(pangkat_tiga(4)))

# Fungsi di dalam fungsi sebagai nilai balik
def halo(nama):
  print(nama, "cuaca hari ini cerah ya?")

def sapa(nama):
  return halo(nama)

sapa("Sanji")

# Generator
def ini_generator():
  yield 1
  yield 2
  yield 3
  yield "JoJo"

for i in ini_generator():
  print(i)

def balok(panjang, lebar, tinggi):
  volume = panjang * lebar * tinggi
  yield volume

  luas_permukaan = 2 * (panjang * lebar) + 2 * (panjang * tinggi) + 2 * (tinggi * lebar)
  yield luas_permukaan

def balok_1(panjang, lebar, tinggi):
  volume = panjang * lebar * tinggi
  luas_permukaan = 2 * (panjang * lebar) + 2 * (panjang * tinggi) + 2 * (tinggi * lebar)
  return volume, luas_permukaan

for i in balok_1(10, 10, 10):
  print(i)

print(balok(5,5,5))