from tkinter import *
import random
import string
import pyperclip

#==============================Function==============================
def generate():
    upper = []
    lower = [] 
    digits = []
    specials = []
    all = []
    allchar  = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    for i in range(upperC.get()):
        upper.append(random.choice(string.ascii_uppercase))
    for i in range(lowerC.get()):
        lower.append(random.choice(string.ascii_lowercase))
    for i in range(digitsC.get()):
        digits.append(random.choice(string.digits))
    for i in range(specialsC.get()):
        specials.append(random.choice(string.punctuation))

    all = upper + lower + digits + specials
    total = upperC.get() + lowerC.get() + digitsC.get() + specialsC.get()
    if total == lengthC.get():
        passwordField.delete(0,END)
        passwordField.insert(0, ''.join(random.sample(all,lengthC.get())))
    else:
        for i in range(lengthC.get() - total):
            all.append(random.choice(allchar))
        passwordField.delete(0,END)
        passwordField.insert(0, ''.join(random.sample(all,lengthC.get())))

def copyText():
    randomPass = passwordField.get()
    pyperclip.copy(random)


#==============================Design================================
root = Tk()
root.geometry("300x300")
root.title("Password Generator")
root.iconbitmap('icons/passGen.ico')

lenghtTitle = Label(root, text = 'Password length:').pack()
lengthC = IntVar()
spinLength = Spinbox(root, from_ = 6, to_ =24, textvariable = lengthC, width = 13, bd = 2).pack()

upperTitle = Label(root, text = 'Number of uppercase letters:').pack()
upperC = IntVar()
spinUpper = Spinbox(root, from_ = 0, to_ = 24, textvariable = upperC, width = 13, bd = 2).pack()

lowerTitle = Label(root, text = 'Number of lowercase letters:').pack()
lowerC = IntVar()
spinLower = Spinbox(root, from_ = 0, to_ = 24, textvariable = lowerC, width = 13, bd = 2).pack()

digitsTitle = Label(root, text = 'Number of digits:').pack()
digitsC = IntVar()
spinDigits = Spinbox(root, from_ = 0, to_ = 24, textvariable = digitsC, width = 13, bd = 2).pack()

specialTitle = Label(root, text = 'Number of special characters:').pack()
specialsC = IntVar()
spinSpecials = Spinbox(root, from_ = 0, to_ = 24, textvariable = specialsC, width = 13, bd = 2).pack()

generateButton = Button(root, text = "Generate", command = generate).pack(pady = 4)

passwordField = Entry(root, width = 30, bd = 2)
passwordField.pack()

copyButton = Button(root, text = "Copy", command = copyText).pack(pady = 4)

root.mainloop()
