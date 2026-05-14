class Product:
    def __init__(self, name, price,stock):
        self.name = name
        self.__price = price
        self.__stock = stock

    def get_price(self):
        return self.__price
    def get_stock(self):
        return self.__stock
    
    def update_stock(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
        else:
            print("Not enough stock available.")

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.__price}, Stock: {self.__stock}"


