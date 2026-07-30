from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Stationery Order Management")
root.geometry("700x450")

canvas = Canvas(root, width=700, height=450)
canvas.pack(fill="both", expand=True)

bg = PhotoImage(file="background.png")
canvas.create_image(0, 0, image=bg, anchor="nw")

frame = Frame(root)
canvas.create_window(350, 220, window=frame)

currency = StringVar(value="USD")

items = [
    ("Pen", 2),
    ("Notebook", 5),
    ("Pencil", 1),
    ("Eraser", 1)
]

entries = []

ttk.Label(frame, text="Item").grid(row=0, column=0)
ttk.Label(frame, text="Price").grid(row=0, column=1)
ttk.Label(frame, text="Quantity").grid(row=0, column=2)

for i, (name, price) in enumerate(items, start=1):

    ttk.Label(frame, text=name).grid(row=i, column=0)

    value = f"${price}" if currency.get() == "USD" else f"₹{price*83}"

    ttk.Label(frame, text=value).grid(row=i, column=1)

    qty = ttk.Entry(frame)
    qty.grid(row=i, column=2)

    entries.append((name, price, qty))


def total():
    total_price = 0

    for name, price, qty in entries:

        q = qty.get()

        if q.isdigit():
            q = int(q)

            cost = price if currency.get() == "USD" else price * 83

            total_price += cost * q

        elif q != "":
            messagebox.showerror("Error", f"Invalid quantity for {name}")
            return

    symbol = "$" if currency.get() == "USD" else "₹"

    messagebox.showinfo("Bill", f"Total = {symbol}{total_price}")


ttk.Radiobutton(frame, text="USD", variable=currency, value="USD").grid(row=6, column=0)

ttk.Radiobutton(frame, text="INR", variable=currency, value="INR").grid(row=6, column=1)

ttk.Button(frame, text="Calculate Total", command=total).grid(row=7, column=0, columnspan=3, pady=10)

root.mainloop()