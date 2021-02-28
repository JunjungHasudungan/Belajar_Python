class Product: 
    amount = 0 # variable 

    def __init__(self, inputName, inputType, inputPrice): #constructor
        self.name = inputName
        self.type = inputType
        self.price = inputPrice
        Product.amount += 1 # counting for all entry product
        print("NO:", Product.amount, "\nProduct Name: ", inputName,"\nProduct Type: ", inputType, "\nProduct Price: ", inputPrice,"\n")


product1 = Product("Lenovo", "AMD A6", 5000000)
# 
product2 = Product("MASPION", "MPX12E", 500000)
# print(Product.amount)
product3 = Product("LG", "EXPY", 1500000)
# print(Product.amount)