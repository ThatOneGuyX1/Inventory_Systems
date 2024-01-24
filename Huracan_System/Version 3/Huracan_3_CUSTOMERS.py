"""
Project Name: Huracan Point of Sale Software
Author: Ian Jon Searle
Function File: Customer V.01
Version: 0.03.0
"""
import random
from tkinter import*
# Indexes for the Customer Account List
ACCOUNT_NUM_INDEX = 0
ACCOUNT_NAME__INDEX = 1
ACCOUNT_PHONE_NUM_INDEX = 2
ACCOUNT_EMAIL_INDEX =3
ACCOUNT_ADDRESS_INDEX = 4
ACCOUNT_BAL_INDEX = 5


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

def display_customer_list(cust_list):
    '''
    Paramaters: item_inventory: the main invenotry dictionary

    Returns: Nothing

    Purpose: Cycles trough each item in the dictionary and passes them to the single item display
    
    Tkinter: Creates the main window and adds the created label to the window
    '''
    row_count = 1
    cust_window = Toplevel()
    for customer in cust_list:

        customer_display =display_customer(cust_list[customer],cust_window)
        customer_display.grid(row = row_count, column= 1)
        row_count += 1 # Incremets the row count by 1 so that the labels do not overlap

    Button(cust_window,text= "CLOSE", command= lambda: close_window(cust_window)).grid(row = row_count, columnspan=2)

def display_customer(item,window):
    '''
    Paramaters: item: the list portion of an item in item_inventory

    Returns: Nothing

    Purpose: Creates a label that contains the information a specfific item.
    
    tKinter: Creates a label and applies it to the window that was passed to it.    
    '''
    lbl = Label(window, text = f'Name: {item[ACCOUNT_NAME__INDEX]} :: PHONE NUMBER:{item[ACCOUNT_PHONE_NUM_INDEX]}')
    return lbl

def close_window(window):
    '''
    Paramaters: window: THe Target window to be closed

    Returns: Nothing

    Purpose: Closes a window.
    '''
    window.destroy()