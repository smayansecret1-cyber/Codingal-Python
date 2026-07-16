from tkinter import *

from tkinter import messagebox

Root=Tk()

Root.geometry("200x200")

def msg():

    messagebox.showerror("This is a error")

    messagebox.showinfo("This is a info box")

    messagebox.showerror("This is a error")

    messagebox.askquestion("This is a question")

button=Button(Root,text="Click to learn about types of show",command=msg)

button.place(x=40,y=80)

Root.mainloop()