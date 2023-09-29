from tkinter import messagebox
import customtkinter as ctk
import pyodbc

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("550x600+%d+%d" % (450,90))

var = ctk.StringVar()
fn = ctk.StringVar()
ln = ctk.StringVar()
dob = ctk.StringVar()
cor = ctk.StringVar()
gn = ctk.StringVar()
cor.set("Select a course")
pn = ctk.StringVar()
em = ctk.StringVar()

connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=BRENT;'
                            'Database= {Sample Project};'
                            'Trusted_Connection=Yes')

def register():
    if (fn.get() == ""):
        messagebox.showerror("Error","First Name cannot be left empty")
    elif (ln.get()==''):
        messagebox.showerror("Error","Last Name cannot be left empty")
    elif (dob.get()==''):
        messagebox.showerror("Error","Date of Birth cannot be left empty")
    elif (cor.get()== 'Select a course'):
        messagebox.showerror("Error","Select a course")
    elif (pn.get()==''):
        messagebox.showerror("Error","Phone Number cannot be left empty")
    elif (em.get()==''):
        messagebox.showerror("Error","Email cannot be left empty")
    else:
        connection.execute('''insert into Registration ([First Name],[Last Name],[Date of Birth],Gender,Course,[Phone Number],Email) values (?,?,?,?,?,?,?) ''',(fn.get(),ln.get(),dob.get(),gn.get(),cor.get(),pn.get(),em.get()))
        connection.commit()
        connection.close()
        messagebox.showinfo(title="Register", message = 'Registered')

        fn.set("")
        ln.set("")
        dob.set("")
        cor.set("Select a course")
        pn.set("")
        em.set("")

def clear():
    fn.set("")
    ln.set("")
    dob.set("")
    cor.set("Select a course")
    pn.set("")
    em.set("")
    gn.set("")

def logout():
    root.destroy()
    import newlogin


def redirect():
    root.destroy()
    import search

def on_closing():
    if messagebox.askyesno(title="Quit?", message="Do you want to quit?"):
        root.destroy()

frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=40, fill="both", expand= True)

label = ctk.CTkLabel(frame,text='Registration form',font=('Roboto',24))
label.pack(padx=10,pady=10)

label = ctk.CTkLabel(frame,text='First Name',font=('Roboto',14)).place(x=10,y=60)
entry = ctk.CTkEntry(frame, textvariable=fn, placeholder_text="First Name",width=210)
entry.pack(pady=12,padx=10)

label = ctk.CTkLabel(frame,text='Last Name',font=('Roboto',14)).place(x=10,y=115)
entry1 = ctk.CTkEntry(frame,textvariable=ln,placeholder_text="Last Name",width=210)
entry1.pack(pady=12,padx=10)

label = ctk.CTkLabel(frame,text='Date of Birth',font=('Roboto',14)).place(x=10,y=170)
entry2 = ctk.CTkEntry(frame,textvariable=dob, placeholder_text="Date of Birth",width=210)
entry2.pack(pady=12,padx=10)

label = ctk.CTkLabel(frame,text='Course of Study',font=('Roboto',14)).place(x=10,y=220)
option = ctk.CTkOptionMenu(frame,variable=cor,values= ("Physics","Algebra","Chemistry","History","Food Science","Politics"),width=210)
option.pack(pady=12,padx=10)

label = ctk.CTkLabel(frame,text='Phone Number',font=('Roboto',14)).place(x=10,y=270)
entry3 = ctk.CTkEntry(frame,textvariable=pn, placeholder_text="Phone Number",width=210)
entry3.pack(pady=12,padx=10)

label = ctk.CTkLabel(frame,text='Email Address',font=('Roboto',14)).place(x=10,y=325)
entry4 = ctk.CTkEntry(frame,textvariable=em, placeholder_text="Email",width=210)
entry4.pack(pady=12,padx=10)

label = ctk.CTkLabel(frame,text='Gender',font=('Roboto',14)).place(x=10,y=380)
radiobutton = ctk.CTkRadioButton(frame,text='Male',variable= gn,value='Male').place(x=140,y=380)
radiobutton = ctk.CTkRadioButton(frame,text='Female',variable= gn,value='Female').place(x=240,y=380)


button = ctk.CTkButton(frame,text='Register',command=register,width=80).place(x=45,y=420)
button = ctk.CTkButton(frame,text='Clear',command=clear,width=80).place(x=175,y=420)
button = ctk.CTkButton(frame,text='Logout',command=logout,width=80).place(x=305,y=420)

label = ctk.CTkLabel(frame,text='If you wish to search, delete or update an exisitng record, click the button below',font=('Roboto',12)).place(x=10,y=460)
button = ctk.CTkButton(frame,text='Redirect',command=redirect,width=80).place(x=175,y=490)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()