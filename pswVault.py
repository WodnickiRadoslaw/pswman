import hashlib
import sqlite3
from functools import partial
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from passgen import passGenerator
from tkinter import filedialog
import tkinter as tk


#TODO zrobic hashowanie tabeli w sql


# tworzenie noego masterpassword - identyfikacja 
with sqlite3.connect("dbMain.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
platform TEXT NOT NULL,
account TEXT NOT NULL,
password TEXT NOT NULL,
notes TEXT NULL);
""")

# Drop table vault ####################################################
#cursor.execute("""
#DROP TABLE vault;
#""")


# Create PopUp #########################################################
def popUp(text):
    answer = simpledialog.askstring("Insert data", text)
    return answer


# Initiate Window
window = Tk()
window.update()

window.title("Password Manager")


def hashPassword(input):
    hash1 = hashlib.sha256(input) #hashowanie sha256/ zmiana na md5 powoduje hashowanie w md5 - biblioteka hashlib
    hash1 = hash1.hexdigest()

    return hash1

#   Set up master password screen #######################################
def firstTimeScreen():
    window.geometry("250x150")

    lbl = Label(window, text="Create Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window, text="Re-enter Password")
    lbl1.config(anchor=CENTER)
    lbl1.pack()

    txt1 = Entry(window, width=20, show="*")
    txt1.pack()

    def savePassword():
        if txt.get() == txt1.get():
            hashedPassword = hashPassword(txt.get().encode('utf-8'))

            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [hashedPassword])
            db.commit()
            vaultScreen()

        else:
            lbl.config(text="Passwords don't match")

    btn = Button(window, text="Save", command=savePassword)
    btn.pack(pady=5)

#   Login screen #######################################################
def loginScreen():
    window.geometry("250x100")

    lbl = Label(window, text="Enter Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window)
    lbl1.pack()

    def getMasterPassword(): #hashowanie MD5
        checkhashedpassword = hashPassword(txt.get().encode("utf-8"))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [checkhashedpassword])

        print(checkhashedpassword)
        return cursor.fetchall()


    def checkPassword():
        password = getMasterPassword()

        if password:
            vaultScreen()

        else:
            txt.delete(0, 'end')
            lbl1.config(text="Wrong Password")

    btn = Button(window, text="Submit", command=checkPassword)
    btn.pack(pady=2)

#   Vault functionalities #################################################


def vaultScreen():
    for widget in window.winfo_children():  
        widget.destroy()

    def addEntry():
        text1 = "Platform"
        text2 = "Account"
        text3 = "Password"

        platform = popUp(text1)
        account = popUp(text2)
        password = popUp(text3)

        insert_fields = """INSERT INTO vault(platform, account, password)
        VALUES(?, ?, ?)"""

        cursor.execute(insert_fields, (platform, account, password))
        db.commit()
        vaultScreen()
    

    # Create buttons

# Updating an entry (password, account and platform) #######################
    def updateEntry(input):
        window = Tk()
        window.geometry("550x100")
        window.title("Choose what to change")

        myFrame = Frame(window)
        myFrame.pack(pady=20)

        #update password button
        myButton = Button(myFrame, text="Update password", command=partial(passwordChange, input))
        myButton.grid(row=0, column=2, padx=10)

        #update account button
        myButton = Button(myFrame, text="Update account", command=partial(accountChange, input))
        myButton.grid(row=0, column=1, padx=10)

        #update platform button
        myButton = Button(myFrame, text="Update platform", command=partial(platformChange, input))
        myButton.grid(row=0, column=0, padx=10)

    # Change password function
    def passwordChange(input):
        update = "Type new password"
        password = popUp(update)

        cursor.execute("UPDATE vault SET password = ? WHERE id = ?", (password, input,))
        db.commit()
        vaultScreen()

    # Change account function
    def accountChange(input):
        update = "Type new account"
        account = popUp(update)

        cursor.execute("UPDATE vault SET account = ? WHERE id = ?", (account, input,))
        db.commit()
        vaultScreen()

    # Change platform function
    def platformChange(input):
        update = "Type new platform"
        platform = popUp(update)

        cursor.execute("UPDATE vault SET platform = ? WHERE id = ?", (platform, input,))
        db.commit()
        vaultScreen()

    # Remove entry function
    def removeEntry(input):
        cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
        db.commit()
        vaultScreen()

    # Copy account function
    def copyAcc(input):
        window.clipboard_clear()
        window.clipboard_append(input)

    # Copy password function
    def copyPass(input):
        window.clipboard_clear()
        window.clipboard_append(input)

    # Creating a notepad
    def makeNotepad(input):
        window = tk.Tk()
        window.title("Notepad")
        #window.geometry("300x300")
        
        text = tk.Text(window, height=8, width=40)
        scroll = tk.Scrollbar(window)
        text.configure(yscrollcommand=scroll.set)
        text.pack(side=tk.LEFT)
        
        scroll.config(command=text.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        #TODO
        #insert_text = """text for test"""
        insert_text = """INSERT INTO notes(input)
            VALUES(?) """
        cursor.execute(insert_text, (input))
        db.commit()
        vaultScreen()
        
        text.insert(tk.END, insert_text)
        tk.mainloop()

        # Creating a button
        #TODO
    
        # Label frame.
        #lf = LabelFrame(window)
        #lf.pack(pady=50, padx=50)

        # Create Entry Box for number of characters.
        #myEntry = Entry(lf, font=("Calibri", 20))
        #myEntry.pack(ipady=150, ipadx=150)
        

        # Frame for buttons.
        #myFrame = Frame(window)
        #myFrame.pack(pady=20)


#   Window layout ###############################################
    window.geometry("700x300")
    window.minsize(650,300)
    window.maxsize(1000,450)

    main_frame = Frame(window)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    #text in main frame
    btn2 = Button(main_frame, text="Generate Password", command=passGenerator)
    
    btn2.place(relx=0.4, anchor=CENTER, y=10)

    btn = Button(main_frame, text="Store New", command=addEntry)
    btn.place(relx=0.6, anchor=CENTER, y=10)

    #creating a line
    my_canvas.pack(fill=BOTH, expand=1)
    my_canvas.create_line(200000, 120, 0, 25, fill="black")

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)
    my_canvas.create_window((0, 30), window=second_frame, anchor="nw")

    # Creating labels in second_frame
    lbl = Label(second_frame, text="Platform", borderwidth=1, relief="solid", background='grey')
    lbl.grid(row=2, column=0, padx=40)
    lbl = Label(second_frame, text="Account", borderwidth=1, relief="solid", background='grey')
    lbl.grid(row=2, column=1, padx=40)
    lbl = Label(second_frame, text="Password", borderwidth=1, relief="solid", background='grey')
    lbl.grid(row=2, column=2, padx=40)
    window.geometry("900x300")

    cursor.execute("SELECT * FROM vault")

#   Buttons Layout #######################################
    if cursor.fetchall() is not None:
        i = 0
        while True:
            cursor.execute("SELECT * FROM vault")
            array = cursor.fetchall()

            lbl1 = Label(second_frame, text=(array[i][1][0 : 10]))
            lbl1.grid(column=0, row=i + 3)
            lbl2 = Label(second_frame, text=(array[i][2][0 : 15]))
            lbl2.grid(column=1, row=i + 3)
            lbl3 = Label(second_frame, text="*****") 
            lbl3.grid(column=2, row=i + 3)
            btn2 = Button(second_frame, text="Copy Acc", command=partial(copyAcc, array[i][2]))
            btn2.grid(column=3, row=i + 3, pady=10)
            btn3 = Button(second_frame, text="Copy Pass", command=partial(copyPass, array[i][3]))
            btn3.grid(column=4, row=i + 3, pady=10)
            btn1 = Button(second_frame, text="Update", command=partial(updateEntry, array[i][0]))
            btn1.grid(column=5, row=i + 3, pady=10)
            btn = Button(second_frame, text="Delete", command=partial(removeEntry, array[i][0]))
            btn.grid(column=6, row=i + 3, pady=10)
            btn4 = Button(second_frame, text="Notepad", command=partial(makeNotepad, array[i][0]))
            btn4.grid(column=7, row=i + 3, pady=10)

            i = i + 1

            cursor.execute("SELECT * FROM vault")
            if len(cursor.fetchall()) <= i:
                break


cursor.execute("SELECT * FROM masterpassword")
if cursor.fetchall():
    loginScreen()
else:
    firstTimeScreen()
window.mainloop()