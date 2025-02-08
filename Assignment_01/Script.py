class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity
        print(f"Stock updated successfully! New stock: {self.stock}")

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock}"


class Store:
    def __init__(self):
        self.products = {}

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        self.products[name] = Product(name, price, stock)
        print("Product added successfully!")

    def update_product_stock(self):
        name = input("Enter product name to update: ")
        if name in self.products:
            quantity = int(input("Enter quantity to add/remove: "))
            self.products[name].update_stock(quantity)
        else:
            print("Product not found.")

    def view_product_details(self):
        name = input("Enter product name: ")
        if name in self.products:
            print(self.products[name])
        else:
            print("Product not found.")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Add a new product")
            print("2. Update product stock")
            print("3. View product details")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.update_product_stock()
            elif choice == '3':
                self.view_product_details()
            elif choice == '4':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

store = Store()
store.run()
