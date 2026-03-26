# Task 1 — Variant A: Shop Receipt

# a) Input & Variables
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter price per unit (KZT): "))
quantity = int(input("Enter quantity: "))

# b) Calculations
subtotal = price * quantity
discount = subtotal * 0.10 if subtotal > 5000 else 0
total = subtotal - discount

# c) Formatted Output
print("=" * 30)
print("SHOP RECEIPT")
print("=" * 30)
print("Customer : " + customer_name)
print("Product  : " + product_name)
print("Price    : " + str(price) + " KZT")
print("Quantity : " + str(quantity))
print("-" * 30)
print("Subtotal : " + str(subtotal) + " KZT")
print("Discount : " + str(discount) + " KZT")
print("Total    : " + str(total) + " KZT")
print("=" * 30)

# d) Comparison
print("Discount applied:", subtotal > 5000)
print("Paid more than 3000:", total > 3000)