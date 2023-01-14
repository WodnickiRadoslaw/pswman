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

def updateEntry(input):

    update = "Type new password"
    password = popUp(update)

    cursor.execute("UPDATE vault SET password = ? WHERE id = ?", (password, input,))
    db.commit()

