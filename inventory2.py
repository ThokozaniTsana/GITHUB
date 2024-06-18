class Shoe:
    # constructing an initializer to assign values.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    # defining methods
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        class_str_repr = f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"
        return class_str_repr

# Create an empty shoe_list
shoe_list = []

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # skip the header row
            for line in file:
                data = line.strip().split(",")
                shoe = Shoe(*data)
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("File not found")

def capture_shoe():  # defining a function to capture shoe data.
    country = input("Enter the country of manufacture: ")
    code = input("Enter the code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

def view_all():  # defining a function to view all shoe data.
    for shoe in shoe_list:
        print(shoe.__str__())

def re_stock():  # defining a function to restock minimum shoe stock.
    # find shoe with minimum quantity
    lowest_qty_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"The shoe with the lowest quantity is: {lowest_qty_shoe}")
    add_qty = input("Do you want to add quantity to this shoe? (y/n): ")
    if add_qty.lower() == "y":
        qty_to_add = int(input("Enter the quantity to add: "))
        lowest_qty_shoe.quantity += int(qty_to_add)

        # update file
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
        with open("inventory.txt", "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[1] == lowest_qty_shoe.code:
                    data[-1] = str(lowest_qty_shoe.quantity)
                    line = ",".join(data) + "\n"
                file.write(line)
        print("Quantity has been updated on the inventory file.")
    else:
        print("Quantity has not been updated.")

def search_shoe():  # defining the search shoe function.
    code = input("Enter the shoe code: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(f"The shoe with code {code} is: {shoe}")
            break
    else:
        print(f"Shoe with code {code} not found.")

def value_per_item():  # defining the value per item function.
    print("Value per item:")
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} - {value}")

def highest_qty():
    highest_qty_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"The shoe for sale with highest quantity is: {highest_qty_shoe}")

# defining the main menu using a while loop
def main_menu():
    read_shoes_data()  # Call the function before entering the menu loop

    while True:
        print("\n==========Main Menu=============")
        print("1. Capture the shoe data")
        print("2. View all the shoes")
        print("3. Restock minimum quantity shoes")
        print("4. Search for a shoe")
        print("5. Calculate the value per item")
        print("6. Find product with highest quantity")
        print("7. Exit the menu")

        option = input("Enter a number from the main menu: ")

        # use if-else statements
        if option == "1":
            capture_shoe()

        elif option == "2":
            view_all()

        elif option == "3":
            re_stock()

        elif option == "4":
            search_shoe()

        elif option == "5":
            value_per_item()

        elif option == "6":
            highest_qty()

        elif option == "7":
            print("Exiting the menu")
            break

        else:
            print("Invalid selection, please try again")

# call the main function to execute the program
main_menu()