from tkinter import Tk, Button
from customtkinter import CTkEntry

window = Tk()
window.geometry('500x500')
window.config(background='blue')

entry = CTkEntry(window,
                 font=("Calibri", 30, 'bold'),
                 corner_radius=20,
                 text_color='red',
                 fg_color='pink',
                 width=300,
                 height=50,
                 justify='center',
                 placeholder_text="Username",
                 placeholder_text_color="green",
                 border_width=5,
                 border_color='red')
entry.place(x=40, y=40)

btn = Button(window, text="Chiqish", command=window.quit)
btn.place(x=45, y=100)

window.mainloop()
