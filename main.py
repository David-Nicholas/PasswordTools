from tkinter import *
import subprocess
#====================================Functions===============================================================
def openpsswordgen():
    tool1 = 'passwordgen.py'
    p1 = subprocess.Popen(tool1, shell = True)
    out, err = p1.communicate()
    print(err)
    print(out)

def openpasswordstr():
    tool2 = 'passwordstr.py'
    p2 = subprocess.Popen(tool2, shell = True)
    out, err = p2.communicate()
    print(err)
    print(out)
#====================================Design=================================================================
rootmain = Tk()
rootmain.geometry("300x70")
rootmain.title("Password Tools")
rootmain.iconbitmap('icons/main.ico')

passGenButton = Button(rootmain, text = "Password generator", command = openpsswordgen, width = 20).pack(pady = 4)
passStrButton = Button(rootmain, text = "Strength check", command = openpasswordstr, width = 20).pack(pady = 4)

rootmain.mainloop()