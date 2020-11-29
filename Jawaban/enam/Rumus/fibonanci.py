def fibonanci(angka):
  deret, satu, dua = [0, 1], 0, 1
  
  for _ in range(angka-2):
    jumlah = satu + dua
    satu, dua = dua, jumlah
    deret.append(jumlah)
  print(deret)