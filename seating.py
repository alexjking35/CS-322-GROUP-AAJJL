import tkinter as tk
window = tk.Tk()
#def button_click(but):
#    if but.background=="white":
 #       but.background="blue"
  #  else: 
   #     but.background="white"

table1 = tk.Button(
    text="Table1",
    width=10,
    height=5,
    bg="blue",
    fg="red",
)
table1.bind("<Button-1>", button_click(table1))
table2 = tk.Button(
    text="Table2",
    width=10,
    height=5,
    bg="blue",
    fg="red",
)
table2.bind("<Button-1>", button_click(table2))

table3 = tk.Button(
    text="Table3",
    width=10,
    height=5,
    bg="blue",
    fg="red",
)
table3.bind("<Button-1>", button_click(table3))

table4 = tk.Button(
    text="Table4",
    width=10,
    height=5,
    bg="blue",
    fg="red",
)
table4.bind("<Button-1>", button_click(table4))

table5 = tk.Button(
    text="Table5",
    width=10,
    height=5,
    bg="blue",
    fg="red",
)
table5.bind("<Button-1>", button_click(table5))

table6 = tk.Button(
    text="Table6",
    width=10,
    height=5,
    bg="blue",
    fg="red",
)
table6.bind("<Button-1>", button_click(table6))

table1.place(x=4,y=4)
table2.place(x=400,y=4)
table3.place(x = 200, y = 450)
table4.place(x=4,y=200)
table5.place(x=100,y=300)
table6.place(x=200,y=100)
window.mainloop()




