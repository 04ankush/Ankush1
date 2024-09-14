import tkinter
from tkinter import messagebox
import tkinter as tk

tag= tk.Tk()
tag.title("EXAM FORM")
tag.geometry("1920x1080")
tag.config(bg="#C8A24F")


def message():
    messagebox.showinfo("Exam Form","successfully filled")

btn=tkinter.Button(tag,text="submit",command=message,width=9,height=2)
btn.place(x=630,y=500)


#--------------------------------------------------------------------------------------------------

label3=tk.Label(tag,text="ENTER YOUR FIRST NAME ",
                     fg="white",
                     bg="black",)
label3.place(x=430,y=85)
label3=tkinter.Entry(tag,bd=4)
label3.place(x=600,y=83)

#--------------------------------------------------------------------------------------------------

label4=tk.Label(tag,text="ENTER YOUR LAST NAME ",
                     fg="white",
                     bg="black",)
label4.place(x=410,y=161)
label4=tkinter.Entry(tag,bd=4)
label4.place(x=600,y=158)


#------------------------------------------------------------------------------------------------

label5=tk.Label(tag,text="ENTER YOUR AGE ",
                     fg="white",
                     bg="black",)
label5.place(x=440,y=240)
label5=tkinter.Entry(tag,bd=4)
label5.place(x=600,y=237)



#------------------------------------------------------------------------------------------------

label6=tk.Label(tag,text="ENTER YOUR MOBILE NUMBER  ",
                     fg="white",
                     bg="black",)
label6.place(x=370,y=320)
label6=tkinter.Entry(tag,bd=4)
label6.place(x=600,y=317)



#-------------------------------------------------------------------------------------------

label7=tk.Label(tag,text="ENTER YOUR E-MAIL ID ",
                     fg="white",
                     bg="black",)
label7.place(x=410,y=400)
label7=tkinter.Entry(tag,bd=4)
label7.place(x=600,y=398)


#-------------------------------------------------------------------------------------------












tag.mainloop()


