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

#Library Imports
import csv
from tkinter import*

# Indexs for Item Inventory
MODEL_INDEX = 0
MANUFACT_INDEX = 1
SERIAL_INDEX = 2 
LOCATION_INDEX = 3
ALLOCATED_INDEX = 4
CUSTOMER_INDEX = 5


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

def create_main_window(id):
   #place Buttons
   place_buttons(id)

def create_button(text = "PLEASE GIVE ME NAME"):
    btn = Button(root,text = f"{text}")
    return btn

def place_buttons(id):
    column_count = 0
    spacing = 2

    # Create Item Button
    create_item_btn = create_button("CREATE ITEM")
    create_item_btn.configure(command= lambda:create_item(id))
    create_item_btn.grid(row=0, column= column_count, padx= spacing)
    column_count += 1

    #Exit Button
    exit_btn = create_button(text= "EXIT AND SAVE")
    exit_btn.config(command=lambda: save(id, 4))
    exit_btn.grid(row=2, columnspan= 4, column= 0, padx= spacing)
    
def create_item(item_inventory):
    '''
    Paramaters: item_inventory: the dictionary of where it will store the item creates

    Returns: Nothing

    Purpose: Creates an item and stores it in the master item_inventory dictionary. 

    Tkinter: Create an new window that takes in the user input. Then uses a button to close out the window and update the main dictionary
    '''
    #Creates a new window
    create_box = Toplevel()
    row_count = 1
     # Create the Model Number Entry and Label
    model_label = Label(create_box, text= "MODEL:")
    model_label.grid(row =row_count, column= 1)
    e_model = Entry(create_box,width=35, borderwidth=5,)
    e_model.grid(row= row_count, column= 2, columnspan=5, padx= 10, pady=10)
    row_count += 1

    # Create the Serial Number Entry and Label 
    serial_label = Label(create_box, text= "SERIAL:")
    serial_label.grid(row =row_count, column= 1)
    e_serial = Entry(create_box,width=35, borderwidth=5)
    e_serial.grid(row= row_count,column= 2, columnspan=5, padx= 10, pady=10)
    row_count += 1
    
    #Create the Price Entry and Label 
    price_label = Label(create_box, text= "PRICE: $")
    price_label.grid(row = row_count, column= 1)
    e_price= Entry(create_box,width=35, borderwidth=5)
    e_price.grid(row= row_count, column= 2, columnspan=5, padx= 10, pady=10)
    row_count += 1

    #Create the Location Dropbox and Label 
    location_label = Label(create_box, text= "Location: ")
    location_label.grid(row =row_count, column= 1)
    location_op = OptionMenu(create_box,locaction_select , *locations)
    location_op.grid(row= row_count,column= 2)
    row_count += 1

    
    #Create the Sumbit Button
    submit_but = Button(create_box, text= "SUBMIT", command= lambda: submit(item_inventory))
    submit_but.grid(row = row_count, column= 1, columnspan= 3, padx= 10, pady= 10)
        
    def submit(item_inventory):
        item =[]
        item.append(e_model.get())
        item.append(e_serial.get())
        item.append(e_price.get())
        item.append(locaction_select)
        #item.append(int(input("Location: 1. Store 2. Floor 3. Backroom 4. Warehouse"))) 
        item_inventory[item[SERIAL_INDEX]] = item  
        close_window(create_box) 

def save(item, x = 0):
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

    create_main_window(item_inventory_master)

if __name__ == "__main__":
    root = Tk()
    root.title("HURCAN")
    root.geometry("1000x500")
    main()
    root.mainloop()


