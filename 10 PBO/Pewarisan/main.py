'''
Pewarisan/Inheritance memungkinan class yang diwarisi
memanfaatkan seluruh atribut dari class pewaris
'''

# SIMPLE INHERITANCE
class Pewaris():
  halo = "Hello world!"
  __privat = "Ini variabel dengan hak akses privat"

  def __init__(self):
    self.str = "Ini kelas pewaris"

  def tampil(self):
    print(self.str)

                # Proses pewarisan
class Terwarisi(Pewaris):
  def lihat(self):
    print("Ini kelas yang diwarisi")

# Inisialisasi objek
objek = Terwarisi()

#objek.tampil()        # Dari class Pewaris
#print(objek.halo)     # Dari class Pewaris
#print(objek.__privat) # Dari class Pewaris
#objek.lihat()         # Dari class Terwaris

print("Class sekarang", objek.__class__)
print("Class pewaris", objek.__class__.__bases__)

# MULTIPLE INHERITANCE
class Mobil:
  def roda(self):
    return "Punya 4 roda"

class Kendaraan:
  def darat(self):
    return "di daratan"

  def laut(self):
    return "di laut"

  def udara(self):
    return "di udara"

  def roda(self):
    print("Ini dari class Kendaraan")

class Jeep(Mobil, Kendaraan):
  def __init__(self):
    self.name = "Katana"

jip = Jeep()
print("Class sekarang", jip.__class__)
print("Class pewaris", jip.__class__.__bases__)

print(jip.roda())
print(jip.darat())
print(jip.name)

# Overriding function
panzer = Kendaraan()
print(panzer.laut())
panzer.roda()