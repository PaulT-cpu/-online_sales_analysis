from product import Product
from product_manager import ProductManager
from cart import Cart

# Create an instance of the ProductManager class
manage_products = ProductManager()

# Add products to the product manager list
product1 = Product("Sparring Gloves", 50, 12)
product2 = Product("Boxing Shorts", 30, 20)
product3 = Product("Headgear", 100, 7)

manage_products.add_product(product1)
manage_products.add_product(product2)
manage_products.add_product(product3)

# Display all products
print("\nAll products:")
manage_products.display_all_products()

# Display the total value of all products
print(f"\nTotal value of all products: ${manage_products.calculate_total_value()}")

# Remove a product
manage_products.remove_product_by_name("Boxing Shorts")

# Display all products after removal
print("\nProducts after removal:")
manage_products.display_all_products()

# Create an instance of the Cart class
shopping_cart = Cart()

# Add products to the cart
shopping_cart.add_item(product1)
shopping_cart.add_item(product2)
shopping_cart.add_item(product3)

# Display the cart
print("\nCart contents:")
shopping_cart.display_cart()

# Display the total cost of the cart
print(f"\nTotal cost of the cart: ${shopping_cart.total_cost()}")
