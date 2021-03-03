class Product:
    amount = 0

    def __init__(self, inputName, inputType, inputPrice): 
        self.name = inputName
        self.type = inputType
        self.__price = inputPrice # private property
        Product.amount += 1

    @property
    def info(self): 
            return "No: {} \nName: {} \nType: {} \nPrice: {}".format(self.amount, self.name, self.type, self.__price)

product1 = Product("Lenovo", "AMD A6", 4500000)
product2 = Product('Iphone', '5S', 150000)

print(product1.info)
print(product2.info)