'''
Enkapsulasi itu mengatur visibilias dari atribut2 sebuah class

--- hak akses variabel di OOP/PBO ---
public : bisa diakses secara langsung di luar class object
protected : bisa ditampilkan di luar class object dan hanya bisa diedit melalui
            class tersebut atau class turunan'nya. INI CUMA KONSEP/TEORI AJA :p
private : bisa diakses cuma lewat class tersebut saja
'''

class Mahasiswa():
  def __init__(self, nama, npm, jurusan):
    self.nama = nama
    self._npm = npm            # protected variable
    self.__jurusan = jurusan   # private variable

  def lihat_mhs(self):
    print("Namanya adalah", self.nama)
    print("NPM'nya adalah", self._npm)
    print("Jurusan'nya adalah", self.__jurusan)

mhs_1 = Mahasiswa("Zainab", 20002, "Sains Data")
#mhs_1.lihat_mhs()

#print(mhs_1.nama)
#mhs_1.nama = "Asiyah"
#print(mhs_1.nama)

#print(mhs_1._npm)
#mhs_1._npm = 20003
#print(mhs_1._npm)

#print(mhs_1.__jurusan)

# public function dan private function
class Pegawai:
  def __init__(self, nama, gaji):
    self.nama = nama
    self.gaji = gaji

  # private function
  def __Lihat_gaji(self):
    print(self.gaji)

  # public function
  def Lihat_data(self):
    print(self.nama)
    self.__Lihat_gaji()

#pgw_1 = Pegawai("Hawa", 12000)

#pgw_1.Lihat_data()
#pgw_1.__Lihat_gaji()

# GETTER dan SETTER
class Karyawan:
  def __init__(self, nama, gaji):
    self.nama = nama
    self.__gaji = gaji

  @property
  def tambah_gaji(self):
    pass

  @tambah_gaji.getter # mendapatkan nilai
  def tambah_gaji(self):
    return self.__gaji

  @tambah_gaji.setter # mengubah nilai
  def tambah_gaji(self, tambahan):
    self.__gaji += tambahan

  # public function
  def Lihat_data(self):
    print(self.nama)
    print(self.__gaji)

kry_1 = Karyawan("Hawa", 12000)
kry_1.Lihat_data()

kry_1.tambah_gaji = 3000
kry_1.Lihat_data()

print(kry_1.tambah_gaji)