from tkinter import *

root = Tk()

root.title("Product Calculator")

root.geometry("300x250")

Label(root, text="Enter First Number").pack()

num1_entry = Entry(root)

num1_entry.pack()

Label(root, text="Enter Second Number").pack()

num2_entry = Entry(root)

num2_entry.pack()

result = Label(root, text="")

result.pack(pady=10)

def multiply():

    num1 = float(num1_entry.get())

    num2 = float(num2_entry.get())

    product = num1 * num2

    result.config(text="Product = " + str(product))

Button(root, text="Calculate Product", command=multiply).pack(pady=10)

root.mainloop()