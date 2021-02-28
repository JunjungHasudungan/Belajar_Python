class Product: 
# type data variable public
    amount = 0  
    name = 0
    tipe = 0

#constructor
    def __init__(self, inputName, inputType, inputPrice = 0): 
        self.name = inputName 
        self.tipe = inputType 
        self.__price = inputPrice # tipe private data variable
        Product.amount += 1 

# void function tanpa argument, tanpa return
    def infoProduct(self):
        print("NO:",self.amount, "\nProduct Name: ", self.name) 

# function dengan argument tanpa return / setter
    def setPrice(self, price):
        self.__price += price

# function tanpa argument dengan return / getter
    def getPrice(self):
        return self.__price

# inisialisasi object dan memberi nilai
product1 = Product("Lenovo", "AMD A6", 500000) 
product1.infoProduct() # menampilkan dengan void method 
product1.setPrice(10000) # mengisi / setting ulang nilai dengan setter method
print("Product Price: ", product1.getPrice()) # menampilkan data dengan method getter
print("Product Type: ", product1.tipe, "\n") # menampikan dengan cara biasa

product2 = Product("LG", " 32''  ", 300000) 
product2.infoProduct() # menampilkan dengan void method 
product2.setPrice(15000) # mengisi / setting ulang nilai dengan setter method
print("Product Price: ", product2.getPrice()) # menampilkan data dengan method getter
print("Product Type: ", product2.tipe, "\n") # menampikan dengan cara biasa

product3 = Product("MASPION", "MAX12", 120000) 
product3.infoProduct() # menampilkan dengan void method 
product3.setPrice(10000) # mengisi / setting ulang nilai dengan setter method
print("Product Price: ", product3.getPrice()) # menampilkan data dengan method getter
print("Product Type: ", product3.tipe, "\n") # menampikan dengan cara biasa

