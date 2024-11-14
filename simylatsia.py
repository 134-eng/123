class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"


class customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def total_cost(self):
        return sum(product.price for product in self.cart)

    def checkout(self):
        if not self.cart:
            print(f"{self.name}, в вашому кошику нічого немає")
        else:
            print(f"кошик {self.name}:")
            for product in self.cart:
                print(f"- {product}")
            print(f"загальна сума: {self.total_cost():.2f}")


apple = product("apple", 1.2)
banan = product("banan", 1.5)
water = product("water", 2)

customer1 = customer("oleg")

customer1.add_to_cart(apple)
customer1.add_to_cart(banan)
customer1.add_to_cart(water)

customer1.checkout()
