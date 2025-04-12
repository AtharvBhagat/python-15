from tkinter import *

root=Tk()
root.title("My first tkinter window")
root.geometry("1000x800")
root.config(bg="dark grey")
headding=Label(root,text="student introduction",bg="green",fg="white",font=("Arial",20))
name=Label(root,text="enter your name",bg="grey",fg="black",font=("Arial",20))
entry=Entry(root)
gender=Label(root,text="enter your gender ",bg="grey",fg="black",font=("Arial",20))
g_entry=Entry(root)
age=Label(root,text="enter your age ",bg="grey",fg="black",font=("Arial",20))
a_entry=Entry(root)

headding.pack()
name.pack()
entry.pack()
gender.pack()
g_entry.pack()
age.pack()
a_entry.pack()

root.mainloop()