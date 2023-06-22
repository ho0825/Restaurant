
def customerOrderPlacement (Order_num):
    Order_Method_list = ["dinein", "takeout", "delivery"]
    print ("Would you like to\n1) Dine in\n2) Takeout\n3) Delivery\n4) Back")
    cat_list = [0,1,2,3]
    choice = int (input ())
    if (choice == 4):
        return
    Order_Method = Order_Method_list[choice]
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
            quantity = int(input("Quantity: "))
            Order_Status = -1
            while (Order_Status != 0 and Order_Status != 1):
                Order_Status = int(input("Continue to order in this category?: "))
        category = -1


def book_table ():

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
        temp1 = " "
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
    j =1
    while (j == 1):
        print ("1) Booking a table\n2) Waiting List\n3) Next waiting customer\n4) Waiting list\n5) Back")
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

temp_list = list ()
detail = list ()
customer = list()
reservation = dict ()
waiting = dict ()
Order_taken = 0
table_reservation ()
customerOrderPlacement (Order_taken)
