from logging import root
from queue import Empty
import string 
from tkinter import *

#==============================================================Functions========================================================================
#time convertor
def TimeConvertor(time):
    century = time // (100 * 10 * 365 * 24 * 3600)
    time = time % (100 * 10 * 365 * 24 * 3600)
    decade = time // (10 * 365 * 24 * 3600)
    time = time % (10 * 365 * 24 * 3600)
    years = time // (365 * 24 * 3600)
    time = time % (365 * 24 * 3600)
    weeks = time // (7 * 24 * 3600)
    time = time % (7 * 24 * 3600)
    days = time // (24 * 3600)
    time = time % (24 * 3600)
    hours = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time // 60
    time %= 60
    milliseconds = time
    if int(century) == 0 and int(decade) == 0 and int(years) == 0 and int(weeks) == 0 and int(days) == 0 and int(hours) == 0 and int(minutes) == 0 and int(seconds) == 0 and int(milliseconds) == 0:
        timeField.insert(0,"INSTANT")
    else:
        timeField.insert(0,f"{int(century)}:{int(decade)}:{int(years)}:{int(weeks)}:{int(days)}:{int(hours)}:{int(minutes)}:{int(seconds)}:{int(milliseconds)}")

# length score
def PasswordLengthScore(length):
    length_score = 0

    if length > 8:
        length_score += 1
    if length > 10:
        length_score += 1
    if length > 12:
        length_score += 1  

    return length_score

# upper case characters score 
def PasswordUpperCaseScore(upper_case):
    uCase_score = 0

    if upper_case >= 1:
        uCase_score += 1
    if upper_case >= 3:
        uCase_score += 1
    if upper_case >= 5:
        uCase_score += 1  
    
    return uCase_score

# lower case characters score 
def PasswordLowerCaseScore(lower_case):
    lCase_score = 0

    if lower_case >= 1:
        lCase_score += 1
    if lower_case >= 3:
        lCase_score += 1
    if lower_case >= 5:
        lCase_score += 1  

    return lCase_score

# special characters score 
def PasswordSpecialScore(special):
    special_score = 0

    if special >= 1:
        special_score += 1
    if special >= 2:
        special_score += 1
    if special >= 3:
        special_score += 1  

    return special_score

# digits score
def PasswordDigitsScore(digits):
    digits_score = 0

    if digits >= 1:
        digits_score += 1
    if digits >= 3:
        digits_score += 1
    if digits >= 5:
        digits_score += 1  

    return digits_score

# input password
def passStr():
    password = passC.get()
    # variable declaration
    upper_case = 0
    lower_case = 0
    special = 0
    digits = 0
    length = len(password)
    total_score = 0
    space_depth = 0
    no = 0
    # count all the characters
    for c in password:
        if c in string.ascii_uppercase:
            upper_case += 1
        elif c in string.ascii_lowercase:
            lower_case += 1
        elif c in string.punctuation:
            special += 1
        elif c in string.digits:
            digits += 1

    # open file
    with open('commonPass.txt', 'r') as f:
        common = f.read().splitlines()

    # chack for common password
    if password in common:
        moreField.delete('1.0',END)
        strangthField.delete(0,END)
        timeField.delete(0,END)
        moreField.insert(INSERT,"Password found in a common list. Score: 0/15")
        strangthField.insert(0,"COMMON")
        timeField.insert(0,"INSTANT")
        no = 1
    # printing details about the password
    if no==0:
        moreField.delete('1.0',END)
        strangthField.delete(0,END)
        timeField.delete(0,END)
        length_score = PasswordLengthScore(length)
        moreField.insert(INSERT,f"Password length {length}: +{length_score}p\n")

        uCase_score = PasswordUpperCaseScore(upper_case)
        moreField.insert(INSERT,f"Password uppercase characters {upper_case}: +{uCase_score}p\n")

        lCase_score = PasswordLowerCaseScore(lower_case)
        moreField.insert(INSERT,f"Password lowercase characters {lower_case}: +{lCase_score}p\n")

        special_score = PasswordSpecialScore(special)
        moreField.insert(INSERT,f"Password special character: {special}: +{special_score}p\n")

        digits_score = PasswordDigitsScore(digits)
        moreField.insert(INSERT,f"Password digits: {digits}: +{digits_score}p")

        # adding all the scores
        total_score = length_score + uCase_score + lCase_score + special_score + digits_score

        # give a security level to the password
        if total_score <= 3: 
            strangthField.insert(0,f"VERY WEAK! Score {total_score} / 15")

        if total_score > 3 and total_score <= 6:
            strangthField.insert(0,f"WEAK! Score {total_score} / 15")

        if total_score > 6 and total_score <= 9: 
            strangthField.insert(0,f"MEDIUM! Score {total_score} / 15")

        if total_score > 9 and total_score <= 12: 
            strangthField.insert(0,f"STRONG! Score {total_score} / 15")

        if total_score > 12 and total_score <= 15: 
            strangthField.insert(0,f"VERY STRONG! Score {total_score} / 15")

        # Brute Force Password “Search Space” Calculator

        # search space depth (alphabet)
        if lower_case > 0:
            space_depth += 26 # 26 lower case characters
        if upper_case > 0: 
            space_depth += 26 # 26 upper case characters
        if special > 0:
            space_depth += 33 # 33 special characters
        if digits > 0: 
            space_depth += 10 # 10 digits

        # exact search space size (count of all possible passwords with this alphabet and this length)
        space_size = space_depth**length

        #Time Required to Exhaustively Search this Password's Space
        # a computer can guess 100,000,000,000 passwords per second
        time_req = space_size / 100000000000
        TimeConvertor(time_req)
#==========================================================Design====================================================================
root2 = Tk()
root2.geometry("450x290")
root2.title("Password Strength")
root2.iconbitmap('icons/passStr.ico')

passTitle = Label(root2, text = 'Type your password:').pack()
passC = StringVar()
passField = Entry(root2, textvariable = passC,width = 40, bd = 2)
passField.pack()

strangthTitle = Label(root2, text = 'Password securiry level:').pack()
strangthC = StringVar()
strangthField = Entry(root2, width = 40, justify=CENTER, bd = 2)
strangthField.pack()

timeTitle = Label(root2, height = 2,text = 'Crack time:\n(centuries:decades:years:weeks:days:hours:minutes:seconds:milliseconds)').pack()
timeC = StringVar()
timeField = Entry(root2, width = 40, justify=CENTER, bd = 2)
timeField.pack()

copyButton = Button(root2, text = "Check", command = passStr).pack(pady = 4)

moreTitle = Label(root2, text = 'More details:').pack()
moreC = StringVar()
moreField = Text(root2, width = 40, height = 5,bd = 2)
moreField.pack()

root2.mainloop()