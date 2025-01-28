from product import Product
from product_manager import ProductManager


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
