
"""
Created on Wed Dec  4 13:06:27 2024

@author: Matthew Flores
"""
from datetime import datetime

products = {
    '1': {'Product': 'Coke', 'price': 1.50, 'quantity': 5},
    '2': {'Product': 'Doritos', 'price': 1.00, 'quantity': 5},
    '3': {'Product': 'Breaks', 'price': 1.75, 'quantity': 5},
   
}
 
def menu():
    while True:
        display_products()
        selected_code = input("Enter product unique code (or 'exit' to quit): ").strip().upper()

        if selected_code == 'EXIT':
            print("Thank you for using the vending machine. Goodbye!")
            break

        product = select_product(selected_code)

        if product:
            process_payment(product)

def display_products():
    print("\nAvailable Products:")
    for code, product in products.items():
        if product['quantity'] > 0:
            print(f"{code}: {product['Product']} - ${product['price']:.2f} (Available: {product['quantity']})")

def select_product(code):
    if code in products and products[code]['quantity'] > 0:
        return products[code]
    else:
        print("Invalid product uc or out of stock.")
        return None

def process_payment(product):
    amount_inserted = float(input(f"Insert money for {product['Product']} (${product['price']:.2f}): $"))
    if amount_inserted >= product['price']:
        product['quantity'] -= 1
        change = amount_inserted - product['price']
        print("//////////"f"Dispensed: {product['Product']}. Change: ${change:.2f}. Thank you!","//////////")
        print ("//////////","Keep Receipt in case of refund! :3", "////////////////")
        print("//////////",f"Transaction Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}","////////////")
    else:
        print("//////////","Insufficient funds. Transaction cancelled.","//////////")



if __name__ == "__main__":
    menu()
    

