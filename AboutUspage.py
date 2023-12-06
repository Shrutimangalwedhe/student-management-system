from tkinter import *
from PIL import Image,ImageTk

root= Tk()
root.title("About us")
root.geometry('700x900')
image1=Image.open("studentaboutus.jpg")
image1=image1.resize((1550,900),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)

main_label=Label(root,text="STUDENT MANAGEMENT SYSTEM",bg="black",width=43,height=1,fg="white",font=("times",20,"bold"))
main_label.place(x=370,y=0)




aboutus_label=Label(root,text="ABOUT US",bg="#2F4F4F",width=20,height=2,fg="white",font=("times",20,"bold"))
aboutus_label.place(x=70,y=210)

text = """
Schools and Universities are the foundation of knowledge and an educational body on which students rely upon.
Therefore, they need to maintain a proper database of its students to keep all the updated records and easily share information with students.

Most schools and Universities count on an advanced software tool known as 'Student Information System (SIS)'\n to keep all their student records and administrative operations including, examinations, attendance, and other activities.

Over the recent years, the performance and efficiency of the education industry have been enhanced by using the Student Management System.
This tool has productively taken over the workload of the admin department with its well-organized, easy, and reliable online school management software.
"""

text_label=Label(root, text=text,width=110,height=10,bg="#C1CDCD",fg="black",font=("times",15,"bold"))
text_label.place(x=70, y=350)




root.mainloop()
