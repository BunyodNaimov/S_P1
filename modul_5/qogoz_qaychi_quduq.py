import random
from tkinter import Label, Tk, Entry, Button, StringVar

window = Tk()
window.geometry('500x500')
computer_value = ["Quduq", "Qog'oz", "Qaychi"]

entry_text = StringVar()


def is_quduq():
    comp_value = random.choice(computer_value)
    if comp_value == "Quduq":
        result = "Bir Xil!"
    elif comp_value == "Qog'oz":
        result = "Computer g'olib bo'ldi!"
    else:
        result = "Siz g'olib bo'ldingiz"

    comp_label.config(text=comp_value)
    player_label.config(text="Quduq")
    entry_text.set(result)


text_label = Label(window, text="Quduq Qog'oz Qaychi", font=("Arial", 30, 'bold'), fg='blue')
text_label.place(x=50, y=10)

player_label = Label(window, text="Player", font=("Arial", 20, 'bold'))
player_label.place(x=90, y=80, )

vs_label = Label(window, text="Vs", font=("Arial", 20, 'bold'))
vs_label.place(x=200, y=80)

comp_label = Label(window, text="Computer", font=("Arial", 20, 'bold'))
comp_label.place(x=250, y=80)

text_entry = Entry(window, textvariable=entry_text, font=("Arial", 15, 'bold'))
text_entry.place(x=80, y=120, height=30, width=330)

quduq_btn = Button(window, text="Quduq", font=("Arial", 20, 'bold'), command=is_quduq)
quduq_btn.place(x=50, y=180)

qogoz_btn = Button(window, text="Qog'oz", font=("Arial", 20, 'bold'))
qogoz_btn.place(x=190, y=180)

qaychi_btn = Button(window, text="Qaychi", font=("Arial", 20, 'bold'))
qaychi_btn.place(x=330, y=180)

reload_btn = Button(
    window, text="Qaytadan o'ynash", font=("Arial", 20, 'bold'), bd=5, bg='black', fg='red')
reload_btn.place(x=80, y=280)

window.mainloop()
