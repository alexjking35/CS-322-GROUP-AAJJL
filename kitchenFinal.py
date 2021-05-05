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
