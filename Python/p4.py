
import tkinter as tk
from tkinter import messagebox

Window=tk.Tk()
Window.title("My app")
Window.geometry("400x200")

def click():
    name = entry.get()
    if name:
        messagebox.showinfo("Good","Valider")
    else:
        messagebox.showwarning("Bonjour","Attention veiller entre un nom")
def click1():
    messagebox.showwarning("Error","Delete")

label=tk.Label(Window,text="Entre votre nom")
entry=tk.Entry(Window,width=30)
button=tk.Button(Window,text="valider",command=click)
button1 = tk.Button(Window, text="refuser",command=click1)
result=tk.Label(Window,text=" ")

label.pack(pady=10)
button.place_configure(x=10)
entry.pack(pady=5)
button.pack(pady=10) 
button.pack(padx=10)
button1.pack(pady=20)
result.pack(pady=10)

Window.mainloop()
