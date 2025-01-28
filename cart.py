from product import Product

class Cart():
    def __init__(self):
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def total_cost(self):
        total = 0
        for item in self.cart_items:
            total += item.price
        return total

    def display_cart(self):
        if not self.cart_items:
            print("No items in the cart")
        for item in self.cart_items:
            print(item.display_info())
