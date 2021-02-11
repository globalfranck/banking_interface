# Bank project
# Creating a menu: new customer, existing customer and exit the program

bank_logo = " -------------------- \n --- Bank and Co. --- \n -------------------- \n "
menu = "1) New customer \n 2) Existing customer \n 3) Exit program \n Enter your choice : "

# Bank data
data = {}

# Standard required information in a bank account represented as a list
standard_bank_info =["Name","Adress","Phone number","Gov ID", "Account Type","Amount"]


while True:

    # clearing the list every time we get an input
    list2 =[]

    # asking input from the user
    user_choice=int(input(bank_logo + menu))

    # New customer
    if user_choice == 1:
        # customer chooses the account number
        acc_num = input("Enter your account number: ")

        # We loop over the list and prompt the user to give us the required information to open an account
        for i in standard_bank_info :
            list2.append(input("Enter {i}"))
