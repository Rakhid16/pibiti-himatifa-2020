kamus = {"elephant" : "gajah", "zebra" : "zebra", "dog" : "anjing", "camel" : "unta"}

kata = input("Masukan kata berbahasa inggris : ")

if kata in kamus:
  print("Terjemahan dari " + kata + " adalah " + kamus[kata])
else:
  print("Kata tersebt belum ada di kamus")