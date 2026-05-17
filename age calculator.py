import tkinter as tk
from tkinter import messagebox
a = tk.Tk()
a.geometry('1500x300')
a.resizable(False, False)
a.title("Age Calculator")
a.config(bg="burlywood1")
def reset():
    d.set("")
    f.set("")
    h.set("")
    k.set("")
    m.set("")
    o.set("")
    r.set("")
menubar = tk.Menu(a)
a.config(menu=menubar)
menuop = tk.Menu(menubar)
menubar.add_cascade(label="Options", menu=menuop)
menuop.add_command(label="Reset", command=reset)
menuop.add_command(label="Exit", command=a.destroy)
def calculate_age():
 t = int(o.get())
 u = int(h.get())  
 v = int(m.get())  
 w = int(f.get())  
 x = int(k.get())  
 y = int(d.get())  
 z = str(r.get())
 if(v<w)or(v==w) and(x<y):
     year=t-u-1
 else:
     year=t-u
 if (v<w) or (v==w) and (x<y):
    month=v-w+12
 else:
     month=v-w
 if x < y:
    day = x - y + 30  
    month=month-1
 else:
    day = x - y
 if z == "leap":
      if (v == 2 and w == 2):
        day = 29 - y + x  
      elif v == 2 and w == 1:
        month = 12
        year=year-1
 else:
    month=month-1
##messagebox.showinfo("Age Calculated", f"You are currently {years}years {months}months and {days}days old")
t = tk.StringVar()
u = tk.StringVar()
v = tk.StringVar()
w = tk.StringVar()
x = tk.StringVar()
y = tk.StringVar()
z = tk.StringVar()
b = tk.Label(text="Date of Birth", font=("Algerian", 24), bg="burlywood1")
c = tk.Label(text="Date", font=("Algerian", 24), bg="burlywood1")
d = tk.Entry(textvariable=y)
e = tk.Label(text="Month(no)", font=("Algerian", 24), bg="burlywood1")
f = tk.Entry(textvariable=w)
g = tk.Label(text="Year", font=("Algerian", 24), bg="burlywood1")
h = tk.Entry(textvariable=u)
i = tk.Label(text="Current Date", font=("Algerian", 24), bg="burlywood1")
j = tk.Label(text="Date", font=("Algerian", 24), bg="burlywood1")
k = tk.Entry(textvariable=x)
l = tk.Label(text="Month(no)", font=("Algerian", 24), bg="burlywood1")
m = tk.Entry(textvariable=v)
n = tk.Label(text="Year", font=("Algerian", 24), bg="burlywood1")
o = tk.Entry(textvariable=t)
p = tk.Button(text="Submit", font=("Algerian", 24), bg="Pink", command=calculate_age)
q = tk.Label(text="Previous Month(name)", font=("Algerian", 24), bg="burlywood1")
r = tk.Entry(textvariable=z)
note = tk.Label(text="Note: If previous month is a leap year, then type leap", font=("Algerian", 15), bg="burlywood1")
b.grid(row=1, column=2)
c.grid(row=2, column=1)
d.grid(row=2, column=2)
e.grid(row=3, column=1)
f.grid(row=3, column=2)
g.grid(row=4, column=1)
h.grid(row=4, column=2)
i.grid(row=1, column=5)
j.grid(row=2, column=4)
k.grid(row=2, column=5)
l.grid(row=3, column=4)
m.grid(row=3, column=5)
n.grid(row=4, column=4)
o.grid(row=4, column=5)
q.grid(row=7, column=3)
r.grid(row=7, column=4)
p.grid(row=9, column=3)
note.grid(row=11, column=3)
a.mainloop()
