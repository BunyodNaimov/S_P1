from tkinter import Tk, Label, Entry, Button

window = Tk()
window.geometry("500x450")
window.title("Python Project")
window.configure(bg='white')

label = Label(window, text="Shohruh")
label.place(x=100, y=70)

entry = Entry(window)
entry.place(x=160, y=70)

btn = Button(window, text="Click me", )
btn.place(x=40, y=40)

window.mainloop()


