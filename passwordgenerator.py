from tkinter import *
import secrets
import string
import tkinter as tk


y = 0
x = 0

def rep():
    y = str(entry2.get())
    x = y.isdigit()

    if y.isdigit():
        print (x)
        numOfCharacters = int(y)

        check1 = caseCheck1.get
        check2 = caseCheck2.get
        check3 = caseCheck3.get
        
        password = passwordGen(check1(),check2(),check3(),numOfCharacters)
        print(password)
        entry.delete(0, END)
        entry.insert(0, password)
    else:
        entry.delete(0, END)
        entry.insert(0, "error")

def clipper():
    window2.clipboard_clear()
    window2.clipboard_append(entry.get())

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

window2 = Tk()
window2.title("Password generator")
window2.geometry('400x250')
window2.minsize(400, 250)
window2.maxsize(500, 300)

window2.config(background= '#3D3D3D')

frame = Frame(window2, bg = '#3D3D3D')

# Title window2
label_title = Label(frame, text= 'Lenght of generated password:', font=("Calibri", 15), bg = '#3D3D3D', fg ='white')          
label_title.pack()                                                                                                                            

entry2 = Entry(frame, text= "", font=("Calibri", 15), bg = '#3D3D3D', fg ='white')                                                         
entry2.pack(fill=X)  

# Option of letters in password
caseCheck1 = IntVar()
case = Checkbutton(frame, text="letters",variable = caseCheck1 ,font=("Calibri", 15), offvalue=0, onvalue=1)
case.pack()

caseCheck2 = IntVar()
case1 = Checkbutton(frame, text="digits",variable = caseCheck2 ,font=("Calibri", 15), offvalue=0, onvalue=1)
case1.pack()

caseCheck3 = IntVar()
case2 = Checkbutton(frame, text="special signs",variable = caseCheck3 ,font=("Calibri", 15), offvalue=0, onvalue=1)
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
window2.mainloop()






