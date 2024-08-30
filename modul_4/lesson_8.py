from tkinter import Tk, Label, messagebox, Button
from customtkinter import CTkEntry

window = Tk()
window.geometry('450x450')
window.config(background='black')


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        messagebox.showinfo("Login Successful", "You have successfully logged in.")
    else:
        messagebox.showerror(title="Error 🙈",
                             message="Iltimos Login va Parolni kiriting!")


sign_in_label = Label(window,
                      text='SIGN IN',
                      fg='#06D607',
                      bg='black',
                      font=('Arial', 20, 'bold'))
sign_in_label.place(x=160, y=100)

username_label = Label(window,
                       text='Username',
                       fg='#06D607',
                       bg='black',
                       font=('Arial', 15, 'bold'))
username_label.place(x=60, y=150)

password_label = Label(window,
                       text="Password",
                       fg='#06D607',
                       bg='black',
                       font=('Arial', 15, 'bold'))
password_label.place(x=60, y=200)

username_entry = CTkEntry(window,
                          placeholder_text="Username kiriting",
                          placeholder_text_color='#4C4C4C')
username_entry.place(x=170, y=155)

password_entry = CTkEntry(window,
                          show="*",
                          placeholder_text="Password kiriting",
                          placeholder_text_color='#4C4C4C')
password_entry.place(x=170, y=205)

forgot_password_label = Label(window,
                              text="Forgot Password",
                              bg='black',
                              fg='white')
forgot_password_label.place(x=60, y=250)

signup_label = Label(window,
                     text="Sign Up",
                     bg='black',
                     fg='#06D607',
                     font=('Arial', 15, 'bold'))
signup_label.place(x=250, y=250)

login_btn = Button(window, text="Login", bg='#06D607', fg='black', bd=5, command=login)
login_btn.place(x=100, y=300, width=200, height=40)

window.mainloop()
