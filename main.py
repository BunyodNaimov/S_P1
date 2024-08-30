from customtkinter import CTkEntry, CTkComboBox
from tkinter import Tk, Label, Button, Entry, PhotoImage, messagebox, Spinbox, Radiobutton, StringVar
from PIL import ImageTk, Image
import webbrowser

window = Tk()
window.config(bg='white')
window.geometry('650x620')
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
center_x = int(width / 2 - 650 / 2)
center_y = int(height / 2 - 620 / 2)
window.geometry(f"500x450+{center_x}+{center_y}")
window.title("Hafiza")
window.resizable(width=False, height=False)


def open_facebook():
    webbrowser.open_new("https://ru-ru.facebook.com/login/")


def open_x():
    webbrowser.open_new("https://x.com/")


def login():
    email = email_entry.get()
    password = password_entry.get()
    if email and password:
        messagebox.showinfo("Login Successful", "You have successful in")
    else:
        messagebox.showerror(title="Error",
                             message="Iltimos email address va parolni kiriting")


label = Label(window,
              text='Register Form',
              font=("Goudy Old Style", 30),
              bg='#BD2EDB',
              fg='white')
label.place(x=130, y=20)

email_entry = CTkEntry(window,
                       width=400,
                       height=45,
                       placeholder_text='Email addres',
                       font=("Goudy Old Style", 30))
email_entry.place(x=50, y=150)

password_entry = CTkEntry(window,
                          width=400,
                          height=45,
                          placeholder_text='Password',
                          font=("Goudy Old Style", 30))
password_entry.place(x=50, y=230)

btn = Button(window,
             text='Login',
             font=("Goudy Old Style", 30),
             bg='white',
             fg='#BD2EDB', command=login)

btn.place(x=50, y=310,
          width=400,
          height=55)

image = Image.open("facebook.png")
size = image.resize((150, 40))
facebook_photo = ImageTk.PhotoImage(size)
facebook_button = Button(window, image=facebook_photo, command=open_facebook)
facebook_button.place(x=50, y=80)

image = Image.open("download.jpg")
size = image.resize((150, 40))
x_photo = ImageTk.PhotoImage(size)
x_button = Button(window, image=x_photo, command=open_x)
x_button.place(x=250, y=80)

window.config(bg='#BD2EDB')
window.mainloop()
