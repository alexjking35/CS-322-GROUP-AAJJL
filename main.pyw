from tkinter import * 

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
Seat = Button(root, text = "Pick a seat",padx = 22, pady = 10).grid()
Order = Button(root, text = "Order food",padx = 21, pady = 10).grid()
Payment = Button(root, text = "Make a payment",padx = 6, pady = 10).grid()
Recipit = Button(root, text = "Print recipit",padx = 19, pady = 10).grid()
MyLable2 = Label(root, text = "Please come again!").grid()

root.mainloop()