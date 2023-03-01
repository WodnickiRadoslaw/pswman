from tkinter import *
import secrets
import string


from random import randint
import random
import string
import PySimpleGUI as sg


def passwordGen(letter, numbers, specials, long) : 
    if letter == 0 :
        letter = ""
    else :
        letter = string.ascii_letters
    if numbers == 0 :
        numbers = ""
    else :
        numbers = string.digits
    if specials == 0 :
        specials = ""
    else :
        specials = string.punctuation
    alphabet = letter + numbers + specials
    password = ''.join(secrets.choice(alphabet) for i in range(long))
    return password
    
print(passwordGen(1, 0, 0, 10))

def rep() :
    numOfCharacters = entry2.get ()
    numOfCharacters = int(numOfCharacters)
    check1 = caseCheck1.get
    check2 = caseCheck2.get
    check3 = caseCheck3.get
    
    password = passwordGen(check1(),check2(),check3(),numOfCharacters)
    print(password)
    entry.delete(0, END)
    entry.insert(0, password)

def clipper():
    window.clipboard_clear()
    window.clipboard_append(entry.get())

window = Tk()
window.title("Password generator")
window.geometry('400x250')
window.minsize(400, 250)
window.maxsize(500, 300)

window.config(background= '#3D3D3D')

frame = Frame(window, bg = '#3D3D3D')


# Title window

label_title = Label(frame, text= 'Lenght of generated password:', font=("Calibri", 15), bg = '#3D3D3D', fg ='white')          
label_title.pack()                                                                                                                            



entry2 = Entry(frame, text= "", font=("Calibri", 15), bg = '#3D3D3D', fg ='white')                                                         
entry2.pack(fill=X)  

# Option of letters in password
caseCheck1 = IntVar()
case = Checkbutton(frame, text="letters",variable = caseCheck1 ,font=("Calibri", 15), onvalue=1, offvalue=0)
case.pack()

caseCheck2 = IntVar()
case1 = Checkbutton(frame, text="digits",variable = caseCheck2 ,font=("Calibri", 15), onvalue=1, offvalue=0)
case1.pack()

caseCheck3 = IntVar()
case2 = Checkbutton(frame, text="special signs",variable = caseCheck3 ,font=("Calibri", 15), onvalue=1, offvalue=0)
case2.pack()

button = Button(frame, text = "Generate password", font=("Calibri", 15), bg = '#3D3D3D', fg ='#000000', command = rep)                       
button.pack(fill=Y) 

# Entry 
entry = Entry(frame, font=("Calibri", 15), bg = '#a7a7a7', fg ='#000000')                                                                    
entry.pack(fill=X)  

# Copy button
clipBtn = Button(frame, text="Copy to Clipboard", font=("Calibri", 15), bg = '#3D3D3D', fg ='#000000', command=clipper)
clipBtn.pack(fill=Y)

frame.pack(expand = YES)
window.mainloop()