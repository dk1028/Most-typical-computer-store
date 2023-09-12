class Computer:
    # Class variable to keep track of number of created objects
    num_computers = 0

    def __init__(self, brand, model, sn, price):
        self.brand = brand
        self.model = model
        self.sn = sn
        self.price = price
        Computer.num_computers += 1

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, SN: {self.sn}, Price: {self.price}"

    def __eq__(self, other):
        if isinstance(other, Computer):
            return self.brand == other.brand and self.model == other.model and self.price == other.price
        return False

    @classmethod
    def findNumberOfCreatedComputers(cls):
        return cls.num_computers

def display_menu():
    print("What do you want to do?")
    print("1. Enter new computers (password required)")
    print("2. Change information of a computer (password required)")
    print("3. Display all computers by a specific brand")
    print("4. Display all computers under a certain price")
    print("5. Quit")


def enter_new_computers(password, inventory):
    # Check password
    if password != "sibalsekiya":
        print("Incorrect password!")
        return

    # Prompt user for number of computers to add
    num_computers = int(input("Enter the number of computers to add: "))
    if num_computers < 0:
        print("Negative number.")
        return

    # Add new computers to inventory
    for i in range(num_computers):
        brand = input("Enter the brand of the computer: ")
        model = input("Enter the model of the computer: ")
        sn = int(input("Enter the serial number of the computer: "))
        price = float(input("Enter the price of the computer: "))
        inventory.append(Computer(brand, model, sn, price))
        print("Computer added successfully!")


def change_computer_info(password, inventory):
    # Check password
    if password != "sibalsekiya":
        print("Incorrect password!")
        return

    sn = int(input("Enter the serial number of the computer to modify: "))
    for computer in inventory:
        if computer.sn == sn:
            # Prompt user for new information
            brand = input("Enter the new brand of the computer: ")
            model = input("Enter the new model of the computer: ")
            price = float(input("Enter the new price of the computer: "))

            # Update computer information
            computer.brand = brand
            computer.model = model
            computer.price = price

            print("Computer information updated.")
            return

    print("Computer not found.")


def display_computers_by_brand(inventory):
    brand = input("Enter the brand of the computers to display: ")
    found = False
    for computer in inventory:
        if computer.brand == brand:
            print(computer)
            found = True

    if not found:
        print("No computers found with that brand.")


def display_computers_under_price(inventory):
    price = float(input("Enter the maximum price of the computers to display: "))
    found = False
    for computer in inventory:
        if computer.price <= price:
            print(computer)
            found = True

    if not found:
        print("No computers found under that price.")



def main():
    print("Welcome to the computer store.")
    n = int(input("Enter the maximum number of computers your store can contain: "))
    inventory = []
    if n < 0:
        print("Negative number.")
        return
    while True:
        display_menu()
        choice = input("Please enter your choice: ")
        if choice == "1":
            password = input("Enter the password: ")
            enter_new_computers(password, inventory)
        elif choice == "2":
            password = input("Enter the password: ")
            change_computer_info(password, inventory)
        elif choice == "3":
            display_computers_by_brand(inventory)
        elif choice == "4":
            display_computers_under_price(inventory)
        elif choice == "5":
            print("Thank you for using the computer store system.")
            break
        else:
            print("Incorrect choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
