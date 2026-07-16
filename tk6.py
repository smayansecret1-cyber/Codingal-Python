from tkinter import *

window = Tk()

window.title("Event Handler")

window.geometry("500x500")

def handle_keypress(event):

    print("\n",event.char)

window.bind("<Key>", handle_keypress)

def handle_clickL(event):

    print("\nI did a left click!")

def handle_clickR(event):

    print("\nI did a right click!")

button = Button(text="Click me!")

button.pack()

button.bind("<Button-1>", handle_clickL)

button.bind("<Button-3>", handle_clickR)

window.mainloop()