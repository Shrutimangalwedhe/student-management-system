from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox as ms
import re


root = Tk()
root.title("welcome to student login")
root.geometry('800x800')  

Name=StringVar()
Email=StringVar()

db = sqlite3.connect('project.db')
cursor = db.cursor()
create_table ='''CREATE TABLE IF NOT EXISTS studentattendance(

                            
                            Name TEXT,
                            Email TEXT,
                            Subject TEXT,
                            Attendance INTEGER
                            
                          );'''
cursor.execute(create_table)
db.commit()

def insert():
    name = Name.get()
    email =Email.get()

    db = sqlite3.connect("project.db")
    cursor = db.cursor()

    select_query=("SELECT * FROM registartionpage WHERE Name=? AND Email=?")
    cursor.execute(select_query,[(Name.get()),(Email.get())])
    result = cursor.fetchall()
    db.close()
    if result:
        msg=""
        print(msg)
        ms.showinfo("Fetched Record Successfully!")
    else:
         ms.showinfo("oops!","Name and Email are not found match")
    
    
   
    

"""frame_alpr = LabelFrame(root,width=700, height=850, bd=5, font=("times", 14, "bold"), bg="#5F9EA0")
frame_alpr.grid(row=0, column=0, sticky="nw")
frame_alpr.place(x=10, y=10)

frame_alpr = LabelFrame(root,width=810, height=790, bd=5, font=("times", 14, "bold"), bg="#EEC591")
frame_alpr.grid(row=0, column=0, sticky="nw")
frame_alpr.place(x=710, y=10)"""

root.configure(bg="pink")

name1_label = Label(root, text="Name", font=("Arial", 14), bg="lightblue")
name1_label.place(x=450, y=250)

name1_entry = Entry(root,textvar=Name, font=("Arial", 12))
name1_entry.place(x=550, y=250, width=300)

Email1_label = Label(root, text="Email id", font=("Arial", 14), bg="lightblue")
Email1_label.place(x=450, y=350)

Email1_entry = Entry(root,textvar=Email, font=("Arial", 12))
Email1_entry.place(x=550, y=350, width=300)

att_button = Button(root, text="View Attendance", font=("Arial", 12),command=insert)
att_button.place(x=600, y=470 )


root.mainloop()