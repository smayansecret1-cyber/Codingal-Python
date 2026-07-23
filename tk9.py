import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def main():
    root = tk.Tk()
    root.title("Denomination Counter")
    root.configure(bg="light blue")
    root.geometry("650x400")

    try:
        upload = Image.open("pngtree-clipart-of-a-money-bag-filled-with-gold-coins-featuring-dollar-png-image_14789520.png")
        upload = upload.resize((300, 300))
        image = ImageTk.PhotoImage(upload)

        label = tk.Label(root, image=image, bg="light blue")
        label.image = image
        label.place(x=180, y=20)

    except FileNotFoundError:
        tk.Label(root, text="Image not found", bg="light blue").place(x=180, y=20)

    label1 = tk.Label(
        root,
        text="Hey User! Welcome to Denomination Counter Application.",
        bg="light blue"
    )
    label1.place(relx=0.5, y=340, anchor=tk.CENTER)

    button1 = tk.Button(
        root,
        text="Let's get started!",
        command=lambda: topwin(root),
        bg="brown",
        fg="white"
    )
    button1.place(x=260, y=360)

    root.mainloop()


def topwin(root):
    top = tk.Toplevel(root)
    top.title("Denominations Calculator")
    top.configure(bg="cyan")
    top.geometry("600x500+50+50")

    amount_label = tk.Label(top, text="Enter total amount", bg="light grey")
    amount_entry = tk.Entry(top)

    result_label = tk.Label(
        top,
        text="Here are number of notes for each denomination",
        bg="light grey"
    )

    label_1000 = tk.Label(top, text="1000", bg="light grey")
    label_500 = tk.Label(top, text="500", bg="light grey")
    label_100 = tk.Label(top, text="100", bg="light grey")
    label_50 = tk.Label(top, text="50", bg="light grey")
    label_20 = tk.Label(top, text="20", bg="light grey")
    label_10 = tk.Label(top, text="10", bg="light grey")
    label_5 = tk.Label(top, text="5", bg="light grey")

    entry_1000 = tk.Entry(top)
    entry_500 = tk.Entry(top)
    entry_100 = tk.Entry(top)
    entry_50 = tk.Entry(top)
    entry_20 = tk.Entry(top)
    entry_10 = tk.Entry(top)
    entry_5 = tk.Entry(top)

    def calculator():
        try:
            amount = int(amount_entry.get())

            if amount < 0:
                messagebox.showerror("Error", "Please enter a non-negative number.")
                return

            note_1000 = amount // 1000
            amount %= 1000

            note_500 = amount // 500
            amount %= 500

            note_100 = amount // 100
            amount %= 100

            note_50 = amount // 50
            amount %= 50

            note_20 = amount // 20
            amount %= 20

            note_10 = amount // 10
            amount %= 10

            note_5 = amount // 5

            entry_1000.delete(0, tk.END)
            entry_500.delete(0, tk.END)
            entry_100.delete(0, tk.END)
            entry_50.delete(0, tk.END)
            entry_20.delete(0, tk.END)
            entry_10.delete(0, tk.END)
            entry_5.delete(0, tk.END)

            entry_1000.insert(0, str(note_1000))
            entry_500.insert(0, str(note_500))
            entry_100.insert(0, str(note_100))
            entry_50.insert(0, str(note_50))
            entry_20.insert(0, str(note_20))
            entry_10.insert(0, str(note_10))
            entry_5.insert(0, str(note_5))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    calculate_button = tk.Button(
        top,
        text="Calculate",
        command=calculator,
        bg="brown",
        fg="white"
    )

    amount_label.place(x=230, y=30)
    amount_entry.place(x=210, y=60)
    calculate_button.place(x=240, y=95)

    result_label.place(x=120, y=145)

    label_1000.place(x=180, y=180)
    entry_1000.place(x=270, y=180)

    label_500.place(x=180, y=210)
    entry_500.place(x=270, y=210)

    label_100.place(x=180, y=240)
    entry_100.place(x=270, y=240)

    label_50.place(x=180, y=270)
    entry_50.place(x=270, y=270)

    label_20.place(x=180, y=300)
    entry_20.place(x=270, y=300)

    label_10.place(x=180, y=330)
    entry_10.place(x=270, y=330)

    label_5.place(x=180, y=360)
    entry_5.place(x=270, y=360)


if __name__ == "__main__":
    main()