from tkinter import *
from PIL import Image,ImageTk
root= Tk()
root.title("Welcome to Student Management System")
root.geometry('450x400')
image1=Image.open("studenthomepage1.jpg")
image1=image1.resize((1800,700),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=130)

main_label=Label(root,text="STUDENT MANAGEMENT SYSTEM",bg="black",width=43,height=1,fg="white",font=("times",20,"bold"))
main_label.place(x=330,y=0)

sub_label=Label(root,bg="#616161",width=100,height=2,fg="white",font=("times",20,"bold"))
sub_label.place(x=0,y=50)

def register():
    from subprocess import call
    call(["python","registrationpage.py"])

def login():
    from subprocess import call
    call (["python","loginpage.py"])

def about():
    from subprocess import call
    call(["python","AboutUspage.py"])
    
def contact():
     from subprocess import call
     call(["python","contactuspage.py"])
     
def admin_b():
    from subprocess import call
    call(["python","admin page structure.py"])
    
def student_b():
    from subprocess import call
    call(["python","registrationpage.py"])
     
     
home_button=Button(root,text="Home",bg="#DEB887",width=10,height=1,fg="white",font=("times",15,"bold"))
home_button.place(x=150,y=65)

registration_button=Button(root,text="Registration",command=register,bg="#DEB887",width=10,height=1,fg="white",font=("times",15,"bold"))
registration_button.place(x=350,y=65)

login_button=Button(root,text="login",command=login,bg="#DEB887",width=10,height=1,fg="white",font=("times",15,"bold"))
login_button.place(x=550,y=65)

about_button=Button(root,text="About Us",command=about,bg="#DEB887",width=10,height=1,fg="white",font=("times",15,"bold"))
about_button.place(x=750,y=65)

contact_button=Button(root,text="Contact Us",command=contact,bg="#DEB887",width=10,height=1,fg="white",font=("times",15,"bold"))
contact_button.place(x=950,y=65)

admin_button=Button(root,text="Admin",command=admin_b,bg="#CD950C",width=20,height=1,fg="white",font=("times",15,"bold"))
admin_button.place(x=400,y=350)

student_button=Button(root,text="Student",command=student_b,bg="#CD950C",width=20,height=1,fg="white",font=("times",15,"bold"))
student_button.place(x=700,y=350)

root.mainloop()