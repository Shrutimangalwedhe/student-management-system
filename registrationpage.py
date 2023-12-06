from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox as ms
import re
root = Tk()
root.title("Welcome to registration page")
root.geometry('800x800')   

image1 = Image.open("registrationimage.png")
image1 = image1.resize((810, 735), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image1)
background_label = Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=710, y=60)


Name=StringVar()
Email=StringVar()
Mobile_number=IntVar()
Gender=StringVar()
Age=IntVar()
Username=StringVar()
password=StringVar()


db = sqlite3.connect('project.db')
cursor = db.cursor()
create_table ='''CREATE TABLE IF NOT EXISTS registartionpage(
                            Name TEXT,
                            Email TEXT,
                            Mobile_number INTEGER,
                            Gender TEXT,
                            Age INTEGER,
                            Username TEXT,
                            password TEXT  
                          );'''
cursor.execute(create_table)
db.commit()


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
    mobile_no = Mobile_number.get()
    gender = gender_var.get()
    age = Age.get()
    user_name = Username.get()
    passw = password.get()
    
    db = sqlite3.connect('project.db')
    cursor = db.cursor()
    find_user=('SELECT * FROM registartionpage WHERE Username=?')
    cursor.execute(find_user,[(Username.get())])
 # to check mail
    #regex = '^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$'
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
    elif((len(str(mobile_no)))<10 or len(str((mobile_no)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((age > 100) or (age == 0)):
        ms.showinfo("Message", "Please Enter valid age")
    elif (cursor.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    
    elif (gender == False):
        ms.showinfo("Message", "Please Enter gender")
    elif (passw == ""):
        ms.showinfo("Message", "Please Enter valid password")
    elif(passw=="")or(password_check(passw))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
        
        
    else:
        db = sqlite3.connect('project.db')
        cursor = db.cursor()
        insert_query='''INSERT INTO registartionpage(Name,Email,Mobile_number,Gender,Age,Username,password) VALUES(?,?,?,?,?,?,?);'''
        user_data=(name,email,mobile_no,gender,age,user_name,passw)
        cursor.execute(insert_query,user_data)
        db.commit()
        db.close()
        ms.showinfo('Success!', 'Account Created Successfully !')
            # window.destroy()
            #window.destroy()
        from subprocess import call
        call(["python","loginpage.py"])
        
    
        




main_label=Label(root,text="STUDENT MANAGEMENT SYSTEM",bg="black",width=43,height=1,fg="white",font=("times",20,"bold"))
main_label.place(x=370,y=0)

frame_alpr = LabelFrame(root,width=700, height=735, bd=5, font=("times", 14, "bold"), bg="#008B8B")
frame_alpr.grid(row=0, column=0, sticky="nw")
frame_alpr.place(x=10, y=60)

loginlabel=Label(root,text="REGISTRATION",bg="black",width=20,height=1,fg="white",font=("times",20,"bold"))
loginlabel.place(x=180,y=80) 

name = Label(root, text="Name", bg="#BA55D3", width=15, height=1, fg="white", font=("times", 20, "bold"))
name.place(x=40, y=150)

nameentry = Entry(root,textvar=Name, width=18, font=("times", 22, "bold"))
nameentry.place(x=330, y=150)

email = Label(root, text="Email", bg="#BA55D3", width=15, height=1, fg="white", font=("times", 20, "bold"))
email.place(x=40, y=210)

emailentry = Entry(root,textvar=Email, width=18, font=("times", 22, "bold"))
emailentry.place(x=330, y=210)

mobileno = Label(root, text="Mobile no", bg="#BA55D3", width=15, height=1, fg="white", font=("times", 20, "bold"))
mobileno.place(x=40, y=270)

mobileentry = Entry(root,textvar=Mobile_number, width=18, font=("times", 22, "bold"))
mobileentry.place(x=330, y=270)

gender = Label(root, text="Gender", bg="#BA55D3", width=15, height=1, fg="white", font=("times", 20, "bold"))
gender.place(x=40, y=330)

gender_var=StringVar()
gender_var.set("Female")

gender_radio1=Radiobutton(root,text="Male",width=10,variable=gender_var,value="Male",font=("times", 14, "bold"))
gender_radio1.place(x=332,y=335)

gender_radio2=Radiobutton(root,text="Female",width=10,variable=gender_var,value="Female",font=("times", 14, "bold"))
gender_radio2.place(x=490,y=335)

age = Label(root, text="Age", bg="#BA55D3", width=15, height=1, fg="white", font=("times", 20, "bold"))
age.place(x=40, y=390)

age_spinbox=Spinbox(root, width=18,font=("times",20,"bold"),from_=0, to=100,textvar=Age)
age_spinbox.place(x=330,y=390)

Username1 = Label(root, text="User Name", bg="#BA55D3", width=15, height=1, fg="white", font=("times", 20, "bold"))
Username1.place(x=40, y=450)

usernameentry = Entry(root,textvar=Username, width=18, font=("times", 22, "bold"))
usernameentry.place(x=330, y=450)

Password = Label(root, text="Password", bg="#BA55D3", width=15, height=1, fg="white", font=("times", 20, "bold"))
Password.place(x=40, y=510)

passwordentry = Entry(root,textvar=password, width=18, font=("times", 22, "bold"))
passwordentry.place(x=330, y=510)

button = Button(root, text="REGISTER", bg="grey", width=15, height=1, fg="white", font=("times", 15, "bold"),command=insert)
button.place(x=120, y=670)

button1 = Button(root, text="CANCEL", bg="grey", width=15, height=1, fg="white", font=("times", 15, "bold"))
button1.place(x=350, y=670)



root.mainloop()