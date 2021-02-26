# create some function with return
def perkalian(a, b):
    hasil = a * b
    return hasil

perkalian = perkalian(2,3)
print("Hasil perkalian = ", perkalian)
print(" ")
print("Contoh Fungsi ke-2 ")

def diskon(hargaDasar):
    hasilDiskon = hargaDasar - (hargaDasar * 10/ 100)
    return hasilDiskon

hargaAwal = 10000
total = diskon(hargaAwal) 
print("Harga awal: ", hargaAwal)
print("Harga Setelah diskon:", total)