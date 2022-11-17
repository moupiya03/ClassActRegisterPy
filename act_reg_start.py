from tkinter import *
import os

root=Tk()
root.geometry("1200x1200")
root.title("ACTIVITY REGISTER")
root.configure(bg="black")


def call1():
    fname="dark_theme.py"
    os.system(fname)
    os.system("notepad"+fname)

def call2():
    fname="light_theme.py"
    os.system(fname)
    os.system("notepad"+fname)

ftop=Frame(root,borderwidth=5,relief=SUNKEN,bg="maroon")
ftop.pack(side=TOP,fill="x",padx=5,pady=5)

ltop=Label(ftop,text="ACTIVITY REGISTER",font="Helvetica 30 bold ",bg="maroon",fg="white")
ltop.pack(padx=5,pady=5)

f1=Frame(root,bg="black",relief=SUNKEN)
f1.pack(side=TOP,padx=10,pady=10,anchor="nw")

l1=Label(f1,text="ABOUT PROJECT :-",font="Helvetica 20 bold underline ",bg="black",fg="white")
l1.pack(padx=10,pady=10,anchor="nw")

f2=Frame(root,bg="black",relief=SUNKEN)
f2.pack(side=TOP,padx=10,pady=10,anchor="center")

l2=Label(f2,text="This is a digital Activity Register which is created to keep record of every class in a gracefull manner",font="Helvetica 18 ",bg="black",fg="white")
l2.pack(padx=10,pady=10,anchor="center")

fbottom=Frame(root,borderwidth=5,relief=SUNKEN,bg="maroon")
fbottom.pack(side=BOTTOM,fill="x",padx=2,pady=2)

lbottom=Label(fbottom,text="Created by - Moupiya  ",font="Helvetica 18 bold",bg="maroon",fg="white")
lbottom.pack(padx=2,pady=2)

fquit=Frame(root,bg="black",relief=SUNKEN,borderwidth=5)
fquit.pack(side=BOTTOM,padx=10,pady=10,anchor="center")

bquit=Button(fquit,text="Quit",font="Helvetica 16 bold underline",bg="black",fg="red",command=root.destroy)
bquit.pack(padx=10,pady=10,anchor="center")

f3=Frame(root,bg="black",relief=SUNKEN)
f3.pack(side=BOTTOM,padx=10,pady=10,anchor="center")

l3=Label(f3,text="To Exit Click Below",font="Helvetica 16 bold underline",bg="black",fg="white")
l3.pack(padx=10,pady=10,anchor="center")

f4=Frame(root,bg="black",relief=SUNKEN)
f4.pack(side=TOP,padx=10,pady=10,anchor="center")

l4=Label(f4,text="Choose your Theme Below",font="Helvetica 16 bold underline",bg="black",fg="white")
l4.pack(padx=10,pady=10,anchor="center")

fdark=Frame(root,bg="black",borderwidth=5,relief=SUNKEN)
fdark.pack(side=TOP,padx=5,pady=5,anchor="center")

bdark=Button(fdark,text="Dark",font="Helvetica 16 bold",bg="black",fg="white",command=call1)
bdark.pack(padx=5,pady=5,anchor="center")

flight=Frame(root,bg="black",borderwidth=5,relief=SUNKEN)
flight.pack(side=TOP,padx=5,pady=5,anchor="center")

blight=Button(flight,text="Light",font="Helvetica 16 bold",bg="black",fg="white",command=call2)
blight.pack(padx=5,pady=5,anchor="center")


root.mainloop()
