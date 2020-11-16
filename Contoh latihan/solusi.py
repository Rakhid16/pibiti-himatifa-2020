lanjut = 'Y'
kumpulan_luas_segitiga = []

while lanjut == 'Y':
  alas = float(input("Masukkan panjang alas (cm) : "))
  tinggi = float(input("Masukkan tinggi segitiga (cm) : "))

  luas = alas * tinggi * 0.5 # / 2

  print("Luas segitiganya adalah :", luas)
  kumpulan_luas_segitiga.append(luas)

  lanjut = input("\nMau lanjut lagi?")

  if lanjut == 'Y':
    continue
  else:
    print("Terima kasih telah menggunakan program kami\n"
          + "Berikut adalah segitiga yang telah dihitung\n",
          kumpulan_luas_segitiga)