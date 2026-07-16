from tkinter import *

from datetime import date

root = Tk()

root.title("Age Calculator")

root.geometry("350x300")

Label(root, text="Enter Date of Birth").pack()

day_entry = Entry(root)

day_entry.pack()

Label(root, text="Enter Month of Birth").pack()

month_entry = Entry(root)

month_entry.pack()

Label(root, text="Enter Year of Birth").pack()

year_entry = Entry(root)

year_entry.pack()

result = Label(root, text="")

result.pack(pady=10)

def calculate_age():

    day = int(day_entry.get())

    month = int(month_entry.get())

    year = int(year_entry.get())

    today = date.today()

    age = today.year - year

    if (today.month, today.day) < (month, day):

        age -= 1

    result.config(text="Present Age = " + str(age) + " years")

Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

root.mainloop()