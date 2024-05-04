import tkinter as tk
from tkinter import ttk

root=tk.Tk()

root.geometry("500x500")
root.title("My GUI")


label = tk.Label(root, text="label", font=("Times New Roman",24))
label.pack(pady=20, padx=20)

textbox=tk.Text(root, height=4, font=("Arial",12))
textbox.pack(padx=10, pady=10)

button = tk.Button(root, text="Click!", font=("Comic Sans MS",10))
button.pack(padx=5, pady=5)


root.mainloop()
