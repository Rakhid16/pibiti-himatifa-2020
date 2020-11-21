# memuat semua isi modul/file
import Bangun_Datar

print(Bangun_Datar.luas_segitiga(5, 5))

# memuat semua isi modul/file dengan alias
import Bangun_Ruang as br

print(br.luas_permukaan_kubus(8))

# memuat sebagian isi dari modul package Beli
from Beli import Buku
from Beli.Mobil import jeep
import Beli

Buku.novel("Perahu Kertas")
jeep("Katana")
Beli.Mobil.sedan()