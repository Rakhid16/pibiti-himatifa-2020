class Mahasiswa:
  # class variable
  nama = "Wahidun"
  npm = 17081010068
  hobi = "panjat pinang"

  # class function
  def lihat(self):
    print(self.nama)
    print(self.npm)
    print(self.hobi)

#print(Mahasiswa)
#print(Mahasiswa.nama)
#print(Mahasiswa.npm)
#print(Mahasiswa.hobi)
#print(type(Mahasiswa.nama))

# Membuat objek dari class Mahasiswa()
#mhs_1, mhs_2 = Mahasiswa(), Mahasiswa()

#print(mhs_1.nama)
#print()
#mhs_2.lihat()

class Mahasiswa1:
  # konstruktor, melakukan instansiasi paling 
  # pertama kali ketika sebuah objek diciptakan
  def __init__(self, input_nama, input_npm, input_jurusan, input_ipk=3.0):
    # instance variable
    self.name = input_nama
    self.npm = input_npm
    self.jurusan = input_jurusan
    self.ipk = input_ipk

  # void function, function tanpa nilai kembalian/return
  def tambah_nilai(self, nilai_tambahan):
    if self.ipk + nilai_tambahan > 4:
      pass
    else:
      self.ipk += nilai_tambahan

  # instance method/function, perlu ada self sebagai argumen/parameter
  def nilai_mhs(self):
    return self.ipk * 25

  # Desktruktor, menghapus objek untuk melepas memori
  def __del__(self):
    print("Objek terhapus")

mhs_1 = Mahasiswa1("Yhwach", 20005, "Sains Data", 3.2)
#print(mhs_1.__dict__)

#print(mhs_1.nilai_mhs())
#mhs_1.tambah_nilai(0.9)

#print("%.2f" %(mhs_1.ipk))
#print(mhs_1.nilai_mhs())

mhs_2 = Mahasiswa1("JoJo", 20001, "Informatika", 2.8)
mhs_3 = Mahasiswa1("Kardun", 20002, "Sistem Informasi", 3.8)
mhs_4 = Mahasiswa1("Kardun", 20002, "Sistem Informasi")

print(mhs_2.__dict__)
print(mhs_3.__dict__)
print(mhs_4.__dict__)