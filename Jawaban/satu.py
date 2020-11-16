# PEMANFAATAN LIST COMPREHENSION

kata = "missisippi"
jumlah_huruf_i = [1 for huruf in kata if huruf == "i"]
print(sum(jumlah_huruf_i))

kumpulan_kata = ["aezakmi", "hesoyam", "rocketman", "abogoboga", "lumberjack"]
kumpulan_kata_o = [kata for kata in kumpulan_kata if "o" in kata]
print(kumpulan_kata_o)