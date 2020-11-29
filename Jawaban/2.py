batas_bawah = input("Masukkan tahun batas bawah : ")
batas_atas = input("Masukkan tahun batas atas : ")

try :
  tahun_kabisat = [tahun for tahun in range(int(batas_bawah), int(batas_atas)) if tahun % 4 == 0]
  print(tahun_kabisat)
except:
  print("hanya menerima angka!")