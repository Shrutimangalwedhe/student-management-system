from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as ms
import re
import sqlite3

root = Tk()
root.title("Remove Student Data")
root.geometry('800x800')

Name=StringVar()
Email=StringVar()
ID=IntVar()
Gender=StringVar()
Mobileno=IntVar()
Address=StringVar()
password=StringVar()

def insert():
    name = Name.get()
    email = Email.get()
    id1 = ID.get()
    gender = Gender.get()
    mobileno1 = Mobileno.get()
    addr= Address.get()
    passw = password.get()
    
    db = sqlite3.connect('project.db')
    cursor = db.cursor()
    select_query = '''SELECT * FROM addstudentdata WHERE Name=? AND Email=?;'''
    cursor.execute(select_query,[(Name.get()),(Email.get())])
    result = cursor.fetchall()
    if (name.isdigit() or (name == "")):
        ms.showinfo("Message", "please enter valid name")
    
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    return 

    if result:
        delete_query = '''DELETE FROM addstudentdata WHERE Name=? AND Email=?;'''
        cursor.execute(delete_query, (name, email))
        db.commit()
        
        ms.showinfo("success data deleted succesfully")
    else:
        ms.showinfo("error record not found for given name and id")


frame_alpr = LabelFrame(root,width=1535, height=900, bd=5, font=("times", 14, "bold"), bg="#836FFF")
frame_alpr.grid(row=0, column=0, sticky="nw")
frame_alpr.place(x=0, y=0)

name = Label(root, text="Name", bg="#8B475D", width=15, height=1, fg="white", font=("times", 20, "bold"))
name.place(x=360, y=200)

nameentry = Entry(root,textvar=Name, width=18, font=("times", 22, "bold"))
nameentry.place(x=700, y=200)

email11 = Label(root, text="Email ID", bg="#8B475D", width=15, height=1, fg="white", font=("times", 20, "bold"))
email11.place(x=360, y=300)

email1 = Entry(root,textvar=Email, width=18, font=("times", 22, "bold"))
email1.place(x=700, y=300)

button = Button(root,command=insert, text="REMOVE DATA", bg="black", width=15, height=1, fg="white", font=("times", 15, "bold"))
button.place(x=550, y=440)


root.mainloop()