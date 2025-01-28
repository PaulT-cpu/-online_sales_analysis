from product import Product

class ProductManager():
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product_by_name(self, name):
        self.products = [product for product in self.products if product.name != name]
