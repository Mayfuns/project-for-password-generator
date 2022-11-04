# import necessary modules
import random
from tkinter import *
from tkinter.ttk import *

def generate_password():
    """Create password using random and return password of 15 characters"""
    entry.delete(0, END)
    password_chars = ""
    password_len = 15   # fix password length
    
    # create a string of ascii characters between ord 33 and 127
    for char in range(33, 127):
        password_chars += chr(char)
 
    password = "" 
    for i in range(password_len):
        character = random.choice(password_chars)
        password += character
        
    return password


def generate():
    """generate  password using the generate_password function """
    password = generate_password()
    entry.insert(10, password)
    
# initialize tkinter
root = Tk()
root.title("Password Generator")

# Customize Tkinter
label = Label(root, text = "My Password")
label.grid(row = 0)
entry = Entry(root)
entry.grid(row=0, column=1)

password_button = Button(root, text="Generate", command=generate)
password_button.grid(row=0, column = 3)





root.mainloop()
