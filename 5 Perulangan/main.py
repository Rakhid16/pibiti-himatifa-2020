i = 0

# while
while i < 5:
  print(i)
  i += 1 # i = i + 5

print()

# for-range
for j in range(5):
  print(j)

print()

# for - C Style
for k in range(-5, 5, 2): # (awalan, akhir, inkremen atau dekremen)
  print(k)

print()

# break
for l in range(5):
  if l == 3 :
    break

  print(l)
  
print()

# continue
for l in range(5):
  if l == 3 :
    continue

  print(l)

print()

# perulangan pada list
binatang_kurban = ["Sapi", "Kambing", "Domba", "Unta"]

for nilai in binatang_kurban:
  print(nilai)

for indeks, nilai in enumerate(binatang_kurban):
  print(indeks, nilai)

