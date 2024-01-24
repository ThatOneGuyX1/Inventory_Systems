""""
Project Name: Huracan Point of Sale Software
Author: Ian Jon Searle
Version: 0.02.5
Summary:    
    This program is desinged for use in a retail enviorment, specificaly targeted toward one single store where I use to work.
    Keeping in mind the needs of the store I designed a software that would track the inventory. Some features such as inventory counting,
    location tracking, and a delivery board have yet to be implemented. This version of the program was to create a Graphic User Interface 
    and learn how the basics of it work. Due to this being a project for a class it is not a fully finsihed version hence version 
    0.02.2, the idea being version 1.00.0 being a fully designed and functional program. 

    Using the tKinter library, a basic GUI was created. This GUI creates multiple windows and allows the user to move between them freely.
    I took inspiration from the Whirlwind Point of Sale Software when looking at features and design ideas for the layout.
    
    Some future implemntations that could take place/ will happen can be found in a list comment at the end of the program. A major one that has
    been thought of is using multiple program files that are then wrapped together in a GUI. This probablt should have been done from the start
    to allow for testing functions.


"""
#Library Imports
import csv
import random
from datetime import datetime
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

# Function list
''' File Function '''
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

'''Item Functions'''
def create_item(item_inventory):
    '''
    Paramaters: item_inventory: the dictionary of where it will store the item creates

    Returns: Nothing

    Purpose: Creates an item and stores it in the master item_inventory dictionary. 

    Tkinter: Create an new window that takes in the user input. Then uses a button to close out the window and update the main dictionary
    '''
    #Creates a new window
    create_box = Toplevel()

    # Create the Model Number Entry and Label
    model_label = Label(create_box, text= "MODEL:")
    model_label.grid(row =1, column= 1)
    e_model = Entry(create_box,width=35, borderwidth=5,)
    e_model.grid(row= 1, column= 2, columnspan=5, padx= 10, pady=10)

    # Create the Serial Number Entry and Label 
    serial_label = Label(create_box, text= "SERIAL:")
    serial_label.grid(row =2, column= 1)
    e_serial = Entry(create_box,width=35, borderwidth=5)
    e_serial.grid(row= 2,column= 2, columnspan=5, padx= 10, pady=10)
    
    #Create the Price Entry and Label 
    price_label = Label(create_box, text= "PRICE: $")
    price_label.grid(row =3, column= 1)
    e_price= Entry(create_box,width=35, borderwidth=5)
    e_price.grid(row= 3, column= 2, columnspan=5, padx= 10, pady=10)
    
    #Create the Sumbit Button
    submit_but = Button(create_box, text= "SUBMIT", command= lambda: submit(item_inventory))
    submit_but.grid(row = 4, column= 1, columnspan= 3, padx= 10, pady= 10)
        
    def submit(item_inventory):
        item =[]
        item.append(e_model.get())
        item.append(e_serial.get())
        item.append(e_price.get())
        item.append(get_date())
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
    item_display = Label(window, text = f'MODEL: {item[MODEL_INDEX]} :: SERIAL:{item[SERIAL_INDEX]}')
    return item_display

def display_inventory(item_inventory):
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

''''Customer Functions'''
def create_customer(cust_list):
    '''
    Paramaters: cust_list: the customer list

    Returns: Nothing

    Purpose: creates an entry box to allow user to input the customer data, while auto generating a customer's unique ID
    
    Note: I do not like the form of this function, but I do not have an easier way to express this function. 
          Possibly could be solved by using one function to create the Tkinter window and another function for writing to the list. 
    
    '''
    # Create the Window
    window = Toplevel()
    window.title("Customer Creations")
    pad_var = 5 # For neatness

    # Creates the account number
    acc_num = create_account_number(cust_list)
    Label(window, text="ACCOUNT NUMBER: " + acc_num).grid(row =0, columnspan= 4)

    #First Names
    e_fname = Entry(window)
    fname_label = Label(window, text= "CUSTOMER FIRST NAME:")
    fname_label.grid(row =1, column= 0, padx= pad_var, pady= pad_var)
    e_fname.grid(row= 1, column= 1, padx= pad_var, pady= pad_var)

    # Last Names
    e_sname = Entry(window)
    sname_label = Label(window, text= "CUSTOMER LASR NAME:")
    sname_label.grid(row =1, column= 2,padx= pad_var, pady= pad_var)
    e_sname.grid(row=1, column= 3,padx= pad_var, pady= pad_var)

    # Phone Number 
    e_pnum = Entry(window)
    pnum_label = Label(window, text= "PHONE NUMBER:")
    pnum_label.grid(row = 2, column= 0,padx= pad_var, pady= pad_var)
    e_pnum.grid(row = 2, column= 1,padx= pad_var, pady= pad_var)

    #Email
    e_email = Entry(window)
    email_label = Label(window, text= "EMAIL:")
    email_label.grid(row = 2, column= 2, padx= pad_var, pady= pad_var)
    e_email.grid(row= 2 , column= 3, padx= pad_var, pady= pad_var)

    # ADDRESS
    e_st = Entry(window)
    st_label = Label(window, text= "ST ADRRESS:")
    st_label.grid(row = 3, column= 0, padx= pad_var, pady= pad_var)
    e_st.grid(row= 3 , column= 1, padx= pad_var, pady= pad_var)

    # Zip Code
    e_zip = Entry(window)
    zip_label = Label(window, text= "ZIP:")
    zip_label.grid(row = 3, column=2, padx= pad_var, pady= pad_var)
    e_zip.grid(row= 3 , column= 3, padx= pad_var, pady= pad_var)

    # City
    e_city = Entry(window)
    city_label = Label(window, text= "CITY:")
    city_label.grid(row = 4, column= 0, padx= pad_var, pady= pad_var)
    e_city.grid(row= 4 , column= 1, padx= pad_var, pady= pad_var)

    # State
    e_state = Entry(window)
    state_label = Label(window, text= "STATE:")
    state_label.grid(row = 4, column= 2, padx= pad_var, pady= pad_var)
    e_state.grid(row= 4 , column= 3, padx= pad_var, pady= pad_var)
    
    #Submit buttong
    submit_but = Button(window, text= "SUBMIT", command= lambda: submit(cust_list))
    submit_but.grid(row= 10, columnspan=5)

    def submit(cust_list):
        '''
        Paramaters: cust_list: the customer list

        Returns: Nothing

        Purpose: Calling the information from the entry boxes and appeneds them to a list. That list is then appeneded to the main customer list.
        
        Note: I want to be able to test this function, but since it is called by a button press I am not able to test it
              I do wish there I knew of a way to be able to. However since Pytest can't be used, I have manualy tested this multiple time
        '''
        customer = [] 
        customer.append(acc_num)
        customer.append(str( e_sname.get() +", " + e_fname.get()))
        customer.append(e_pnum.get())
        customer.append(e_email.get())
        address = str(f'{e_st.get()}, {e_city.get()}, {e_state.get()}, {e_zip.get()}') 
        customer.append(address)
        customer.append((0.0))
        cust_list[customer[ACCOUNT_NUM_INDEX]] = customer

        close_window(window)

def create_account_number(cust_list):
    '''
    Paramaters: cust_list: the customer list

    Returns: Nothing

    Purpose: Randomly generates a unique ID for each new customer, also checks if the account number already exists. 
             If the account number exists it will create a new one.
    '''
    # Account number is 1 + a number
    num = 1
    while num == 1:
        rand = random.randint(0,10000)

        temp_num = rand + 1
        if temp_num not in cust_list:
            num = temp_num

    return str(num)

'''Point of Sale Functions'''
def create_quote(inventory,cust_list):
    '''
    Paramaters: cust_list: The Master Customer Dictionary
                inventory: The Master Inventory dictionary

    Returns: Nothing

    Purpose: Allows the user to select a customer and creates and invoice for them. 

    Tkinter: Creates two windows, the main and the child. The child window is for selecting which customer the item is being sold to.
             The main window then holds the information for creating the sale. 
    '''
    #Important Variables
    row_count = [0]
    customer_name = StringVar()
    subtotal = []
    customer_selected = []
    
    #Create the Windows
    window_main = Toplevel(root)
    window_child = Toplevel(window_main)
    item_frame = LabelFrame(window_main)
    item_frame.grid(row= 5, column=0)
    
    #Add Row
    def add_row(row_count,subtotal):
        '''
        Paramaters: row_count: The starting row for the invoice
                    subtotal: Tracks the total price

        Returns: Nothing

        Purpose: Looks at what model the user has selected and then creates a new row with the need information.
        '''
        model_target = e_model.get()
        for item in inventory:
            if model_target == inventory[item][MODEL_INDEX]:
                model_list = inventory[item]
                create_item_row(model_list,row_count)
                row_count[0] += 1
                subtotal.append(model_list[PRICE_INDEX])

                break

        inventory.pop(item,None)


    #Getting the Account
    def show_customer():
        '''
        Paramaters: NONE

        Returns: Nothing

        Purpose: Using a drop downmenu allows the user to select which customer is being selected
        '''
        customer_target = customer_name.get()
        for customer in cust_list:
            if cust_list[customer][ACCOUNT_NAME__INDEX] == customer_target:
                customer_selected.append(cust_list[customer])
                break
        # Updates the Customer Frame on the main window
        customer_name_label.config(text= cust_list[customer][ACCOUNT_NAME__INDEX])
        customer_adress_label.config(text= cust_list[customer][ACCOUNT_ADDRESS_INDEX])
        customer_phone_label.config(text= cust_list[customer][ACCOUNT_PHONE_NUM_INDEX])

        close_window(window_child)
    
    #Create Item Information
    def create_item_row(model_list, row_count):

        if model_list[SERIAL_INDEX] in inventory:

            # Model Label
            model_lbl = Label(item_frame,text="")
            model_lbl.config(text=model_list[MODEL_INDEX])
            model_lbl.grid(row = row_count[0], column= 0)

            # Serial
            serial_lbl = Label(item_frame,text="")
            serial_lbl.config(text=model_list[SERIAL_INDEX])
            serial_lbl.grid(row = row_count[0], column= 1)
            # Cost
            cost_lbl = Label(item_frame,text="")
            cost_lbl.config(text=model_list[PRICE_INDEX])
            cost_lbl.grid(row = row_count[0], column= 2)

    def end_sale(subtotal,customer_selected):
        window_total = Toplevel()
        total_label= Label(window_total, text="")
        total = 0
        for price in subtotal:
            total += float(price)
        total_label.config(text= f"{(total*1.06):.2f}")
        total_label.pack()
        Button(window_total, text='End Sale', command= lambda:close_window(window_main)+ close_window(window_total)).pack()

    customer_name_list = []
    for customer in cust_list:
       customer_name_list.append(cust_list[customer][ACCOUNT_NAME__INDEX])
    

    """Interface Options"""
    #Shows the options and creates button
    OptionMenu(window_child, customer_name ,*customer_name_list).pack()
    Button(window_main,text="REFRESH CUSTOMER", command= show_customer).grid(row= 0, column= 1)
    Button(window_main, text="SAVE ITEM", command= lambda:add_row(row_count,subtotal)).grid(row= 0, column= 2)
    btn_create_invoice=Button(window_main, text= "CREATE INVOICE", command = lambda:end_sale(subtotal, customer_selected))
    btn_create_invoice.grid(row = 0, column= 3)
   #Button(window_main,text="REFRESH ITEM", command= show_item).grid(row= 0, column= 2)
    
    # FRAME
    customer_info = LabelFrame(window_main)
    window_main.geometry("500x500")
    customer_info.grid(row=1, columnspan= 3)

    # Customer Name
    customer_name_label = Label(customer_info, text= "")
    Label(customer_info, text="NAME").grid(row=1, column=1)
    customer_name_label.grid(row =1 , column=2)

    #Customer Adress
    customer_adress_label = Label(customer_info, text= "")
    Label(customer_info, text="ADDRESS").grid(row=2, column=1)
    customer_adress_label.grid(row =2 , column=2)

    #Customer Phone Number
    Label(customer_info, text="PHONE NUMBER").grid(row = 3, column= 1)
    customer_phone_label = Label(customer_info,text = "")
    customer_phone_label.grid(row=3, column= 2)

    #Model Selection
    e_model = Entry(window_main)
    e_model.grid(row =4, columnspan= 4)
       
# I was not able to work on the payment portion of the GUI before the due date
""""
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
"""

""" other Function""" 
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
    '''
    Paramaters: NONE

    Returns: None

    Purpose: Creates the main user window which houses the main buttons and options. 

    Note: There is still room to expand the main window and add more features. Something I would like to implent later
    is a clock function as well as time clock and a delivery board however I belive this will be done using a differnt GUI.
    '''

    #setup main varibale
    item_inventory = open_file("huracan_inventory.csv", SERIAL_INDEX)
    customer_list = open_file("all_customers.csv", ACCOUNT_NUM_INDEX)

    create = Button(root,text = "CREATE ITEM", command=lambda: create_item(item_inventory))
    display = Button(root, text = "Display Inventory",command=lambda: display_inventory(item_inventory))
    customer = Button(root, text= "Create Customer", command= lambda:create_customer(customer_list))
    sale = Button(root,text= "Create Sale", command= lambda: create_quote(item_inventory,customer_list))
    exit = Button(root, text = "EXIT", command=lambda: save(item_inventory,customer_list, 4))


    create.grid(row = 0, column= 1)
    display.grid(row = 0, column= 2)
    customer.grid(row = 0, column= 3)
    sale.grid(row = 0, column= 4)
    exit.grid(row = 1 ,columnspan = 100)

if __name__ == "__main__":
    root = Tk()
    root.title("HURCAN")
    root.geometry("500x500")
    main()
    root.mainloop()

"""
Future Features:
    Payment options and balance tracking
    A time clock and employee database
    Delivery Option
        This would posisbly inculde some form of non-serial inventory
    Location and Type of Product
    Using multiple Files that are then imported into the main function, this should allow for more test functions, and upgradiblity.
    An autocomplte text bar in the sale window
    Storing the sale information. 





"""