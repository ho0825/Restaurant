
class Order:
    def __init__ (self, choice):
        self.choice = choice
        self.food = []

    def listOfItem (self, food):
        self.food.append (food)


    def __str__ (self):
        return

def customerOrderPlacement (Order_num):
    Order_Method_list = ["dinein", "takeout", "delivery"]
    print ("Would you like to\n1) Dine in\n2) Takeout\n3) Delivery\n4) Back")
    cat_list = [0,1,2,3]
    choice = int (input ())
    if (choice != 4):
        Order_Method = Order_Method_list[choice]
        Odering = Order (choice)
        Order_num += 1
        End_Order = 0
        category = -1
        while (End_Order != 1):
            #show category
            while category not in cat_list:
                category = int(input("Please choose a food category: "))
            if (category == 0):
                End_Order = 1
                Order_Status = 0
            else:
                Order_Status = 1

            while (Order_Status == 1):
                #show menu
                food = int(input("Choose a food you want to order: "))
                portion = int(input("Select the portion: "))
                quantity = int(input("Quantity: "))
                Order_Status = -1
                while (Order_Status != 0 and Order_Status != 1):
                    Order_Status = int(input("Continue to order in this category?: "))
            category = -1


def table_reservation ():
    print ("1) Booking a table\n2) Waiting List\n3) Back")
    if ()




Order_taken = 0
customerOrderPlacement (Order_taken)







