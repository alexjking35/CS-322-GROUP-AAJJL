
import tkinter as tk
# import everything from tkinter module
from tkinter import *
 
# globally declare the expression variable
expression = ""
total_bill = 0
items = []
 
# Defining functions for all the food
def nachos():
    global total_bill
    global items
    total_bill = total_bill + 10.99
    equation.set("Nachos $10.99")
    items.append("Nachos $10.99")

# Defining functions for all the food
def soda():
    global total_bill
    total_bill = total_bill + 2.99
    equation.set("Soda $2.99")
    items.append("Soda $2.99")

# Defining functions for all the food
def cheeseburger():
    global total_bill
    total_bill = total_bill + 11.99
    equation.set("CheeseBurger $11.99")
    items.append("CheeseBurger $11.99")

# Defining functions for all the food
def hotdog():
    global total_bill
    total_bill = total_bill + 6.99
    equation.set("HotDog $6.99")
    items.append("HotDog $6.99")


# Defining functions for all the food
def pizzaslice():
    global total_bill
    total_bill = total_bill + 3.50
    equation.set("Pizza Slice $3.50")
    items.append("Pizza Slice $3.50")

# Defining functions for all the food
def beer():
    global total_bill
    total_bill = total_bill + 4.00
    equation.set("Beer $4.00")
    items.append("Beer $4.00")

# Defining functions for all the food
def fries():
    global total_bill
    total_bill = total_bill + 4.99
    equation.set("Fries $4.99")
    items.append("Fries $4.99")

# Defining functions for all the food
def fish_chips():
    global total_bill
    total_bill = total_bill + 12.99
    equation.set("Fish and Chips $12.99")
    items.append("Fish and Chips $12.99")

    # Defining functions for all the food
def tatertots():
    global total_bill
    total_bill = total_bill + 4.99
    equation.set("Tatertots $4.99")
    items.append("Tatertots $4.99")


 
 
# Function to evaluate the final expression
def totalpress():
    global total_bill 
    equation.set("$"+str(round(total_bill,2)))
 
 
# Function to clear the contents
# of text entry box
def clear():
    global expression
    global total_bill
    global items
    total_bill = 0
    expression = ""
    equation.set("")
    items *= 0

def print_reciept():
    global items
    global total_bill
    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill = Y )

    length = len(items)
    mylist = Listbox(root, yscrollcommand = scrollbar.set )
    for x in range(length):
        mylist.insert(END, items[x])
    
    mylist.insert(END,"TOTAL")
    mylist.insert(END,'$' + str(round(total_bill,2)))

    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
   
 
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
 
    # set the background colour of GUI window
    gui.configure(background="light blue")
 
    # set the title of GUI window
    gui.title("Payment Plan")
 
    # set the configuration of GUI window
    gui.geometry("400x400")
 

    equation = StringVar()
 
    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=4, ipadx=70)

    button1 = Button(gui, text='Nachos $10.99', fg='black', bg='red',
                    command=nachos, height=1, width=16)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text='Soda $2.99', fg='black', bg='red',
                    command=soda, height=1, width=16)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text='CheeseBurger $11.99', fg='black', bg='red',
                    command=cheeseburger, height=1, width=16)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text='HotDog $6.99', fg='black', bg='red',
                    command=hotdog, height=1, width=16)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text='Pizza Slice $3.50', fg='black', bg='red',
                    command=pizzaslice, height=1, width=16)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text='Beer $4.00', fg='black', bg='red',
                    command=beer, height=1, width=16)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text='Fries $4.99', fg='black', bg='red',
                    command=fries, height=1, width=16)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text='Fish and Chips $12.99', fg='black', bg='red',
                    command=fish_chips, height=1, width=16)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text='Tatertots $4.99', fg='black', bg='red',
                    command=tatertots, height=1, width=16)
    button9.grid(row=4, column=2)
 
    total = Button(gui, text='Total', fg='black', bg='red',
                command=totalpress, height=1, width=7)
    total.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='red',
                command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    ## Creating a print reciept part
    reciept = Button(gui, text='Print Reciept', fg='black', bg='red',
                command=print_reciept, height=1, width=10)
    reciept.grid(row=5, column=0)
 
    gui.mainloop()