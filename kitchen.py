import tkinter as tk
window = tk.Tk()
window.title("Kitchen")
window.geometry("350x400")

kitchenIntro = tk.Label(text= "Welcome To The Kitchen")
kitchenIntro.grid(row = 0, column = 4)

nachobutton = tk.Button(
    text= "Nachos",
    width = 5,
    height = 1,
    bg = "Black",
    fg = "White",
)
nachobutton.grid(row = 1, column = 2)

cheeseburgerbutton = tk.Button(
    text= "Cheeseburger",
    width = 12,
    height = 1,
    bg = "Black",
    fg = "White",
)
cheeseburgerbutton.grid(row = 2, column = 2)

hotdogbutton = tk.Button(
    text= "Hot Dog",
    width = 8,
    height = 1,
    bg = "Black",
    fg = "White",
)
hotdogbutton.grid(row = 3, column = 2)

pizzabutton = tk.Button(
    text= "Pizza Slice",
    width = 12,
    height = 1,
    bg = "Black",
    fg = "White",
)
pizzabutton.grid(row = 4, column = 2)

fishbutton = tk.Button(
    text= "Fish and Chips",
    width = 15,
    height = 1,
    bg = "Black",
    fg = "White",
)
fishbutton.grid(row = 5, column = 2)

sodabutton = tk.Button(
    text= "Soda",
    width = 5,
    height = 1,
    bg = "Black",
    fg = "White",
)
sodabutton.grid(row = 1, column = 4)

beerbutton = tk.Button(
    text= "Beer",
    width = 5,
    height = 1,
    bg = "Black",
    fg = "White",
)
beerbutton.grid(row = 2, column = 4)

friesbutton = tk.Button(
    text= "Fries",
    width = 7,
    height = 1,
    bg = "Black",
    fg = "White",
)
friesbutton.grid(row = 1, column = 7)

totsbutton = tk.Button(
    text= "Tatortotes",
    width = 11,
    height = 1,
    bg = "Black",
    fg = "White",
    command = clicked
)
totsbutton.grid(row = 2, column = 7)



window.mainloop()
