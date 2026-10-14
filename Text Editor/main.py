import tkinter as tk
from tkinter import filedialog,messagebox

root = tk.Tk()
root.title("Text Editor")

text = tk.Text(
    root,
    wrap= tk.WORD,
    font=("Helvetica", 18)
)

text.pack(expand=True, fill=tk.BOTH)

def newfile():
    text.delete(1.0, tk.END)

def openfile():
    filepath = filedialog.askopenfilename(
        filetypes=[("file text", "*.txt")]
    )

    if filepath:
        with open(filepath,"r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def savefile():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("file", "*.txt")]
    )  

    if filepath:
     with open(filepath, "w") as file:
        file.write(text.get(1.0, tk.END))

    messagebox.showinfo("Saved", "File saved successfully!")

menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)

menu.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="open", command=openfile)
filemenu.add_command(label="save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="exit", command=root.quit)

root.mainloop()