from os import system
from Acak.angka_acak import acak_bos
from Rumus import fibonanci, prima

while True:
  print("1. Tampilkan angka acak\n" +
        "2. Masukan angka prima\n" +
        "3. Masukan angka untuk bilangan fibonanci" +
        "\n\nMasukan q untuk keluar")
  
  pilihan = input("Masukan pilihan : ")
  
  if pilihan == '1':
    system('clear')
    acak_bos()
    back = input("Tekan enter untuk kembali")
    system('clear')
    continue

  elif pilihan == '2':
    system('clear')
    angka = int(input("Masukan angka berapapun : "))
    prima.prima(angka)
    back = input("Tekan enter untuk kembali")
    system('clear')
    continue

  elif pilihan == '3':
    system('clear')
    angka = int(input("Masukan angka : "))
    fibonanci.fibonanci(angka)
    back = input("Tekan enter untuk kembali")
    system('clear')
    continue

  elif pilihan == 'q':
    break

  else:
    back = input("Masukan tidak valid!\nTekan enter untuk mengulang")
    system('clear')
    continue