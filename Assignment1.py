# Create an Inventory Management - Use Loops to display a list of stock items 
inventory_list = [
    {"item": "Sugar", "quantity": 10, "price": 3500},
    {"item": "Salt", "quantity": 8, "price": 800},
]

# Display Inventory
print("Shop Inventory")
for product in inventory_list:
    print(f"Item: {product['item']}, Quantity: {product['quantity']}, Price: ${product['price']}")
