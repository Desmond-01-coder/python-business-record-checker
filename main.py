import json

print("===================================")
print("     BUSINESS RECORD CHECKER")
print("===================================")

business_name = input("Enter your business name: ")

print(f"\nWelcome to {business_name}!")

# Store product records

products = [
{"name": "Rice", "price": 25000, "quantity": 5},
{"name": "Beans", "price": 18000, "quantity": 3},
{"name": "Cooking Oil", "price": 12000, "quantity": 0},
{"name": "Spaghetti", "price": 8500, "quantity": 4}
]

def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(products, file, indent=4)

def load_inventory():
    global products

    try:
        with open("inventory.json", "r") as file:
            products = json.load(file)

    except FileNotFoundError:
        save_inventory()

load_inventory()
print("\nPRODUCT RECORDS")
print("-----------------------------------")

for product in products:
    print(f"Product: {product['name']}")
    print(f"Price: ₦{product['price']:,}")
    print(f"Quantity: {product['quantity']}")
    print("-----------------------------------")
  
  # Calculate number of products
total_products = len(products)

print("\nBUSINESS SUMMARY")
print("-----------------------------------")
print(f"Total different products: {total_products}")

    # Total number of items in stock
total_quantity = sum(product["quantity"] for product in products)
print(f"Total items in stock: {total_quantity}")

  # identifying the most expensive product
most_expensive = max(products, key=lambda product: product["price"])
  # identifying the cheapest product
cheapest = min(products, key=lambda product: product["price"])
print(f"Cheapest product: {cheapest['name']} - ₦{cheapest['price']:,}")
print(f"Most expensive product: {most_expensive['name']} - ₦{most_expensive['price']:,}")
  # Average product price
total_price = sum(product["price"] for product in products)
average_price = total_price / len(products)
print(f"Average product price: ₦{average_price:,.2f}")
  
  # total number of products that need restocking
products_to_restock = sum(1 for product in products if product["quantity"] <= 3)
print(f"Products needing restocking: {products_to_restock}")
  # Percentage of products that nees restocking
restock_percentage = (products_to_restock / len(products)) * 100
print(f"Percentage of products needing restocking: {restock_percentage:.1f}%")
  # Inventory status
if restock_percentage == 0:
    inventory_status = "Stock levels are healthy"
elif restock_percentage < 50:
    inventory_status = "Some products need attention"
else:
    inventory_status = "Restocking is urgently needed"

print(f"Inventory status: {inventory_status}")
 # Calculate the total value of stock
total_stock_value = 0
for product in products:
    stock_value = product["price"] * product["quantity"]
    total_stock_value += stock_value

print("\nTOTAL STOCK VALUE")
print(f"₦{total_stock_value:,}")

   # Empty stock alert
print("\nSTOCK ALERTS")
print("-----------------------------------")

for product in products:
    if product["quantity"] == 0:
        print(f"OUT OF STOCK: {product['name']}")

    # Low stock alert
print("\nLOW STOCK ALERTS")
print("-----------------------------------")

for product in products:
    if product["quantity"] > 0 and product["quantity"] <= 3:                    # Checks whether there are three items or fewer
        print(f"LOW STOCK: {product['name']} - Only {product['quantity']} left!")

  # Searching for a product by name
while True:
    search_name = input("\nEnter the product name to search for (or type 'exit' to quit): ").strip()              # the strip() method removes unnedessary spaces from begining and end of user's input

    if search_name.lower() == "exit":
        print("Thank you for using the Business Record Checker!")
        break
    if search_name.strip() == "":                      # To handle empty input
        print("Please enter a product name.")
        continue

    found = False

    for product in products:
        if product["name"].lower() == search_name.lower():
            found = True
            print(f"Product found: {product['name']}")
            print(f"Unit price: ₦{product['price']:,}")
            print(f"Quantity in stock: {product['quantity']}")
            print(f"Stock value: ₦{product['price'] * product['quantity']:,}")

    if not found:
     print(f"Sorry, {search_name} was not found in the inventory.")

   # Stock movement
while True:
    print("\n--- STOCK UPDATE ---")
    print("1. Stock In (New stock received)")
    print("2. Stock Out (Stock sold)")
    print("3. Exit")

    stock_choice = input("Choose an option (1, 2 or 3): ")
    if stock_choice == "3":
        print("Thank you for using the Business Record Checker!")
        break

    if stock_choice not in ("1", "2"):
        print("Invalid option. Please choose 1 or 2 or 3.")
        continue
    product_name = input("Enter the product name: ").strip()

    product_found = False

    for product in products:
        if product["name"].lower() == product_name.lower():
            product_found = True
            print(f"Selected product: {product['name']}")
            print(f"Current quantity: {product['quantity']}")
            break

    if not product_found:
        print("Product not found in inventory.")
        continue
    if product_found:
        while True:
            quantity_input = input("Enter the quantity: ")
            if not quantity_input.isdigit():
                print("Error: Please enter a whole number.")
                continue
            quantity = int(quantity_input)

            if quantity <= 0:
                print("Error: Quantity must be greater than zero.")
            else:
                break
        if stock_choice == "1":
            product["quantity"] += quantity
            print(f"Stock updated! New quantity: {product['quantity']}")
            save_inventory()
        elif stock_choice == "2":
            if quantity <= product["quantity"]:
                product["quantity"] -= quantity
                print(f"Stock updated! New quantity: {product['quantity']}")
                save_inventory()
            else:
                print("Error: Not enough stock available.")

        else:
            print("Invalid option. Please choose 1 or 2.")
    

