from tkinter import messagebox
import customtkinter as ctk
import pyodbc
import pandas as pd

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
pn = ctk.StringVar()
em = ctk.StringVar()
ind = ctk.IntVar()
id = ctk.StringVar()





connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=BRENT;'
                            'Database= {Sample Project};'
                            'Trusted_Connection=Yes')

def show():
        
    cursor = connection.cursor()
    cursor.execute("Select * from Registration")
    connection.commit()
    data = pd.read_sql("Select [First Name],[Last Name],Course,Email,Gender,[Phone Number],[Date of Birth] from Registration where ID = "+ id.get() ,con=connection)
    fn.set(data['First Name'].iloc[ind.get()])
    ln.set(data['Last Name'].iloc[ind.get()])
    cor.set(data['Course'].iloc[ind.get()])
    em.set(data['Email'].iloc[ind.get()])
    gn.set(data['Gender'].iloc[ind.get()])
    pn.set(data['Phone Number'].iloc[ind.get()])
    dob.set(data['Date of Birth'].iloc[ind.get()])
        

def update():
    cursor = connection.cursor()
    cursor.execute("Update Registration set [First Name] = ? where ID = ? ",(fn.get(),id.get()))
    cursor.execute("Update Registration set [Last Name] = ? where ID = ? ",(ln.get(),id.get()))
    cursor.execute("Update Registration set Course = ? where ID = ? ",(cor.get(),id.get()))
    cursor.execute("Update Registration set Email = ? where ID = ? ",(em.get(),id.get()))
    cursor.execute("Update Registration set Gender = ? where ID = ? ",(gn.get(),id.get()))
    cursor.execute("Update Registration set [Phone Number] = ? where ID = ? ",(pn.get(),id.get()))
    cursor.execute("Update Registration set [Date of Birth] = ? where ID = ? ",(dob.get(),id.get()))

    connection.commit()
    messagebox.showinfo(title="Updated",message= fn.get())

def search():
    root.destroy()
    import newsearch

def clear():
    fn.set("")
    ln.set("")
    dob.set("")
    cor.set("")
    pn.set("")
    em.set("")
    gn.set("")
    

def on_closing():
    if messagebox.askyesno(title="Quit?", message="Do you want to quit?"):
        root.destroy()

frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=40, fill="both", expand= True)

label = ctk.CTkLabel(frame,text='Update Entry',font=('Roboto',24))
label.pack(padx=10,pady=10)

label = ctk.CTkLabel(frame,text='First Name',font=('Roboto',14)).place(x=10,y=60)
entry = ctk.CTkEntry(frame, textvariable=fn,width=210)
entry.pack(pady=12,padx=10)

label = ctk.CTkLabel(frame,text='Last Name',font=('Roboto',14)).place(x=10,y=115)
entry1 = ctk.CTkEntry(frame,textvariable=ln,width=210)
entry1.pack(pady=12,padx=10)

label = ctk.CTkLabel(frame,text='Date of Birth',font=('Roboto',14)).place(x=10,y=170)
entry2 = ctk.CTkEntry(frame,textvariable=dob,width=210)
entry2.pack(pady=12,padx=10)

label = ctk.CTkLabel(frame,text='Course of Study',font=('Roboto',14)).place(x=10,y=220)
entry5 = ctk.CTkEntry(frame,textvariable=cor,width=210)
entry5.pack(pady=12,padx=10)

label = ctk.CTkLabel(frame,text='Phone Number',font=('Roboto',14)).place(x=10,y=270)
entry3 = ctk.CTkEntry(frame,textvariable=pn,width=210)
entry3.pack(pady=12,padx=10)

label = ctk.CTkLabel(frame,text='Email Address',font=('Roboto',14)).place(x=10,y=325)
entry4 = ctk.CTkEntry(frame,textvariable=em,width=210)
entry4.pack(pady=12,padx=10)

label = ctk.CTkLabel(frame,text='Gender',font=('Roboto',14)).place(x=10,y=380)
entry6 = ctk.CTkEntry(frame,textvariable=gn,width=210)
entry6.pack(pady=12,padx=10)


label = ctk.CTkLabel(frame,text='Enter the ID you wish to change in the entry',font=('Roboto',14)).place(x=100,y=410)
label = ctk.CTkLabel(frame,text='below and click the update button',font=('Roboto',14)).place(x=125,y=432)
entry = ctk.CTkEntry(frame,textvariable=id,width=150).place(x=160,y=460)
button = ctk.CTkButton(frame,text='Show',command=show,width=80).place(x=50,y=500)
button = ctk.CTkButton(frame,text='Clear',command=clear,width=80).place(x=200,y=500)
button = ctk.CTkButton(frame,text='Save',command=update,width=80).place(x=350,y=500)


#root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()