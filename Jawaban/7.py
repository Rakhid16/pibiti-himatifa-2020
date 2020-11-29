from os import system

class Universitas:
  def __init__(self):
    self.fakultas = []

  def tambah(self, nama_fakultas):
    self.fakultas.append(nama_fakultas)

  def lihat(self):
    print(self.fakultas)

UPNJATIM, UPNJOGJA, UPNJKT = Universitas(), Universitas(), Universitas()

while True:
  print("1. Lihat Fakultas UPNJATIM\n" +
        "2. Lihat Fakultas UPNJOGJA\n" +
        "3. Lihat Fakultas UPNJKT\n" +
        "4. Tambah Fakultas UPNJATIM\n" +
        "5. Tambah Fakultas UPNJOGJA\n" +
        "6. Tambah Fakultas UPNJKT\n\nMasukan q untuk keluar")
  
  pilihan = input("Masukan pilihan : ")
  
  if pilihan == '1':
    system('clear')
    UPNJATIM.lihat()
    back = input("Ketikan apapun untuk kembali")
    system('clear')
    continue

  elif pilihan == '2':
    system('clear')
    UPNJOGJA.lihat()
    back = input("Ketikan apapun untuk kembali")
    system('clear')
    continue

  elif pilihan == '3':
    system('clear')
    UPNJKT.lihat()
    back = input("Ketikan apapun untuk kembali")
    system('clear')
    continue

  elif pilihan == '4':
    system('clear')
    fakultas_baru = input("Masukan nama fakultas baru : ")
    UPNJATIM.tambah(fakultas_baru)
    system('clear')
    continue

  elif pilihan == '5':
    system('clear')
    fakultas_baru = input("Masukan nama fakultas baru : ")
    UPNJOGJA.tambah(fakultas_baru)
    system('clear')
    continue

  elif pilihan == '6':
    system('clear')
    fakultas_baru = input("Masukan nama fakultas baru : ")
    UPNJKT.tambah(fakultas_baru)
    system('clear')
    continue

  elif pilihan == 'q':
    break

  else:
    back = input("Masukan tidak valid!\nKetikan apapun untuk mengulang")
    system('clear')
    continue
