from tkinter import *
from customtkinter import *

window = Tk()
window.geometry('500x500')

t1=CTkLabel(window,text="Quduq Qog'oz Qaychi",text_color="blue",font=("Arial",30,"bold"))
t1.place(x=100,y=0)

t2=CTkLabel(window,text="Player VS Computer",text_color="black",font=("Arial",20,"bold"))
t2.place(x=150,y=100)

e=CTkEntry(window,width=500,height=50)
e.place(x=0,y=150)

b1=CTkButton(window,text="Quduq",font=("Arial",20),bg_color="black",fg_color="black")
b1.place(x=20,y=250)

b2=CTkButton(window,text="Qog'oz",font=("Arial",20),bg_color="black",fg_color="black")
b2.place(x=180,y=250)

b3=CTkButton(window,text="Qaychi",font=("Arial",20),bg_color="black",fg_color="black")
b3.place(x=350,y=250)

b4=CTkButton(window,text="Qaytadan o'ynash",font=("Arial",30),bg_color="black",fg_color="black",text_color="red")
b4.place(x=130,y=350)
window.mainloop()
