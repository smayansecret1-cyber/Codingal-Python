from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Reading Schedule Planner")
root.geometry("300x200")


def open_planner():
    top = Toplevel(root)
    top.title("Planner")
    top.geometry("350x250")

    Label(top, text="Total Pages").pack()
    pages_entry = Entry(top)
    pages_entry.pack()

    Label(top, text="Pages Per Day").pack()
    perday_entry = Entry(top)
    perday_entry.pack()

    result = Label(top, text="")
    result.pack(pady=10)

    def calculate():
        try:
            total = int(pages_entry.get())
            perday = int(perday_entry.get())

            days = total // perday
            remaining = total % perday

            result.config(
                text=f"Complete Days: {days}\nRemaining Pages: {remaining}"
            )

        except:
            messagebox.showerror("Error", "Please enter valid numbers")

    Button(top, text="Calculate", command=calculate).pack(pady=10)


Button(root, text="Open Reading Planner", command=open_planner).pack(pady=60)

root.mainloop()