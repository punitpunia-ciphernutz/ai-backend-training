from models.user import Customer
from models.product import Product
from models.order import Order

#create product:
p1 = Product("Laptop", 150000, 50)
p2 = Product("Phone", 50000, 100)

#create customer:
c1 = Customer("Punit")
c2 = Customer("Ankit")

#create order:

order = Order(c1)
order.add_product(p1, 5)
order.add_product(p2, 10)

order2 = Order(c2)
order2.add_product(p1, 3)
order2.add_product(p2, 5)

print(p1)
print(p2)
print(order)
print(order2)