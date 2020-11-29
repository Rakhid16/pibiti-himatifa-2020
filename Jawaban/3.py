print("Format masukkan = JAM:MENIT:DETIK")

waktu_awal = input("Masukkan waktu awal : ").split(":")
waktu_akhir = input("Masukkan waktu akhir : ").split(":")

try:
  waktu_awal, waktu_akhir = [int(satuan) for satuan in waktu_awal], [int(satuan) for satuan in waktu_akhir]
  
  if waktu_awal[1] > 60 or waktu_awal[2] > 60 or waktu_akhir[1] > 60 or waktu_akhir[2] > 60:
    print("Menit dan detik harus tidak lebih dari 60")
  else:
    waktu_awal = waktu_awal[0] * 3600 + waktu_awal[1] * 60 + waktu_awal[2]
    waktu_akhir = waktu_akhir[0] * 3600 + waktu_akhir[1] * 60 + waktu_akhir[2]
    
    print(waktu_awal)
    print(waktu_akhir)

    selisih = waktu_akhir - waktu_awal
      
    Jam = int(selisih / 3600)
    menit = selisih % 3600
    Menit = int(menit / 60)
    Detik = menit % 60
  
    print("Selisih waktunya adalah " + str(Jam) + ":" + str(Menit) + ":" + str(Detik))

except:
  print("Masukan harus berupa angka!")