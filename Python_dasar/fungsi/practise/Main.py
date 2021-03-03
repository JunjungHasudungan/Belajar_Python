class Operator:
    nilai = 0

    def __init__(self, nilaiInput = 0):
        self.nilai = nilaiInput

    def perkalian(self, nilai1, nilai2):
        hasil = nilai1 * nilai2
        print(nilai1, "*", nilai2, "=", hasil)
        return hasil

    def pembagian(self, nilai1, nilai2):
        hasil = nilai1 / nilai2
        print(nilai1, "/", nilai2, "=", hasil)
        return
    
    def kuadrat(self, nilai1):
        hasil = nilai1 ** 2
        print(nilai1, "^ = ", hasil)
        return hasil

    def pengurangan(self, nilai1, nilai2):
        hasil = nilai1 - nilai2
        print(nilai1, "-", nilai2, "=", hasil)

operator1 = Operator()
print("Perkalian")
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
operator1.perkalian(a, b)
print(" ")
print("Pembagian")
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
operator1.pembagian(a,b)
print(" ")
print("Kuadrat")
a = int(input("Masukkan nilai a: "))
operator1.kuadrat(a)
print(" ")
print("Pengurangan")
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
operator1.pembagian(a, b)