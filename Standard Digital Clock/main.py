import time
import tkinter as tk

root = tk.Tk()
root.title("Standard Digital Clock")

def currentTime():
    string = time.strftime('%I:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, currentTime)

label = tk.Label(
    root,
    font= ('calibri', 60, 'bold'),
    background='yellow',
    foreground='black'
)

label.pack(anchor='center')

currentTime()
root.mainloop()