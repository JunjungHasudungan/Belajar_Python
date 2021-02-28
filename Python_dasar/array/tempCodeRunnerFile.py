# belajar memasukkan nilai kedalam array
array = []
jumlahNilai = int(input("Masukkan jumlah nilai: "))

# looping
for x in range(jumlahNilai):
    nilai = int(input("Masukkan nilai ke {}: ". format( x + 1 )))
array.append(nilai)
print("Hasil inputan:", array)