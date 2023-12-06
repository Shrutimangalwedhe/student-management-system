from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox as ms
import re
root = Tk()
root.title("Update Student Data")
root.geometry('800x800')   

Name=StringVar()
Email=StringVar()
ID=IntVar()
Gender=StringVar()
Mobileno=IntVar()
Address=StringVar()
password=StringVar()

def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        print('length should not be greater than 20')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False

    if val:
        return val

def insert():
    name = Name.get()
    email = Email.get()
    id1 = ID.get()
    gender = gender_var.get()
    mobileno1 = Mobileno.get()
    addr= Address.get()
    passw = password.get()
    
    db = sqlite3.connect('project.db')
    cursor = db.cursor()
    find_user=('SELECT * FROM addstudentdata WHERE Name=? ')
    cursor.execute(find_user,[(Name.get())])
    result=cursor.fetchall()
    db = sqlite3.connect('project.db')
    cursor = db.cursor()
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (name.isdigit() or (name == "")):
        ms.showinfo("Message", "please enter valid name")
    
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif(not isinstance(id1,int)or id1==0):
         ms.showinfo("Message", "please enter valid id")
    elif (gender == False):
        ms.showinfo("Message", "Please Enter gender")
     
    elif((len(str(mobileno1)))<10 or len(str((mobileno1)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    
    elif (addr.isdigit() or (addr == "")):
        ms.showinfo("Message", "please enter valid address")
   
    elif (passw == ""):
         ms.showinfo("Message", "Please Enter valid password")
    elif(passw=="")or(password_check(passw))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif result:
        update_query='''UPDATE addstudentdata SET Email=?,ID=?,Gender=?,Mobileno=?,Address=?,password=? WHERE Name=?'''
        update_data=(email,id1,gender,mobileno1,addr,passw,name)
        cursor.execute(update_query,update_data)
        db.commit()
        db.close()
        ms.showinfo("success data updated succesfully")
    else:
        ms.showinfo("error record not found for given name")

frame_alpr = LabelFrame(root,width=700, height=850, bd=5, font=("times", 14, "bold"), bg="#CD9B1D")
frame_alpr.grid(row=0, column=0, sticky="nw")
frame_alpr.place(x=10, y=10)

name = Label(root, text="Name", bg="#8B0000", width=15, height=1, fg="white", font=("times", 20, "bold"))
name.place(x=40, y=150)

nameentry = Entry(root,textvar=Name, width=18, font=("times", 22, "bold"))
nameentry.place(x=330, y=150)

updateemail = Label(root, text="Update Email", bg="#8B0000", width=15, height=1, fg="white", font=("times", 20, "bold"))
updateemail.place(x=40, y=210)

updateemailentry = Entry(root,textvar= Email,width=18, font=("times", 22, "bold"))
updateemailentry.place(x=330, y=210)

updatestudentid = Label(root, text="Update ID", bg="#8B0000", width=15, height=1, fg="white", font=("times", 20, "bold"))
updatestudentid.place(x=40, y=270)

updatestudentid = Entry(root, textvar=ID,width=18, font=("times", 22, "bold"))
updatestudentid.place(x=330, y=270)

updategender = Label(root, text="Update Gender", bg="#8B0000", width=15, height=1, fg="white", font=("times", 20, "bold"))
updategender.place(x=40, y=330)

gender_var=StringVar()
gender_var.set("Female")

gender_radio1=Radiobutton(root,text="Male",width=10,variable=gender_var,value="Male",font=("times", 14, "bold"))
gender_radio1.place(x=332,y=335)

gender_radio2=Radiobutton(root,text="Female",width=10,variable=gender_var,value="Female",font=("times", 14, "bold"))
gender_radio2.place(x=490,y=335)

updatemobileno= Label(root, text="Update Mobileno", bg="#8B0000", width=15, height=1, fg="white", font=("times", 20, "bold"))
updatemobileno.place(x=40, y=390)

updatemobileno=Entry(root,textvar=Mobileno, width=18,font=("times",22,"bold"))
updatemobileno.place(x=330,y=390)

updateAddress = Label(root, text="Update Address", bg="#8B0000", width=15, height=1, fg="white", font=("times", 20, "bold"))
updateAddress.place(x=40, y=450)

updateAdressentry = Entry(root,textvar=Address, width=18, font=("times", 22, "bold"))
updateAdressentry.place(x=330, y=450)

updatepassword = Label(root, text="Update Password", bg="#8B0000", width=15, height=1, fg="white", font=("times", 20, "bold"))
updatepassword.place(x=40, y=510)

updatepasswordentry = Entry(root,textvar=password, width=18, font=("times", 22, "bold"))
updatepasswordentry.place(x=330, y=510)

button = Button(root,command=insert, text="UPDATE DATA", bg="#8B6969", width=15, height=1, fg="white", font=("times", 15, "bold"))
button.place(x=200, y=650)

image1 = Image.open("updatestudentdataimage.jpg")
image1 = image1.resize((810, 790), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image1)
background_label = Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=710, y=10)

root.mainloop()