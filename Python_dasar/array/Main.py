# belajar memasukkan nilai kedalam array menggunakan input user
array = []
jumlahNilai = int(input("Masukkan jumlah nilai: "))

# looping
for x in range(jumlahNilai):
    # memasukkan nilai
    nilai = int(input("Masukkan nilai ke {}: ". format( x + 1 )))
    array.append(nilai)

print("Hasil inputan:", array, "\nJumlah array: ", len(array))
# print("")
print("Menampilkan isi array manual:\n")
gorengan = ['bala-bala', 'risoles', 'ubi-goreng']

# print(gorangan)
for g in gorengan:
    print(g)