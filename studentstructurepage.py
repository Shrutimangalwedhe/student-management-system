


from tkinter import *
import sqlite3

root = Tk()
root.title("Welcome to Student page")
root.geometry("550x200")

Username=StringVar()
Password=StringVar()

db = sqlite3.connect('project.db')
cursor = db.cursor()
create_table ='''CREATE TABLE IF NOT EXISTS studentloginpage(
                            
                            Username TEXT,
                            Password TEXT  
                          );'''
cursor.execute(create_table)
db.commit()

def insert():
    
    user_name = Username.get()
    passw = Password.get()
    
    db = sqlite3.connect('project.db')
    cursor = db.cursor()
    insert_query='''INSERT INTO studentloginpage(Username,Password) VALUES(?,?);'''
    user_data=(user_name,passw)
    cursor.execute(insert_query,user_data)
    db.commit()
    db.close()
    from subprocess import call
    call(["python","studentloginpage.py"])

# Set the background color of the window
root.configure(bg="#DEB887")

studentid_label = Label(root, text="Password", font=("Arial", 14), bg="#DEB887")
studentid_label.place(x=450, y=350)
studentid_entry = Entry(root,textvar=Username, font=("Arial", 12))
studentid_entry.place(x=550, y=350, width=300)

studentname_label = Label(root, text="Name", font=("Arial", 14), bg="#DEB887")
studentname_label.place(x=450, y=250)
studentname_entry = Entry(root,textvar=Password, font=("Arial", 12))
studentname_entry.place(x=550, y=250, width=300)


    

view_academic_record_button = Button(root, text="View Academic Record",font=("Arial", 12),command=insert)
view_academic_record_button.place(x=600, y=540, width=200)



root.mainloop()