# dictionaries merupakan sekumpulan data yang
# terdiri dari kunci dan nilai

provinsi = {"jatim" : {"surabaya": "pakal"},
            "jateng":"semarang",
            "DIY":"jogja",
            "jabar" : "bandung",
            "DKI" : "jakarta"}

print(type(provinsi))
print(provinsi)

print(provinsi.items())
print(provinsi.keys())
print(provinsi.values())

# nambah elemen pada dictionraries
provinsi["bali"] = "denpasar"
print(provinsi)

# mengubah value pada dictionaries
provinsi["DIY"] = "Yogya"
print(provinsi)

# cara menghapus elemen pada dictionaries
del provinsi["bali"]
print(provinsi)

provinsi.pop("DKI")
print(provinsi)

# cek nilai di dictionaries
print("jatim" in provinsi)
print("surabaya" in provinsi.values())

print(provinsi['jatim']['surabaya'])

baru = {}
i = 0

for nama_ibukota_prov in provinsi:
  baru[i] = nama_ibukota_prov
  i += 1

print(baru)
print(baru[0])