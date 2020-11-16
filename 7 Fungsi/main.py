# Pendefinisian fungsi biasa
def nama_fungsi():
  larik = [1,2,3,4]
  print("Hello world!", sum(larik))

nama_fungsi()

# Fungsi dengan parameter/argumen
def sapa(nama):
  print("Namaku adalah", nama)

Nama = input("Masukkan nama : ")
sapa(Nama)
sapa("Jojo")

# Fungsi dengan argumen default
def kali_dua(angka=4):
  print(angka, "jika dikali dua hasilnya", angka*2)

kali_dua()
kali_dua(88)

# Fungsi dengan nilai kembalian
def balok(panjang, lebar, tinggi):
  volume = panjang * lebar * tinggi
  luas_permukaan = 2 * (panjang * lebar) + 2 * (panjang * tinggi) + 2 * (tinggi * lebar)

  return volume, luas_permukaan

volume_balok, luas_permukaan_balok = balok(10, 5, 7)

print(volume_balok)
print(luas_permukaan_balok)

# Cakupan global dan lokal
hewan = "Onta" # global variabel

def hewan_kurban():
  #global hewan
  #print(hewan)

  hewan = "Sapi Bertanduk" # local variabel
  print(hewan)

print(hewan)
hewan_kurban()

print(hewan)