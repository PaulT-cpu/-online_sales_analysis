from product import Product

class ProductManager():
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        if not self.products:
            print("No products to display")
        for product in self.products:
            print(product.display_info())
 
    def calculate_total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total

    def remove_product_by_name(self, name):
        self.products = [product for product in self.products if product.name != name]
