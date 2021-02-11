# Bank project
# Creating a menu: new customer, existing customer and exit the program

bank_logo = " -------------------- \n --- Bank and Co. --- \n -------------------- \n "
menu = "1) New customer \n 2) Existing customer \n 3) Exit program \n Enter your choice : "
hyphens = " -------------------- \n"

# Bank data, used to store bank details
data = {}

# Standard required information in a bank account represented as a list
standard_bank_info =["Name", "Adress", "Phone number", "Gov ID", "Account Type", "Amount"]

# Creating a function that takes data from user and stores it for new customer
def store_data():
    # We create a new account number using the customer input
    account_number = input("Enter your account number: ")

    # We loop over the standard banking info list and prompt the user to give us the required details to open an account and then add this information
    for i in standard_bank_info :
        user_details.append(input(f"Enter {i}: "))

    # STORING DATA
    # We store the info into a dictionary using the zip function to map and combine standard bank info with user details
    data[account_number] = dict(zip(standard_bank_info, user_details))
    print(f"Account n° {account_number} was created.")
    print(hyphens)
    return 

# Creating a function that ask an existing customer the options he'd like to choose
def other_options():
    print(hyphens)
    customer_option = int(input("1. Check Balance \n2. Withdraw\n3. Deposit\nEnter choice: "))
    
    # User wants to see the current balance
    if customer_option == 1:
        print("Current balance available: ", data[account_number]["Amount"])
        print(hyphens)

    # User wants to withdraw money
    elif customer_option == 2:
        withdraw_amount = int(input("Enter amount to withdraw: "))
        # Converting the amount in the dictionary into a number
        data[account_number]["Amount"] = int(data[account_number]["Amount"])
        data[account_number]["Amount"] -= withdraw_amount
        print(hyphens)
        print("Withdraw successful")
        print("New balance is: ", data[account_number]["Amount"])
        print(hyphens)

    # User wants to deposit money
    else:
        deposit_amount = int(input("Enter amount to deposit: "))
        # Converting the amount in the dictionary into a number
        data[account_number]["Amount"] = int(data[account_number]["Amount"])
        data[account_number]["Amount"] += deposit_amount
        print(hyphens)
        print("Deposit successful")
        print("New balance is: ", data[account_number]["Amount"])
        print(hyphens)


while True:
    # We will store into this list the input details from the client
    user_details = []

    # Showing menu and asking for the user choice
    user_choice = int(input(bank_logo + menu))

    # New customer
    if user_choice == 1 :
        store_data()

    # Existing customer
    elif user_choice == 2 :
        account_number = input("Enter your account number: ")
        if account_number in data:
            print("Record found.")
            # Showing options to the user
            other_options()
        else:
            print("Record not found.")
    else:
        break
