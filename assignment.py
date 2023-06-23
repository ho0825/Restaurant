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

    def Ordering (self, category, item):
        self.list = list ()
        if category == 1:
            self.FOOD = self.food[item-1]
            for i in self.FOOD:
                if (i != "" and i != "*"):
                    self.list.append (i)

            return self.list
        else:
            self.BEVERAGE = self.beverage[item-1]
            for i in self.BEVERAGE:
                self.list.append (i)
            return self.list

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

    def display_menu (self, category):
        self.category = category
        if (self.category == 1):
            print("\n------Food Menu------")
            print("Remark '*' = Spicy food\n")
            for (name, remark, price) in self.food:
                print (f"{name} {remark}: RM {price}")

        elif (self.category == 2):
            print("\n-----Beverage Menu-----")
            for (name, price) in self.beverage:
                print(f"{name} : RM {price}")


class Restaurant ():
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



def customerOrderPlacement (Order_num, table_list, takeout_list):

    Food_List = list ()
    Price_List = list ()
    Quantity_List = list ()

    print ("Would you like to\n1) Dine in\n2) Takeout\n3) Back")

    OrderMethod = int (input ("Select an option:"))

    if OrderMethod == 1:
        while True:
            print ("Occupied Table: ", table_list)
            Tablenum = int(input ("Enter table number: "))
            if Tablenum not in table_list:
                break

    if (OrderMethod == 3):
        return

    End_Order = 0
    category = -1

    while (End_Order != 1):
      #  category = int (input (""))
        category = int (input("Select a category to order \n1. Food\n2. Beverage\n3. Check Order\n4. Delete Item\n5. End Order\n6. Exit\n"))
        if category == 3:
            display_order_list (Food_List, Price_List, Quantity_List)
            continue
        elif category == 4:
            display_order_list (Food_List, Price_List, Quantity_List)
            delete_item (Food_List, Price_List, Quantity_List)
            continue
        elif category == 5:
            break
        elif category == 6:
            return
        Order_Status = 1
        while (Order_Status == 1):

            restaurant.menu.display_menu (category)
            foodChoice = int(input("Choose a food you want to order / choose 0 to back: "))
            if (foodChoice == 0):
                break
            quantity = int(input("Quantity: "))
            dishes, price = restaurant.menu.Ordering (category, foodChoice)
            Food_List.append (dishes)
            Price_List.append (price*quantity)
            Quantity_List.append (quantity)


            Order_Status = -1
            while (Order_Status != 0 and Order_Status != 1):
                Order_Status = int(input("Continue to order (0: back, 1: continue) ? : "))



    confirmChoice = int(input("Confirm the order (press 1 to confirm) ?\n"))
    if (confirmChoice != 1):
        print ("Invalid input")
    elif (confirmChoice == 1):
        if (OrderMethod == 1):
            updateFile (OrderMethod, Food_List, Price_List, Quantity_List, Order_num, Tablenum)
            table_list.append(Tablenum)
        else :
            updateFile (OrderMethod, Food_List, Price_List, Quantity_List, Order_num)
            takeout_list.append (Order_num)
        return int (Order_num) + 1


def delete_item (Food_List, Price_List, Quantity_List):
    if len (Food_List) == 0:
        print ("No item to delete")
        return
    deleteChoice = int (input ("Which item would you like to delete?:\n"))
    if deleteChoice >0 and deleteChoice <= (len(Food_List)):
        del Food_List [deleteChoice-1]
        del Price_List [deleteChoice-1]
        del Quantity_List [deleteChoice-1]
    else:
        print ("Invalid input")


def display_order_list (Food_List, Price_List, Quantity_List):
    print (f'No.\t Items\t\t         ----->\tQuantity , Price')
    for i in range (len(Food_List)):
        print (i+1,"\t","%.20s" % Food_List[i],"\t\t-->\t", Quantity_List[i]," , ", "%.2f" % Price_List[i])


def updateFile (OrderMethod, Food_List, Price_List, Quantity_List, Order_num, Tablenum = 0):
    if OrderMethod == 1:
        fileName = "T" + str(Tablenum) + ".txt"
        file = open (fileName, "w")

    elif OrderMethod == 2:
        fileName = str(Order_num) + ".txt"
        file = open (fileName, "w")

    for i in range (len(Food_List)):
            file.write (Food_List [i] + "\n" + str (Quantity_List[i]) + "\n" + str(Price_List [i]) + "\n")
    file.close ()

def book_table ():

    temp_list = list ()

    choice = int(input ("Reservation Section:\n1)Reserve Table\n2)Check Reservation\n3)Remove Reservation\n4)Back\n"))
    if (choice == 1):
        username = input("Enter your name: ")
        phone = input("Phone Number: ")
        time = input ("Time: ")
        date = input ("Date: ")
        ptd = phone + "   " + time + "   " + date
        reservation [username] = ptd
        file = open ("Reservation.txt", "a")
        for i in reservation:
            print (i, reservation[i])
            file.write (i)
            file.write ("\n")
            file.write (reservation [i])

    elif (choice == 2 or choice == 3):
        file = open ("Reservation.txt", "r")
        while (True):
            list_of_reservation = file.readline().splitlines ()
            if len (list_of_reservation) == 0:
                break
            temp_list.append(list_of_reservation)
        file.close ()
        for i in range(len(temp_list)):
            temp = temp_list [i][0]
            if (i%2 == 0):
                customer.append (temp)
                continue
            else:
                detail.append (temp)

        for i in range (len(customer)):
            print (customer[i], detail [i])

        if (choice == 3):
            delete_choice = int (input ("Which reservation you want to delete from the list?:"))
            del customer [delete_choice]
            del detail [delete_choice]
            file = open ("Reservation.txt", "w")
            for i in range (len(customer)):
                file.write (customer[i])
                file.write ("\n")
                file.write (detail [i])
                if i == (len (customer) -1):
                    file.write ("\n")

    file.close ()

def Waiting_list ():

    username = input("Enter your name: ")
    pax = input ("Enter number of person: ")
    waiting [username] = pax

def Eject_waiting ():

    for i in waiting:

        print (i , waiting [i])
        del waiting [i]
        return


    print ("no customer in pending")

def Check_Waiting ():

    if not waiting:
        print ("no customer in pending")
    for i in waiting:
        print (i , waiting [i])
    else:
        return


def table_reservation ():
    while True:
        print ("1) Booking a table\n2) Waiting List\n3) Next waiting customer\n4) Check Waiting list\n5) Back")
        choice = int(input ("Select an option: "))

        if (choice == 1):
            book_table ()
        elif (choice == 2):
            Waiting_list ()
        elif (choice == 3):
            Eject_waiting ()
        elif (choice == 4):
            Check_Waiting ()
        elif (choice == 5):
            return
        else:
            print ("Invalid Input")

def pending_order (table_list, takeout_list):
    while True:
        print ("1. Check for available order pending\n2. Delete order\n3. Back\n")
        pendingChoice = int (input ("Select an option:\n"))
        if pendingChoice == 1:
            Check_pending (table_list, takeout_list)

        elif pendingChoice == 2:
            Delete_pending (table_list, takeout_list)

        elif pendingChoice == 3:
            return

        else:
            print ("Invalid Input")


def Check_pending (table_list, takeout_list):

    temp_list = list ()
    foodItem = list ()
    quantityItem = list ()
    priceItem = list ()

    print ("1. Dine\n2. Takeout\n")
    checkOption = int(input("Select an option:"))
    if checkOption == 1:
        print (table_list)
        TableNum = int (input ("Select a table number:"))
        if TableNum in table_list:
            fileName = "T"+TableNum+".txt"
            file.open (fileName, "r")
            while (True):
                list_from_file = file.readline().splitlines ()
                if len (list_from_file) == 0:
                    break
                temp_list.append(list_from_file)
                num = 1
                for i,j,k in range(len(temp_list)):

                    print (f"{no}\t{i}\t{j}\t{k}")


'''
                    temp = temp_list [i][0]
                    foodItem.append (temp)
                    temp = temp_list [j][0]
                    quantityItem.append (temp)
                    temp = temp_list [k][0]
                    priceItem.append (temp)
'''

    #elif checkOption == 2:

def Delete_pending ():
    pass
#variables initialization


detail = list ()
customer = list()
table_list = list ()
takeout_list = list ()
reservation = dict ()
waiting = dict ()
Order_num = 1
list_of_mainChoice = [1,2,3,4,5,6]

restaurant = Restaurant()



while True:
    print ("Main Menu:\n1) Order\n2) Table Reservation\n3) Check List of Order\n4) Payment\n5) Menu\n6) Print Report\n7) Exit")
    mainChoice = int (input ("Select an option:"))

    if mainChoice == 1:
        Order_num = customerOrderPlacement (Order_num, table_list, takeout_list)
    elif mainChoice == 2:
        table_reservation ()
    elif mainChoice == 3:
        pending_order (table_list, takeout_list)
    elif mainChoice == 5:
        restaurant.main()
    elif mainChoice == 7:
        break

    if mainChoice not in list_of_mainChoice:
        print ("Invalid Input")


