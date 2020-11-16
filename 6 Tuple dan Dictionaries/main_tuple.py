mahasiswa_list = ["Jojo", "Naruto", "Trump"]
mahasiswa_tuple = ("Jojo", "Naruto", "Trump")


print(mahasiswa_list)
print(mahasiswa_list[0])
print(type(mahasiswa_list))

print()

print(mahasiswa_tuple)
print(mahasiswa_tuple[0])
print(type(mahasiswa_tuple))


# yang membedakan tuple dengan list hanyalah hak akses
# list bisa menambah elemen, hapus elemen, edit elemen, dan cetak elemen2
# tuple cuma bisa menambah elemen (tidak langsung), hapus elemen, dan cetak elemen2

print(mahasiswa_list)
mahasiswa_list[0] = "Komandan Hitsugaya"
print(mahasiswa_list)

print(mahasiswa_tuple)
mahasiswa_tuple[0] = "Zoro" # ERROR
print(mahasiswa_tuple)

mahasiswa_list.append("Ichigo")
print(mahasiswa_list)

mahasiswa_tuple = mahasiswa_tuple + ("Ichigo", "Sasuke")
print(mahasiswa_tuple)

print(type(mahasiswa_tuple))
print(mahasiswa_tuple)
tuple_to_list = list(mahasiswa_tuple)

print(type(tuple_to_list))
print(tuple_to_list)