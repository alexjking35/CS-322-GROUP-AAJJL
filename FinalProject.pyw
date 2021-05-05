from tkinter import * 

total_bill = 0
items = []


# -- KITCHEN -----
def kitchen():
    import tkinter as tk
    window = tk.Tk()
    window.title("Kitchen")
    window.geometry("350x400")

    kitchenIntro = tk.Label(text= "Welcome To The Kitchen")
    kitchenIntro.grid(row = 0, column = 4)

    #List box for kitchen orders
    lb = tk.Listbox(window, )
    lb.grid( row = 40, column = 4)

    #Adding the items to Listbox 
    def click_nachos():
        lb.insert(0,'Nachos')

    def click_cheese():
        lb.insert(0,'Cheeseburger')

    def click_hotdog():
        lb.insert(0,'Hot Dog')

    def click_pizza():
        lb.insert(0,'Pizza Slice')

    def click_fish():
        lb.insert(0,'Fish and Chips')

    def click_soda():
        lb.insert(0,'Soda')

    def click_beer():
        lb.insert(0,'Beer')

    def click_fries():
        lb.insert(0,'Fries')

    def click_tots():
        lb.insert(0,'Tatortots')

    #Delete selected items from Listbox 
    def delete(listbox):
        global things
        #Delete 
        selection = lb.curselection()
        lb.delete(selection[0])
        #Delete from list
        value = eval(lb.get(selection[0]))
        ind = things.index(value)
        del(things[ind])
        print(things)

    #Buttons 
    buttondel = tk.Button(window, text = "Delete item", command = lambda: delete(1))
    buttondel.grid(row = 10, column = 5)

    nachobutton = tk.Button(
        text= "Nachos",
        width = 5,
        height = 1,
        bg = "Black",
        fg = "White",
        command = click_nachos
    )
    nachobutton.grid(row = 1, column = 2)

    cheeseburgerbutton = tk.Button(
        text= "Cheeseburger",
        width = 12,
        height = 1,
        bg = "Black",
        fg = "White",
        command = click_cheese
    )
    cheeseburgerbutton.grid(row = 2, column = 2)

    hotdogbutton = tk.Button(
        text= "Hot Dog",
        width = 8,
        height = 1,
        bg = "Black",
        fg = "White",
        command = click_hotdog
    )
    hotdogbutton.grid(row = 3, column = 2)

    pizzabutton = tk.Button(
        text= "Pizza Slice",
        width = 12,
        height = 1,
        bg = "Black",
        fg = "White",
        command = click_pizza
    )
    pizzabutton.grid(row = 4, column = 2)

    fishbutton = tk.Button(
        text= "Fish and Chips",
        width = 15,
        height = 1,
        bg = "Black",
        fg = "White",
        command = click_fish
    )
    fishbutton.grid(row = 5, column = 2)

    sodabutton = tk.Button(
        text= "Soda",
        width = 5,
        height = 1,
        bg = "Black",
        fg = "White",
        command = click_soda
    )
    sodabutton.grid(row = 1, column = 4)

    beerbutton = tk.Button(
        text= "Beer",
        width = 5,
        height = 1,
        bg = "Black",
        fg = "White",
        command = click_beer
    )
    beerbutton.grid(row = 2, column = 4)

    friesbutton = tk.Button(
        text= "Fries",
        width = 7,
        height = 1,
        bg = "Black",
        fg = "White",
        command = click_fries
    )
    friesbutton.grid(row = 1, column = 7)

    totsbutton = tk.Button(
        text= "Tatortots",
        width = 11,
        height = 1,
        bg = "Black",
        fg = "White",
        command = click_tots
    )
    totsbutton.grid(row = 2, column = 7)



    window.mainloop()


# ---  SEATING -----
def seating():
    import tkinter as tk
    window = tk.Tk()
    window.geometry("700x500")
    window.configure(bg="black")

    name = tk.Label(window,text="Choose A Table",fg="Red",bg="Black",font="Arial")
    name.place(x=100,y=440)
    tab1_var=tk.StringVar()
    tab2_var = tk.StringVar()
    tab3_var = tk.StringVar()
    tab4_var=tk.StringVar()
    tab5_var=tk.StringVar()
    tab6_var=tk.StringVar()



    table1 = tk.Button(window,
        text="Table1",
        width=19,
        height=5,
        bg="blue",
        fg="red"
    )
    tab1_entry = tk.Entry(window,textvariable = tab1_var, font=('calibre',10,'normal'))

    table2 = tk.Button(window,
        text="Table2",
        width=19,
        height=5,
        bg="blue",
        fg="red",
    )
    tab2_entry = tk.Entry(window,textvariable = tab1_var, font=('calibre',10,'normal'))

    table3 = tk.Button(window,
        text="Table3",
        width=19,
        height=5,
        bg="blue",
        fg="red",
    )
    tab3_entry = tk.Entry(window,textvariable = tab1_var, font=('calibre',10,'normal'))

    table4 = tk.Button(window,
        text="Table4",
        width=19,
        height=5,
        bg="blue",
        fg="red",
    )
    tab4_entry = tk.Entry(window,textvariable = tab1_var, font=('calibre',10,'normal'))

    table5 = tk.Button(window,
        text="Table5",
        width=19,
        height=5,
        bg="blue",
        fg="red",
    )
    tab5_entry = tk.Entry(window,textvariable = tab1_var, font=('calibre',10,'normal'))

    table6 = tk.Button(window,
        text="Table6",
        width=19,
        height=5,
        bg="blue",
        fg="red",
    )
    tab6_entry = tk.Entry(window,textvariable = tab1_var, font=('calibre',10,'normal'))


    table1.place(x=4,y=4)
    tab1_entry.place(x=4,y=80)
    table2.place(x=400,y=4)
    tab2_entry.place(x=400,y=80)
    table3.place(x = 400, y = 250)
    tab3_entry.place(x=400,y=330)
    table4.place(x=4,y=200)
    tab4_entry.place(x=4,y=280)
    table5.place(x=100,y=300)
    tab5_entry.place(x=100,y=380)
    table6.place(x=200,y=100)
    tab6_entry.place(x=200,y=180)
    window.mainloop()
    






# ------- Payment ------------

def payment():
    import tkinter as tk
# import everything from tkinter module
 
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
        global items
        total_bill = total_bill + 2.99
        equation.set("Soda $2.99")
        items.append("Soda $2.99")

    # Defining functions for all the food
    def cheeseburger():
        global total_bill
        global items
        total_bill = total_bill + 11.99
        equation.set("CheeseBurger $11.99")
        items.append("CheeseBurger $11.99")

    # Defining functions for all the food
    def hotdog():
        global total_bill
        global items
        total_bill = total_bill + 6.99
        equation.set("HotDog $6.99")
        items.append("HotDog $6.99")


    # Defining functions for all the food
    def pizzaslice():
        global total_bill
        global items
        total_bill = total_bill + 3.50
        equation.set("Pizza Slice $3.50")
        items.append("Pizza Slice $3.50")

    # Defining functions for all the food
    def beer():
        global total_bill
        global items
        total_bill = total_bill + 4.00
        equation.set("Beer $4.00")
        items.append("Beer $4.00")

    # Defining functions for all the food
    def fries():
        global total_bill
        global items
        total_bill = total_bill + 4.99
        equation.set("Fries $4.99")
        items.append("Fries $4.99")

    # Defining functions for all the food
    def fish_chips():
        global total_bill
        global items
        total_bill = total_bill + 12.99
        equation.set("Fish and Chips $12.99")
        items.append("Fish and Chips $12.99")

        # Defining functions for all the food
    def tatertots():
        global total_bill
        global items
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
        expression_field = Entry(gui, textvariable = equation)

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

















# -- MAIN MENU ---- 
root = Tk()
root.title("Resturant management system V1.0")

#functions regarding sign in
def accountRetrive():
    accountRetrive = Tk()
    accountRetrive.title("Resturant management system V1.0")
    myLable = Label(accountRetrive, text = "Please enter your phone number:").grid()
    myentry_1 = Entry(accountRetrive, width = 40, borderwidth = 2).grid()
    myButton_1 = Button(accountRetrive, text = "Cancel", command = accountRetrive.destroy).grid()

def signInF():
    signin = Tk()
    signin.title("Resturant management system V1.0")
    myLabel_1 = Label(signin, text = "Account name:").grid()
    myentry_1 = Entry(signin, width = 40, borderwidth = 2).grid()
    myLabel_2 = Label(signin, text = "Password:").grid()
    myentry_2 = Entry(signin, width = 40, borderwidth = 2).grid()
    myButton_1 = Button(signin, text = "Cancel", command = signin.destroy).grid()
    myButton_2 = Button(signin, text = "Forget your account info?",command = accountRetrive).grid()

#design of the main interface
MyLable1 = Label(root, text = "Welcome to our resturant!").grid()
SignIn = Button(root, text = "Sign in",padx = 32, pady = 10,command = signInF).grid()
Seat = Button(root, text = "Pick a seat",padx = 22, pady = 10, command = seating).grid()
Order = Button(root, text = "Order food",padx = 21, pady = 10, command = kitchen).grid()
Payment = Button(root, text = "Make a payment/Print Reciept",padx = 6, pady = 10, command = payment).grid()
#kitchen_ = Button(root, text = "Kitchen",padx = 19, pady = 10, command = kitchen).grid()
MyLable2 = Label(root, text = "Please come again!").grid()

root.mainloop()