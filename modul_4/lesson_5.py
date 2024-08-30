from tkinter import Tk, Label, Button

window = Tk()
window.geometry('500x500')

btn1 = Button(window,
              text='Sign in',
              bg="blue",
              fg="green",
              activebackground="red",
              activeforeground="yellow",
              font=('Verdana', 25),
              )
btn1.place(x=100, y=100)

btn2 = Button(window,
              text="LOGIN",
              bg="red",
              fg="white",
              activebackground="#FFDAFF",
              activeforeground="#B30B00",
              font=('Stencil', 20, 'bold'),
              # bd=10,
              state="normal",
              width=15,
              height=4,
              cursor="X_cursor",
              command=window.quit
              )

btn2.place(x=100, y=250)






window.mainloop()
