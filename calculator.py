import tkinter as tk
a=tk.Tk()
def cal(w):
    if w=="C":
        d.configure(text="")
    elif w=="=":
        try:
            z=eval(d["text"])
            d.configure(text=z)
        except:
            d.configure(text="Syntax error")
    else:
        x=str(d["text"])
        x=x+w
        d.configure(text=x)
no=[["7","8","9","/"],["4","5","6","*"],["1","2","3","-"],["0",".","=","+"]]
d=tk.Label()
d.grid(row=1,column=4)
s=tk.Button(text="C",command=lambda:cal("C"))
s.grid(row=6,column=3,columnspan=4)
def write(t,r,c):
    b=tk.Button(text=t,command=lambda:cal(t))
    b.grid(row=r,column=c)
for i in range(len(no)):
    for j in range(len(no[i])):
        write(no[i][j],i+2,j)
#b=tk.Label()
##c=tk.Button(text=7)
##d=tk.Button(text=8)
##e=tk.Button(text=9)
##f=tk.Button(text="/")
##g=tk.Button(text=4)
##h=tk.Button(text=5)
##i=tk.Button(text=6)
##j=tk.Button(text="*")
##k=tk.Button(text=1)
##l=tk.Button(text=2)
##m=tk.Button(text=3)
##n=tk.Button(text="-")
##o=tk.Button(text=0)
##p=tk.Button(text=".")
##q=tk.Button(text="=")
##r=tk.Button(text="+")
##s=tk.Button(text="C")
##b.grid(row=1,column=3)
##c.grid(row=2,column=1)
##d.grid(row=2,column=2)
##e.grid(row=2,column=3)
##f.grid(row=2,column=4)
##g.grid(row=3,column=1)
##h.grid(row=3,column=2)
##i.grid(row=3,column=3)
##j.grid(row=3,column=4)
##k.grid(row=4,column=1)
##l.grid(row=4,column=2)
##m.grid(row=4,column=3)
##n.grid(row=4,column=4)
##o.grid(row=5,column=1)
##p.grid(row=5,column=2)
##q.grid(row=5,column=3)
##r.grid(row=5,column=4)
##s.grid(row=6,column=3,columnspan=4)
a.mainloop()
