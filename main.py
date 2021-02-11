# Bank project
# Creating a menu: new customer, existing customer and exit the program

bank_logo = " -------------------- \n --- Bank and Co. --- \n -------------------- \n "
menu = "1) New customer \n 2) Existing customer \n 3) Exit program \n Enter your choice : "
hyphens = " -------------------- \n"

# Bank data, used to store bank details
data = {}

# Standard required information in a bank account represented as a list
standard_bank_info =["Name", "Adress", "Phone number", "Gov ID", "Account Type", "Amount"]

# Creating a function that takes data from user and stores it
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

while True:
    # We will store into this list the input details from the client
    user_details = []

    # Showing menu and asking for the user choice
    user_choice = int(input(bank_logo + menu))

    # New customer
    if user_choice == 1 :
        store_data()
