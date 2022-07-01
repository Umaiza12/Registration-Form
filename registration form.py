import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import*

root= Tk()
root.title("Registration Form")
root.geometry("500x400")
root.configure(bg = "#eeeeee")

a = Label(root,text="Registration Form", fg="black", bg="#eeeeee", font = ("arial", 20))
a.place(x = 20, y = 10)


b = Label(root,text="Full Name", fg="black", bg="#eeeeee", font = ("arial", 11),  anchor = "w")
b.place(x=20, y = 75)

c= Label(root,text="Email", fg="black", bg="#eeeeee", font = ("arial", 11), anchor = "w")
c.place(x=20, y = 115)

d = Label(root,text="Gender", fg="black", bg="#eeeeee", font = ("arial", 11),  anchor = "w")
d.place(x=20, y = 155)

e = Label(root,text="Country", fg="black", bg="#eeeeee", font = ("arial", 11),  anchor ="w")
e.place(x=20, y = 195)

f = Label(root,text="Programming", fg="black", bg="#eeeeee", font = ("arial", 11), anchor = "w")
f.place(x = 20, y = 235)

name = tk.StringVar()
a1=Entry(root, bg="white", width = 40, textvariable=name)
a1.place(x=150, y = 75)

email = tk.StringVar()
a2=Entry(root, bg="white", width = 40, textvariable=email)
a2.place(x = 150, y = 115)





v=IntVar()
a4 = tk.Radiobutton(root,text="Male",variable=v,value=1)
a4.place(x=150, y= 155)
a5 = tk.Radiobutton(root,text="Female",variable=v,value=2)
a5.place(x= 250, y = 155)

def submit():
    print("Form Successfully Submitted")
    a1 = name.get()
    a2 = email.get()
    a4 = v.get()
    a5 = v.get()
    c2_choosen = c2.get()
    check1 = var1.get()
    check2 = var2.get()

    if a1 == "":
        messagebox.showerror("Error", "Name has not been entered")
    elif a2 == "":
        messagebox.showerror("Error", "Email has not been entered")
    elif a4 == "" or a5 == "":
        messagebox.showerror("Error", "Gender has not been selected")
    elif c2_choosen == "Select your country":
        messagebox.showerror("Error", "country has not been selected")
    elif check1 == False and check2 == False:
        messagebox.showerror("Error", "No programming language has been selected")
    else:
        b4 = Label(root, text = "Registration Successful", font = (13), fg = "green")
        b4.place(x = 180, y = 350)
        messagebox.showinfo("Registration", "Registration is succesful")

    
        
b1=Button(root, text="Submit",bg="red",fg="white",command=submit, width = "8", font = (14))
b1.place(x = 25, y = 275)

c2=tk.StringVar()
c2_choosen=ttk.Combobox(root,width=40,textvariable=c2)
c2_choosen['value']=["Select your country","Pakistan", "America", "Germany", "India"]
c2_choosen.place(x=150, y = 195)
c2_choosen.current(0)

var1=IntVar()
check1=Checkbutton(root,text="Python",variable=var1)
check1.select()
check1.place(x=150, y = 235)

var2=IntVar()
check2=Checkbutton(root,text="Java",variable=var2)
check2.deselect()
check2.place(x=250, y = 235)


root.mainloop()
