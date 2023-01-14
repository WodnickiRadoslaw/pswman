from tkinter import *
#from updatePassword import updateEntry
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


with sqlite3.connect("dbMain.db") as db:
    cursor = db.cursor()

def popUp(text):
    answer = simpledialog.askstring("input string", text)
    return answer

def updateAll():
    # Password Generator window.

    window = Tk()
    window.geometry("550x100")
    window.title("Choose what to change")


    def updatePsw(input):

        update = "Type new password"
        password = popUp(update)

        cursor.execute("UPDATE vault SET password = ? WHERE id = ?", (password, input,))
        db.commit()
        updateAll()

    def updateAcc(input):

        update = "Type new account"
        account = popUp(update)

        cursor.execute("UPDATE vault SET account = ? WHERE id = ?", (account, input,))
        db.commit()
        updateAll()

    def updatePlt(input):

        update = "Type new platform"
        platform = popUp(update)

        cursor.execute("UPDATE vault SET password = ? WHERE id = ?", (platform, input,))
        db.commit()
        updateAll()

    # Frame for buttons.


    myFrame = Frame(window)
    myFrame.pack(pady=20)

    updatePassword = Button(myFrame, text="Update password", command=updatePsw)
    updatePassword.grid(row=0, column=2, padx=10)

    updateAccount = Button(myFrame, text="Update Account", command=updateAcc)
    updateAccount.grid(row=0, column=1, padx=10)    

    updatePlatform = Button(myFrame, text="Update platform", command=updatePlt)
    updatePlatform.grid(row=0, column=0, padx=10)


    

    #window.mainloop()