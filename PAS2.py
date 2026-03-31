# Variant A — Shop Receipt
# Practice 2, Week 2: Control Flow and Loops

# Task A1 — Multi-Item Shopping (while loop)

customer_name = input("Enter customer name: ")

total = 0.0
item_count = 0

while True:
    product = input("Enter product name (or 'done' to finish): ")
    if product == "done":
        break
    price = float(input("Enter price: "))
    total += price
    item_count += 1

print("customer :" + customer_name.upper())
print("Items : " + str(item_count))
print("Subtotal : " + str(total) + " KZT")

# Task A2 — Tiered Discount (if/elif/else)

if total < 3000:
    tier_label = "No discount"
    discount_percent = 0
elif total < 7000:
    tier_label = "5% discount"
    discount_percent = 5
else:
    tier_label = "15% discount"
    discount_percent = 15

discount_amount = total * discount_percent / 100
final_total = total - discount_amount

print("-"*30)
print("Discount tier : " + str(tier_label))
print("Discount : " + str(discount_amount) + " KZT")
print("Total : " + str(final_total) + " KZT")

#print
# Task A3 — Name Analysis (strings)

print()
name_length = len(customer_name)
print("Name : " + customer_name.upper())
print("Name : " + customer_name.lower())
print("Name : " + str(name_length))

if name_length > 5:
    print("Long name")
else:
    print("Short name")