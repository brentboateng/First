import pyodbc
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("dark-blue")


connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=BRENT;'
                            'Database= {Sample Project};'
                            'Trusted_Connection=Yes')

root = ctk.CTk()
root.geometry("900x700+%d+%d" % (200,10))
frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=40, fill="both", expand= True)
root.title("Redirect")  
label = ctk.CTkLabel(frame,text = "Entry Records",font=('Roboto',20)).pack(padx=10,pady=10)


cursor = connection.cursor()
cursor.execute("Select * from Registration")

for row in cursor:

    label = ctk.CTkLabel(frame,text = row).pack(padx=10,pady=10)

connection.commit()


def login():
    root.destroy()
    import newlogin

def redirect():
    root.destroy()
    import search

def register():
    root.destroy()
    import newreg

button = ctk.CTkButton(frame,text='Login',command=login,width=80).place(x=230,y=520)
button = ctk.CTkButton(frame,text='Redirect',command=redirect,width=80).place(x=360,y=520)
button = ctk.CTkButton(frame,text='Register',command=register,width=80).place(x=480,y=520)

root.mainloop()
