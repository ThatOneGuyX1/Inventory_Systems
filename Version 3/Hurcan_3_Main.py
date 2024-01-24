""""
Project Name: Huracan Point of Sale Software
Author: Ian Jon Searle
Function File: MAIN V.01
Version: 0.03.0
Summary:    
    This program is desinged for use in a retail enviorment, specificaly targeted toward one single store where I use to work.
    Keeping in mind the needs of the store I designed a software that would track the inventory. Some features such as inventory counting,
    location tracking, and a delivery board have yet to be implemented. This version builds off of the Graphic User Interface devloped in the 
    last version. However we are now creating seperate files for each set of function which will then be imported. The idea behind this is it 
    will allow for the development of indicuial functions with out changing the overall program and have it be easier to read.
   
   This file includes all file functions, such as writing and saving the information, as well the overall main function and the main display
   functions.
    """
#Other File Imports
import Huracan_3_ITEMS
import Huracan_3_CUSTOMERS


#Library Imports
import csv
from tkinter import*

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

def open_file(filename,key_column_index):
    """ 
    Paramaters: filename: the name of the file to open
                key_column_index: the index of the key value

    Returns: dictionary: the data of the file 
    
    Purpose: Opens a file and stores the data into a dictionary that is then returned to the main program
    """
    dictionary = {} # Creates a temp dictionary

    with open(filename, "r", encoding='utf-8') as csv_file: # Opens the target file 
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

# tKinter fucntions

def create_main_window(id,cl):
   #place Buttons
   place_buttons(id,cl)

def create_button(text = "PLEASE GIVE ME NAME"):
    btn = Button(root,text = f"{text}")
    return btn

def place_buttons(id,cl):
    column_count = 0
    spacing = 2

    # Create Item Button
    create_item_btn = create_button("CREATE ITEM")
    create_item_btn.configure(command= lambda: Huracan_3_ITEMS.create_item(id))
    create_item_btn.grid(row=0, column= column_count, padx= spacing)
    column_count += 1

    # Display Invenotry Buttons
    display_inventory_btn = create_button("DISPLAY INVENTOY") 
    display_inventory_btn.configure(command=lambda:Huracan_3_ITEMS.display_inventory_all(id))
    display_inventory_btn.grid(row=0, column= column_count, padx= spacing)
    column_count += 1

    #Display Invenotry by Location
    display_location_btn = create_button("DISPLAY INVENTORY LOCATION") 
    display_location_btn.configure(command=lambda:Huracan_3_ITEMS.display_inventory_location(id))
    display_location_btn.grid(row=0, column= column_count, padx= spacing)
    column_count += 1

    #Create Customer
    display_inventory_btn = create_button("CREATE CUSTOMER") 
    display_inventory_btn.configure(command=lambda:Huracan_3_CUSTOMERS.create_customer(cl))
    display_inventory_btn.grid(row=0, column= column_count, padx= spacing)
    column_count += 1

    #Dislpay Customers
    display_inventory_btn = create_button("DISPLAY CUSTOMERS") 
    display_inventory_btn.configure(command=lambda:Huracan_3_CUSTOMERS.display_customer_list(cl))
    display_inventory_btn.grid(row=0, column= column_count, padx= spacing)
    column_count += 1

    #Exit Button
    exit_btn = create_button(text= "EXIT AND SAVE")
    exit_btn.config(command=lambda: save(id,cl, 4))
    exit_btn.grid(row=2, columnspan= 4, column= 0, padx= spacing)
    
def save(item, cust, x = 0):
    '''
    Paramaters: item: The master item_inventory
                cust: The master customer dictionary
                x: An interger which will determine if the save function is being used as the exit function or not
                    The idea was that at times, mayber after doing a long inventory update the user could save, but not exit
                    using X the program would know if it should close or not.

    Returns: Nothing

    Purpose: Updates the CSV files and if X is greater than 0 it will end the program
    '''

    update_file("huracan_inventory.csv", item, ["MODEL", "SERIAL", "PURCHASE PRICE", "DATE RECIVED"])
    update_file("all_customers.csv",cust,['ACCOUNT NUMBER', 'NAME', 'PHONE NUMBER', "EMAIL",'ADDRESS', 'BALANCE'])
    if x != 0:
        close_window(root)

def close_window(window):
    '''
    Paramaters: window: THe Target window to be closed

    Returns: Nothing

    Purpose: Closes a window.
    '''
    window.destroy()

def main():

    item_inventory_master = open_file("huracan_inventory.csv", SERIAL_INDEX)
    customer_list_master = open_file("all_customers.csv", ACCOUNT_NUM_INDEX)

    create_main_window(item_inventory_master,customer_list_master)

if __name__ == "__main__":
    root = Tk()
    root.title("HURCAN")
    root.geometry("1000x500")
    main()
    root.mainloop()


