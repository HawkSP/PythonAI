from tkinter import *
from functools import partial

def account_login():


    def validate_Login(username, password):
        print("username entered :", username.get())
        print("password entered :", password.get())
        if username.get() == "Dedeye" and password.get() == "ADMIN":
            print("Account already exists")
            program_restart = input("Would you like to create a new profile?: ")
            if program_restart == "Yes" or "Y" or "y" or "yes":
                from main import get_sound
                from soundsplitter import sound_splitter
                get_sound()
                sound_splitter()



        else:
            return


    # window
    tkWindow = Tk()
    tkWindow.geometry('400x150')
    tkWindow.title('DEDAI')

    # username label and text entry box
    usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

    # password label and password entry box
    passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

    validateLogin = partial(validate_Login, username, password)

    # login button
    loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

    tkWindow.mainloop()

account_login()