from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.title("Letter Writing Application")
root.geometry("700x500")

current_file = ""


def open_file():
    global current_file
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file:
        current_file = file
        root.title(file)

        with open(file, "r") as f:
            text.delete("1.0", END)
            text.insert(END, f.read())


def save_file():
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file:
        with open(file, "w") as f:
            f.write(text.get("1.0", END))

        messagebox.showinfo("Saved", "Letter Saved Successfully")


text = Text(root, font=("Arial", 12))

btn_open = Button(root, text="Open Letter", command=open_file)
btn_save = Button(root, text="Save As", command=save_file)

btn_open.grid(row=0, column=0, padx=10, pady=10)
btn_save.grid(row=0, column=1, padx=10, pady=10)

text.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()