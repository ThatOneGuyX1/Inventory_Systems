"""
Project Name: Huracan Point of Sale Software
Author: Ian Jon Searle
Function File: Item V.01
Version: 0.03.0
"""

# Indexs for Item Inventory
MODEL_INDEX = 0
SERIAL_INDEX = 1  
PRICE_INDEX = 2
DATE_RECIVED_INDEX = 3 
LOCATION_INDEX = 4

#Imports

from tkinter import*
from datetime import datetime

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
    locations = ["Store", "Warehouse", "Floor"]
    locaction_select = StringVar()
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
        item.append(get_date())
        item.append(locaction_select)
        #item.append(int(input("Location: 1. Store 2. Floor 3. Backroom 4. Warehouse"))) 
        item_inventory[item[SERIAL_INDEX]] = item  
        close_window(create_box) 
    
def display_item(item,window):
    '''
    Paramaters: item: the list portion of an item in item_inventory

    Returns: Nothing

    Purpose: Creates a label that contains the information a specfific item.
    
    tKinter: Creates a label and applies it to the window that was passed to it.    
    '''
    item_display = Label(window, text = f'MODEL: {item[MODEL_INDEX]} :: SERIAL:{item[SERIAL_INDEX]} :: Location: {item[LOCATION_INDEX]}')
    return item_display

def display_inventory_all(item_inventory):
    '''
    Paramaters: item_inventory: the main invenotry dictionary

    Returns: Nothing

    Purpose: Cycles trough each item in the dictionary and passes them to the single item display
    
    Tkinter: Creates the main window and adds the created label to the window
    '''
    row_count = 1
    item_window = Toplevel()
    for item in item_inventory:

        item_display =display_item(item_inventory[item],item_window)
        item_display.grid(row = row_count, column= 1)
        row_count += 1 # Incremets the row count by 1 so that the labels do not overlap

    Button(item_window,text= "CLOSE", command= lambda: close_window(item_window)).grid(row = row_count, columnspan=2)

def display_inventory_location(item_inventory):
    location = ["Store", "Floor", "Warehouse"]
    count = 0
    row_count = 1
    item_window = Toplevel()
    if count != len(location):
        for item in item_inventory:
            if item_inventory[item][LOCATION_INDEX] == location[count]:
                display_item(item_inventory[item], item_window).grid(row = row_count, column= 1)
                row_count += 1
        count += 1
            
    Button(item_window,text= "CLOSE", command= lambda: close_window(item_window)).grid(row = row_count, columnspan=2)

def get_date():
    '''
    Paramaters: NONE

    Returns: today: date formated as YYYY/MM/DD

    Purpose: Creates the date for the date an item recived
    '''
    cday = str(datetime.now().day)
    cmonth = str(datetime.now().month)
    cyear = str(datetime.now().year)
    today = cyear +"/" + cmonth + "/" + cday
    return today

def delete_item(key_value,item_inventory):
    '''
    Paramaters: key_value: the targer Key value to be deleted 

    Returns: Nothing

    Purpose: Removes an item from the dictionary, this a real simple one.
    '''
    item_inventory.pop(key_value)

def close_window(window):
    '''
    Paramaters: window: THe Target window to be closed

    Returns: Nothing

    Purpose: Closes a window.
    '''
    window.destroy()

