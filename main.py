import json

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f'{self.name} - ${self.price}'

class Electronic(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty

    def get_info(self):
        return f'{self.name} ({self.brand}) - ${self.price}, Warranty: {self.warranty} years'

class HomeAppliance(Product):
    def __init__(self, name, price, power):
        super().__init__(name, price)
        self.power = power

    def get_info(self):
        return f'{self.name} - ${self.price}, Power: {self.power}W'

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_cart(self):
        total = 0
        for item in self.items:
            print(item.get_info())
            total += item.price
        print(f'Total: ${total}')

class ItemNotAvailableError(Exception):
    pass

def load_products(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f'Error: {e}')
        return []

def create_products(data):
    products = []
    for p in data:
        if p['type'] == 'electronic':
            products.append(Electronic(p['name'], p['price'], p['brand'], p['warranty']))
        elif p['type'] == 'home_appliance':
            products.append(HomeAppliance(p['name'], p['price'], p['power']))
        else:
            products.append(Product(p['name'], p['price']))
    return products

def main():
    print("Welcome to the Store!")
    products_data = load_products('products.json')
    if not products_data: return
    products = create_products(products_data)
    cart = ShoppingCart()

    while True:
        print("\n1. Show products\n2. Add to cart\n3. Show cart\n4. Exit")
        choice = input("Choice: ")

        if choice == '1':
            for i, p in enumerate(products):
                print(f'{i + 1}. {p.get_info()}')
        elif choice == '2':
            try:
                num = int(input("Product number: ")) - 1
                if num < 0 or num >= len(products): raise ItemNotAvailableError
                cart.add_item(products[num])
                print(f'Added {products[num].name}')
            except (ValueError, ItemNotAvailableError):
                print("Invalid selection.")
        elif choice == '3':
            cart.show_cart()
        elif choice == '4':
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
