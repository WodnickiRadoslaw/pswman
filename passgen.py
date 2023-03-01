from tkinter import *
from random import randint
import random
import string
import PySimpleGUI as sg

# def passGenerator():
#     upper=random.sample(string.ascii_uppercase, 2)
#     lower=random.sample(string.ascii_lowercase, 2)
#     digits=random.sample(string.digits, 2)
#     symbols=random.sample(string.punctuation, 2)

#     total=upper+lower+digits+symbols
#     total=random.sample(total, len(total))
#     total=''.join(total)
#     print(total)

#     sg.theme('DarkGrey')
#     sg.set_options(font='calibri 13')
#     layout=[
#         [sg.Text('Uppercase letters: '), sg.Push(), sg.Input(size=13)],
#         [sg.Text('Lowercase letters: '), sg.Push(), sg.Input(size=13)],
#         [sg.Text('Digits: '), sg.Push(), sg.Input(size=13)],
#         [sg.Text('Special symbols: '), sg.Push(), sg.Input(size=13)],
#         [sg.Button('OK', button_color = 'black')],
#         [sg.Text('Password: '), sg.Push(), sg.Multiline(size=13, no_scrollbar=True, disabled=True)],
#     ]

#     window=sg.Window('Password Generator', layout)

#     while True:
#         event, values=window.read()
#         if event=='OK'

#     window.close()
def passGenerator():
    # Password Generator window.
    window = Tk()

    window.title("Password Generator")

    myPassword = chr(randint(33,126))

    def newRand():
        pwEntry.delete(0, END)
        pwLength = int(myEntry.get())

        myPass = ""

        for x in range(pwLength):
            myPass += chr(randint(33, 126))

        pwEntry.insert(0, myPass)
        

    def clipper():
        window.clipboard_clear()
        window.clipboard_append(pwEntry.get())


    # Label frame.
    lf = LabelFrame(window, text="How many characters?")
    lf.pack(pady=50)

    # Create Entry Box for number of characters.
    myEntry = Entry(lf, font=("Calibri", 10))
    myEntry.pack(pady=20, padx=20)

    # Create entry box for returned password.
    pwEntry = Entry(window, text="", font=("Calibri", 10), bd=0)
    pwEntry.pack(pady=30)

    # Frame for buttons.
    myFrame = Frame(window)
    myFrame.pack(pady=20)

    # Create buttons
    myButton = Button(myFrame, text="Generate Password", command=newRand)
    myButton.grid(row=0, column=0, padx=10)



    clipBtn = Button(myFrame, text="Copy to Clipboard", command=clipper)
    clipBtn.grid(row=0, column=1, padx=10)


    window.mainloop()