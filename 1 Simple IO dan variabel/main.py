print("Hello world!")
print(1442)

nama = input("\nMasukan nama anda : ")
print("Hai " + nama)

# single line comment

'''
multiple line comment
'''

print(1)

Nama = "Ikal"
Usia = 21
Gaji = 12.5

# PRINT biasa - 1
print("Nama saya", Nama, "usia saya", Usia, "tahun")

# PRINT biasa - 2
print("Nama saya " + Nama + " gaji saya " + str(Gaji) + "k dolar")

# PRINT yang lain
print("Nama saya %s, usia saya %d" %(Nama, Usia))

# PRINT dengan fitur format{}
print("Orang yang berusia {} memiliki gaji sebesar {} juta rupiah".format(Usia, Gaji))

# hapus variabel
del nama
print(nama)

# pesan error akan tercetak karena variabel nama udah terhapus