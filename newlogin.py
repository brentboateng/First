from tkinter import messagebox
import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("400x400+%d+%d" % (500,100))
root.title("Modern Interface")

un = ctk.StringVar()
password = ctk.StringVar()

def validate():
        if (un.get()==''):
            messagebox.showerror("Error","Username cannot be left empty")
        elif (password.get()==''):
            messagebox.showerror("Error","Password cannot be left empty")
        elif(un.get()== 'admin' and password.get()== '1234'):
            messagebox.showinfo("Validated","Welcome "+un.get())
            root.destroy()
            import newreg
        elif(un.get()!= 'admin' or password.get()!= '1234'):
             messagebox.showinfo("Invalid","Invalid username or password")


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand= True)

label = ctk.CTkLabel(master=frame, text= "Login System", font=('Roboto',24))
label.pack(pady=12,padx=10)

entry = ctk.CTkEntry(frame,textvariable=un, placeholder_text="Username")
entry.pack(pady=12,padx=10)

entry1 = ctk.CTkEntry(frame,textvariable=password, placeholder_text="Password", show="*")
entry1.pack(pady=12,padx=10)

button = ctk.CTkButton(frame, text="Login",command=validate)
button.pack(pady=12,padx=10)

checkbox = ctk.CTkCheckBox(frame,text="Remember Me")
checkbox.pack(pady=12,padx=10)
root.mainloop()



