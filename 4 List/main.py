# LIST  itu adalah array sebagaimana di bahasa pemrograman lain
# bedanya list pada python ini bisa menyimpan lebih dari 1 tipe data
# pada sebuah list

larik = [2,4,6,8,10]
print(larik)

print(len(larik))

larik.append(12)
print(larik)

larik.reverse()
print(larik)

larik.sort()
print(larik)

# Akses elemen berdasarkan indeks

print(larik[0])
print(larik[-1])
print(larik[2])
print(larik[1:4])

del larik[0]

print(larik)

larik.remove(10)

print(larik)

matriks = [[1,2] , [3,4]]
print(matriks)

tensor = [[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]],[[13,14],[15,16],[17,18]]]
print(tensor[0][0][0])