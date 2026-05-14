class Order:
    def __init__(self,customer):
        self.customer = customer
        self.items = []

    def add_product(self, product, quantity):
        if quantity <= product.get_stock():
            self.items.append ((product, quantity))
            product.update_stock(quantity)
        else:
            print(f"Not enough stock for {product.name}. Available: {product.get_stock()}")
    
    def total_price(self):
        total = 0
        for product, quantity in self.items:
            total += product.get_price() * quantity
        return total
    
    def __str__(self):
        result = f"order for {self.customer.name}\n"
        for product, quantity in self.items:
            result += f"{product.name} x {quantity}\n"
        result += f"Total Price: ${self.total_price()}"
        return result