from tkinter import *

root = Tk()

root.title("Inches to Centimeters")

root.geometry("400x300")

frame = Frame(root, height=100, width=360, bg="#d0efff")

frame.place(x=20, y=20)

lbl1 = Label(frame, text="Length (inches)", bg="#3895D3", fg="white", width=15)

inch_entry = Entry(frame)

textbox = Text(root, bg="#BEBEBE", fg="black", width=40, height=5)

def convert():

    inches = float(inch_entry.get())

    centimeters = inches * 2.54

    textbox.delete("1.0", END)

    textbox.insert(END, "Length in centimeters = ")

    textbox.insert(END, centimeters)

btn = Button(root, text="Convert", command=convert, bg="red", fg="white")

lbl1.place(x=20, y=30)

inch_entry.place(x=180, y=30)

btn.place(x=140, y=140)

textbox.place(x=40, y=190)

root.mainloop()