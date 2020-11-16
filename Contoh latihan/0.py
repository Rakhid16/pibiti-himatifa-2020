lanjut = 'Y'
kumpulan_luas_segitiga = []

while lanjut == 'Y':
  alas = input("Masukan panjang alas (cm) : ")
  tinggi  = input("Masukan tinggi segitiga (cm) : ")

  luas = float(alas) * float(tinggi) * 0.5

  print("Luasnya adalah ", luas)
  kumpulan_luas_segitiga.append(luas)

  lanjut = input("\nMau lanjut lagi? (Y/T) : ")

  if lanjut == 'Y':
    continue
  else:
    print("Terima kasih telah menggunakan kami, " +
    "berikut adalah luas segitiga yang telah dihitung\n",
    kumpulan_luas_segitiga)