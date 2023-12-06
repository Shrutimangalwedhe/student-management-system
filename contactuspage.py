from tkinter import *
import sqlite3
from PIL import Image,ImageTk
from tkinter import messagebox as ms
import re
root= Tk()
root.title("You can contact us")
root.geometry('700x900')

Name=StringVar()
Email=StringVar()
Message=StringVar()

db = sqlite3.connect('project.db')
cursor = db.cursor()
create_table ='''CREATE TABLE IF NOT EXISTS contactus(
                            
                            Name TEXT,
                            Email TEXT,
                            Message TEXT
                          );'''
cursor.execute(create_table)
db.commit()

def insert():
    
    nam = Name.get()
    emai= Email.get()
    mess=message_text.get("1.0", "end-1c")
    if not nam.strip() or not emai.strip() or not mess.strip():
       ms.showinfo("Error!","name,email and message cannot be blank") 
       return
    db = sqlite3.connect('project.db')
    cursor = db.cursor()
    find_user=('SELECT * FROM registartionpage WHERE Name=? AND Email=?')
    cursor.execute(find_user,[(Name.get()),(Email.get())])
    result=cursor.fetchall()
    if not result:
       ms.showinfo("Error!","name and email could not be matched") 
       return
    else:
     insert_query='''INSERT INTO contactus(Name,Email,Message) VALUES(?,?,?);'''
     user_data=(nam,emai,mess)
     cursor.execute(insert_query,user_data)
     db.commit()
     db.close()
     ms.showinfo("Success","Reason submitted successfully")
    
    

image1=Image.open("studentcontactus.jpg")
image1=image1.resize((1550,900),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)

main_label=Label(root,text="STUDENT MANAGEMENT SYSTEM",bg="black",width=43,height=1,fg="white",font=("times",20,"bold"))
main_label.place(x=370,y=0)

sub_label=Label(root,text="Contact us",bg="#8B8970",width=20,height=2,fg="white",font=("times",20,"bold"))
sub_label.place(x=40,y=120)

logo_image = PhotoImage(file="personlogo.png")
logo_image = logo_image.subsample(8)  

name1_label = Label(root, text="Name", bg="#CDB7B5", width=15, height=1, fg="black", font=("times", 20, "bold"))
name1_label.place(x=40, y=230)


logo_label = Label(root, image=logo_image, width=52, height=30)
logo_label.place(x=40, y=230)

name1entry=Entry(root,textvar=Name,bg="#CDB7B5",width=20,font=("times",20,"bold"))
name1entry.place(x=350,y=230)


logo_image1 = PhotoImage(file="emaillogo.png")
logo_image1 = logo_image1.subsample(8)

email1_label = Label(root, text="Email", bg="#CDB7B5", width=15, height=1, fg="black", font=("times", 20, "bold"))
email1_label.place(x=40, y=290)

logo_label1 = Label(root, image=logo_image1, width=50, height=30)
logo_label1.place(x=40, y=292)

email1entry=Entry(root,textvar=Email,bg="#CDB7B5",width=20,font=("times",20,"bold"))
email1entry.place(x=350,y=290)

message1_label = Label(root, text="Message", bg="#CDB7B5", width=15, height=1, fg="black", font=("times", 20, "bold"))
message1_label.place(x=40, y=350)

message_text=Text(root,bg="#CDB7B5",height=8,width=40)
message_text.place(x=350,y=350)

scrollbar = Scrollbar(root, command=message_text.yview)
scrollbar.place(x=670, y=350, height=132)
message_text.config(yscrollcommand=scrollbar.set)


button=Button(root,text="Send Message",bg="#8B7E66",width=20,height=1,fg="white",font=("times",20,"bold"),command=insert)
button.place(x=40,y=550)





root.mainloop()