import tkinter as tk
from tkinter import * 
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

# Add one Combobox 
my_str = tk.()
months=['google','MSN','Microsoft','Yahoo'] # options of Combobox 
cb1 = ttk.Combobox(my_w, values=months,width=10,textvariable=my_str,font=22)
cb1.grid(row=1,column=1,padx=10,pady=20)

# add one button 
b1 = tk.Button(my_w, text='Clik me to open new window',
               command=lambda:my_open())
b1.grid(row=2,column=2) 

def my_open():
    my_w_child=Toplevel(my_w) # Child window 
    my_w_child.geometry("250x200")  # Size of the window 
    my_w_child.title("www.plus2net.com")

    l1 = tk.Label(my_w_child,  text='Your Name', width=10 ) 
    l1.grid(row=0,column=0,padx=5,pady=10) 

    e1 = tk.Entry(my_w_child, width=20,bg='yellow',font=20) 
    e1.grid(row=1,column=0,padx=5,pady=2)

    b2 = tk.Button(my_w_child, text='Submit',
        command=lambda:my_str.set(e1.get()))
    b2.grid(row=2,column=0,padx=5) 
    b3 = tk.Button(my_w_child, text=' Close Child',
                   command=my_w_child.destroy)
    b3.grid(row=3,column=0,padx=5)
    
my_w.mainloop()
