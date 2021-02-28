# looping menggunakan list
names = ['hasudungan', 'rendi', 'bekti', 'yosua']

for name in names:
    print(name)

print(" ")

# for dalam for
gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']
buah = ['semangka','jeruk','apel','anggur']
sayur = ['kangkung','wortel','tomat','kentang']

Daftar_belanja = [gorengan,buah,sayur]

for subDaftarBelanja in Daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)