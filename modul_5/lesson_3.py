from tkinter import Label, Tk, Entry, Button, Frame
from customtkinter import CTkEntry

window = Tk()
window.geometry('500x500')

frame = Frame(window)
frame.grid(column=0, row=0, padx=120, pady=200)

name_label = Label(frame, text="Username")
name_entry = CTkEntry(frame, )
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)


password_label = Label(frame, text="Email")
password_entry = CTkEntry(frame)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

btn = Button(frame, text="Submit")
btn.grid(row=2, column=1)

window.mainloop()
