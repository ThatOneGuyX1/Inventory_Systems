""""
Project Name: Huracan Point of Sale Software
Author: Ian Jon Searle
Version: 0.01.9 
Summary:
    This program is desinged for use in a retail enviorment, specificaly targeted toward one single store where I use to work.
    Keeping in mind the needs of the store I designed a software that would track the inventory. Some features such as inventory counting,
    location tracking, and a delivery board have yet to be implemented. This version of the program was more a proof of concept and 
    to strech my skills to see if I could get it working with a basic terminal. Later version will incude a GUI and the features mentioned previsouly.
    This system is designed for a cashier to use.

"""

import csv
import random
from datetime import datetime

# Indexs for Item Inventory
MODEL_INDEX = 0
SERIAL_INDEX = 1  
PRICE_INDEX = 2
RECIVED_INDEX = 3 
LOCATION_INDEX = 4

# Indexes for the Customer Account List
ACCOUNT_NUM_INDEX = 0
ACCOUNT_NAME__INDEX = 1
ACCOUNT_PHONE_NUM_INDEX = 2
ACCOUNT_EMAIL_INDEX =3
ACCOUNT_ADDRESS_INDEX = 4
ACCOUNT_BAL_INDEX = 5

# Function list
''' File Functions'''

def open_file(filename,key_column_index):
    """ 
    Paramaters: filename: the name of the file to open
                key_column_index: the index of the key value

    Returns: dictionary: the data of the file 
    
    Purpose: Opens a file and stores the data into a dictionary that is then returned to the main program
    """
    dictionary = {} # Creates a temp diction

    with open(filename, "r", encoding='utf-8') as csv_file: # OPens the target file 
        reader = csv.reader(csv_file) 
        next(reader) # Skips the header

        for row_list in reader: # For each row in the file will create an entry into the dictionary
          if len(row_list) != 0:
            key = row_list[key_column_index]
            dictionary[key] = row_list

    csv_file.close()
    return dictionary

def update_file(filename, dict,header):
    """ 
    Paramaters: filename: the name of the file to open and update
                dict: the data to be stored
                header: The header of the file 

    Returns: Nothing

    Purpose: Stores the value of a dictionary to a file to be reused in at a later time.
    
    A small interesting thing I noticed was that if I made the header a variable I would be able to use the same
    function (update_file) for both files. Orgianaly I had two seperate function for each file but was able to combine them.
    """
    with open(filename, 'w',encoding='utf-8') as f:
        
        writer = csv.writer(f)
        writer.writerow(header)
        for key, item in dict.items():
            writer.writerow(item)

    f.close()

'''Item Functions'''
def create_item(item_inventory):
    '''
    Paramaters: item_inventory: the dictionary of where it will store the item creates

    Returns: Nothing

    Purpose: Creates an item and stores it in the master item_inventory dictionary. 
    '''

    item =[] # Creates a temperoray list 

    item.append(str(input("MODEL:")))
    item.append(str(input("SERIAL: "))) # The serial number acts a unique key beacuse no two items have the same Serial number.
    item.append(float(input("PRICE:")))
    item.append(get_date())

    item_inventory[item[SERIAL_INDEX]] =  item # Stores list into main dictionary
    
def display_item(item_list):
    '''
    Paramaters: item: the list portion of an item in item_inventory

    Returns: Nothing

    Purpose: Prints out the data for an indiviudal item. This function was designed in this way in case I wanted to 
            later print out a specfic item and not have to call the whole list.
    '''
    print(f'MODEL: {item_list[MODEL_INDEX]} :: SERIAL:{item_list[SERIAL_INDEX]}')

def get_date():
    '''
    Paramaters: NONE

    Returns: today: date formated as YYYY/MM/DD

    Purpose: Creates the date for the date an item recived. The idea is that will allow us to track when items come in as well as
             helps ensure that the invenory is being well cycled and older items are not being sold before and older model.
    '''
    cday = str(datetime.now().day)
    cmonth = str(datetime.now().month)
    cyear = str(datetime.now().year)
    today = cyear +"/" + cmonth + "/" + cday
    return today

def display_inventory(item_inventory):
    '''
    Paramaters: item_inventory: the main invenotry dictionary

    Returns: Nothing

    Purpose: Cycles trough the master invenotry dictionary and pass it to the display_item function. This is not a needed function but
             allows for the display_item function to be called seperatly.
    '''
    for item in item_inventory:
        display_item(item_inventory[item])

def delete_item(key_value,item_inventory):
    '''
    Paramaters: key_value: the target Key value to be deleted 

    Returns: Nothing

    Purpose: Removes an item from the dictionary
    '''
    item_inventory.pop(key_value)

''''Customer Functions'''
def create_customer(cust_list):
    customer = []
    acc_num = create_account_number(cust_list)
    #ACCOUNT NUMBER,NAME,PHONE NUMBER,EMAIL,ADDRESS,BALANCE
    name = str(input("Customer Name: "))
    phone_number = str(input("Customer Phone Number: "))
    email = str(input("Customer Email: "))
    address = str(input("Customer Adress: "))
    bal = 0.00 
    customer.append(acc_num)
    customer.append(name)
    customer.append(phone_number)
    customer.append(email)
    customer.append(address)
    customer.append(bal)

    cust_list[customer[ACCOUNT_NUM_INDEX]] = customer
    print(customer)

def create_account_number(cust_list):
    # Account number is 1 + a number
    num = 1
    while num == 1:
        rand = random.randint(0,10000)

        temp_num = rand + 1
        if temp_num not in cust_list:
            num = temp_num

    return str(num)

def display_customers(customer_list):
    for key in customer_list:
        customer = customer_list[key]
        print(f"NAME: {customer[ACCOUNT_NAME__INDEX]}")
        print(f"ACC_NUM: {customer[ACCOUNT_NUM_INDEX]}")
        print(f"BALANCE {float(customer[ACCOUNT_BAL_INDEX]):.2f}")
        print()

'''Point of Sale Functions'''
def create_quote(inventory,cust_list):
    choice = 1
    cart = {}
    x = None
    customer = None
    shop = 1
    count = 0
    subtotal = 0.00

    #Selects the customer
    x = int(input("Do you need to create a new customer? 1. Yes 2. No "))
    if x == 1:
        create_customer(cust_list)
    acc_num = str(input("What is the account number?"))
    if acc_num in cust_list:
        customer = cust_list[acc_num]

    #Create the Items in the cart
    while shop == 1:
        count +=1
        model = str(input("What model do you want to purchase?"))
        for item in inventory:
            if model in inventory[item]:
                cart[count] = inventory[item]
                delete_item(item,inventory)
                break
        shop = int(input("Would you like to countine shopping? 1. Yes 0.no "))

    # Calculate the Total
    for key in cart:
        item = cart[key]
        subtotal += (float(item[PRICE_INDEX ]) / .75)
    total = subtotal * 1.06
    customer[ACCOUNT_BAL_INDEX] = total
    cust_list[acc_num] = customer

def take_payment(customer_list):
    bal = None

    target = input("What is the account number?")
    if target in customer_list:
        bal = float(customer_list[target][ACCOUNT_BAL_INDEX])
        print(f'BALANCE: ${bal:.2f}')
        payment = float(input("How much is the payment? $"))
        if payment <= bal:
            bal -= payment
        elif bal < payment:
            change = payment - bal
            bal = 0.000
            print(f'Change: ${change:.2f}')
        print(f'BALANCE: ${bal:.2f}')
        customer_list[target][ACCOUNT_BAL_INDEX] = bal

'''OTher Function'''
def display_menu():
    print("-----------------------------------------------")
    print("1. Create Item")
    print("2. Display Inventory")
    print("3. Create Customer")
    print("4. Display Customers")
    print("5. Create Sale")
    print("6. Payments")

def main():
    #setup main varibale
    choice =99999
    item_inventory = open_file("huracan_inventory.csv", SERIAL_INDEX)
    customer_list = open_file("all_customers.csv", ACCOUNT_NUM_INDEX)

    while choice !=0:
        display_menu()
        choice = int(input("SELCTION: "))
        print("-----------------------------------------------")
        if choice == 1:
            create_item(item_inventory)
        elif choice == 2:
            display_inventory(item_inventory)
        elif choice == 3:
            create_customer(customer_list)
        elif choice == 4:
            display_customers(customer_list)
        elif choice == 5:
            create_quote(item_inventory,customer_list)
        elif choice == 6:
            take_payment(customer_list)




    update_file("huracan_inventory.csv", item_inventory, ["MODEL", "SERIAL", "PURCHASE PRICE", "DATE RECIVED"])
    update_file("all_customers.csv",customer_list,['ACCOUNT NUMBER','NAME','PHONE NUMBER','EMAIL','ADDRESS','BALANCE'])
    
if __name__ == "__main__":
    main()
