import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
user={"craby168","snaily168","lisalisa168","bb523168"}
passw={"craby22602584","0","0","0"}
def login():
   print("Welcome")

root=ctk.CTk()
root.geometry("500*350")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=12, padx=10, expand=True, fill="both")

label=ctk.CTkLabel(master=frame, text="Login System", font=("Arial",24))
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username", placeholder_text_color="grey")
entry1.pack(pady=12, padx=10)

entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", placeholder_text_color="grey", show="*")
entry2.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox=ctk.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12, padx=10)

def click(option):
   print("You're a :", option)
combobox=ctk.CTkComboBox(master=frame, values=["Admin","Teacher","Student", "Parent"], command=click)
combobox.pack(pady=12, padx=10)

root.mainloop()




