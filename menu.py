class Menu:
    def __init__ (self):
        self.food = [("Tom Yam Seafood","*",28.90), ("Fish n Chips","",38.90),("Nasi Lemak Ayam","*",22.90),("Chicken Chop","",35.90)]
        self.beverage = [("Limau Ais", 78.90), ("Bandung Ais", 88.90), ("Teh Ais", 98.90)]

    def add_food (self, categories, name, remark, price):
        if categories == "food":
            self.food.append((name, remark, price))
        else:
            return ("Invalid choice")

    def add_beverage (self, categories, name, price):
        if categories == "beverage":
            self.beverage.append((name, price))
        else:
            return ("Invalid choice")

    def delete_menu (self, categories, name):
        if categories == "food":
            for dish in self.food:
                if dish[0] == name:
                    self.food.remove(dish)
                    break

        elif categories == "beverage":
            for drink in self.beverage:
                if drink[0] == name:
                    self.food.remove(drink)
                    break
        else:
            return "This category is not available"

    def display_menu (self):
        print("\n------Food Menu------")
        print("Remark '*' = Spicy food\n")
        for (name, remark, price) in self.food:
            print(f"{name} {remark}: RM {price}")

        print("\n-----Beverage Menu-----")
        for (name, price) in self.beverage:
            print(f"{name} : RM {price}")


class Restaurant:
    def __init__(self):
        self.menu = Menu()
        self.waiter_authenticated = False

    def main(self):
        print("\n***Welcome to Restaurant M-01***\n")
        print("1. Customers")
        print("2. Waiters")
        print("3. Exit\n")
        choice = input("Please enter your choice (1-3):")

        if choice == "1":
            self.customer_ui()
        elif choice == "2":
            self.waiter_ui()
        elif choice == "3":
            return
        else:
            return ("Invalid choice")

    def customer_ui(self):
        self.menu.display_menu()
        print()
        exit = input("Exit to main page (Y):")

        if exit == "Y" or "y":
            self.main()

    def waiter_ui(self):
        if not self.waiter_authenticated:
            password = input("Please enter password:")
            if password == "123456":
                self.waiter_authenticated = True
            else:
                print("Invalid password")
                self.main()

        print("\n---Welcome to waiter interface---\n")
        print("1. Add food into menu")
        print("2. Add beverage into menu")
        print("3. Delete item in menu")
        print("4. View menu")
        print("5. Exit\n")
        waiter_choice = input("Please enter your choice (1-4):")

        if waiter_choice == "1":
             self.add_food()
        elif waiter_choice == "2":
             self.add_beverage()
        elif waiter_choice == "3":
            self.menu.display_menu()
            self.delete()
        elif waiter_choice == "4":
            self.menu.display_menu()
            exit = input("Exit to waiter interface (Y):")
            if exit == "Y" or "y":
                self.waiter_ui()
        elif waiter_choice == "5":
            self.waiter_authenticated = False
            self.main()
        else:
            print("Invalid choice")

    def add_food(self):
        print("\nAdd new dish into menu")
        category = "food"
        name = input("Enter the name of the new dish:")
        remark = input("If spicy enter '*':")
        price = float(input("Enter the price of the new menu:"))
        self.menu.add_food(category, name, remark, price)
        print(f"{name} is added into the food menu")
        self.waiter_ui()

    def add_beverage(self):
        print("\nAdd new beverage into menu")
        category = "beverage"
        name = input("Enter the name of the new beverage:")
        price = float(input("Enter the price of the new menu:"))
        self.menu.add_beverage(category, name, price)
        print(f"{name} is added into the beverage menu")
        self.waiter_ui()

    def delete(self):
        print("\nDelete item in menu")
        category = input("Please choose menu categories (food/beverage):")
        name = input("Enter the name of the food or beverage:")
        self.menu.delete_menu(category, name)
        print(f"{name} is removed from the {category} menu")
        self.waiter_ui()

restaurant = Restaurant()
restaurant.main()

