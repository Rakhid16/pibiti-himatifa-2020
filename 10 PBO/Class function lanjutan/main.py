class StatMethod:
  # tidak memerlukan self sebagai argumen
  # dan bisa membuat argumen secara bebas
  # bisa dipake buat helper function
  @staticmethod
  def halo(nama):
    print("Hello world!", nama)

class ClassMethod:
  def __init__(self, nama_mhs_baru = ""):
    self.nama_mhs = "Jojo, Biden, Haris"
    self.nama_mhs_baru = nama_mhs_baru

  # wajib ada argumen namun bukan self
  # biasanya nama argumen'nya cls
  @classmethod
  def halo(cls): # cls itu merujuk pada kelasnya sendiri (ClassMethod)
    mhs_baru = ", Patimura"
    tambah_mhs = cls(mhs_baru)

    return tambah_mhs.nama_mhs + tambah_mhs.nama_mhs_baru

  # cocok digunakan jika terdapat case yang tidak memerlukan
  # komunikasi langsung dengan instance suatu class, tetapi
  # masih membutuhkan attribut-atrribut lain dalam classnya.

#Halo_1 = StatMethod()
#Halo_1.halo("Ikal")

#Halo_2 = ClassMethod().halo()
#print(Halo_2)

# Menambahkan class variabel dan 
# class function dari luar
class Nasabah():
  pass

Nasabah.nama = "Carl Johnson"
Nasabah.usia = 40
Nasabah.gaji = 12000

def Lihat(self):
  print(self.nama)
  print(self.usia)
  print(self.gaji)

# memasukkan function Lihat ke dalam class Nasabah
# function Lihat menjadi class function dengan nama lihat
Nasabah.lihat = Lihat

nsb_1 = Nasabah()
nsb_1.lihat()