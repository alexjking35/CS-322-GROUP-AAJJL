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



table1 = tk.Button(
    text="Table1",
    width=19,
    height=5,
    bg="blue",
    fg="red",
)
tab1_entry = tk.Entry(window,textvariable = tab1_var, font=('calibre',10,'normal'))

table2 = tk.Button(
    text="Table2",
    width=19,
    height=5,
    bg="blue",
    fg="red",
)
tab2_entry = tk.Entry(window,textvariable = tab1_var, font=('calibre',10,'normal'))

table3 = tk.Button(
    text="Table3",
    width=19,
    height=5,
    bg="blue",
    fg="red",
)
tab3_entry = tk.Entry(window,textvariable = tab1_var, font=('calibre',10,'normal'))

table4 = tk.Button(
    text="Table4",
    width=19,
    height=5,
    bg="blue",
    fg="red",
)
tab4_entry = tk.Entry(window,textvariable = tab1_var, font=('calibre',10,'normal'))

table5 = tk.Button(
    text="Table5",
    width=19,
    height=5,
    bg="blue",
    fg="red",
)
tab5_entry = tk.Entry(window,textvariable = tab1_var, font=('calibre',10,'normal'))

table6 = tk.Button(
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




