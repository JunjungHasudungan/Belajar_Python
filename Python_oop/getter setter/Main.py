class Product:

    amount = 0

    def __init__(self, inputName = 0):
        self.__name = inputName
        Product.amount += 1

    # setter
    def setName(self, inputName):
        self.__name = inputName

    def getName(self):
        # return info()
        return self.__name

name = input("enter your name: ")
product1 = Product()

product1.setName(name)
print("Your input Name: ", product1.getName())
