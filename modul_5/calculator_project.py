from tkinter import *
from customtkinter import CTkEntry

window = Tk()
window.geometry('485x560')

frame_output = Frame(window, width=480, height=50)
frame_output.pack(side='top')

text = StringVar()
btn_text = ""


def click_button(item):
    global btn_text
    btn_text += str(item)
    text.set(btn_text)


def clear_button():
    global btn_text
    btn_text = ""
    text.set("")


def button_equal():
    global btn_text
    result = str(eval(btn_text))
    text.set(result)
    btn_text = ""


entry = CTkEntry(
    frame_output, textvariable=text, width=480, height=80, fg_color="#000000", justify='right',
    text_color='white', font=('Arial', 30, 'bold'))
entry.grid(column=0, row=0)

frame_button = Frame(window, width=480, height=480, bg='grey')
frame_button.pack()

clear_btn = Button(
    frame_button, width=13, height=2, text="C", font=("Arial", 20, "bold"), bg='#AB3939', bd=5, command=clear_button
)
clear_btn.grid(column=0, row=0, columnspan=2, padx=1, pady=1)

divide_btn = Button(
    frame_button, text="/", width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#666666",
    command=lambda: click_button("/"))

divide_btn.grid(column=2, row=0, padx=1, pady=1)

multiple_btn = Button(
    frame_button, text="*", width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#666666",
    command=lambda: click_button("*"))
multiple_btn.grid(row=0, column=3, padx=1, pady=1)

btn_7 = Button(
    frame_button, text=7, width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#4D4D4D",
    command=lambda: click_button("7"))
btn_7.grid(column=0, row=1, padx=1, pady=1)

btn_8 = Button(
    frame_button, text=8, width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#4D4D4D",
    command=lambda: click_button("8"))
btn_8.grid(column=1, row=1)

btn_9 = Button(
    frame_button, text=9, width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#4D4D4D",
    command=lambda: click_button("9"))
btn_9.grid(column=2, row=1)

minus_btn = Button(
    frame_button, text='-', width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#666666",
    command=lambda: click_button("-"))
minus_btn.grid(column=3, row=1)

btn_4 = Button(
    frame_button, text=4, width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#4D4D4D",
    command=lambda: click_button("4"))
btn_4.grid(column=0, row=2)

btn_5 = Button(
    frame_button, text="5", width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#4D4D4D",
    command=lambda: click_button("5"))
btn_5.grid(column=1, row=2)

btn_6 = Button(
    frame_button, text=6, width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#4D4D4D",
    command=lambda: click_button("6"))
btn_6.grid(column=2, row=2)

plus_btn = Button(
    frame_button, text='+', width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#666666",
    command=lambda: click_button("+"))
plus_btn.grid(column=3, row=2)

btn_1 = Button(
    frame_button, text=1, width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#4D4D4D",
    command=lambda: click_button("1"))
btn_1.grid(column=0, row=3)

btn_2 = Button(
    frame_button, text=2, width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#4D4D4D",
    command=lambda: click_button("2"))
btn_2.grid(column=1, row=3)

btn_3 = Button(
    frame_button, text=3, width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#4D4D4D",
    command=lambda: click_button("3"))
btn_3.grid(column=2, row=3)

btn_equal = Button(
    frame_button, text="=", width=6, height=5, bd=5, font=('Arial', 20, "bold"), bg="#004566",
    command=button_equal)
btn_equal.grid(column=3, row=3, rowspan=2)

btn_0 = Button(
    frame_button, text=0, width=13, height=2, bd=5, font=('Arial', 20, "bold"), bg="#4D4D4D",
    command=lambda: click_button("0"))
btn_0.grid(column=0, row=4, columnspan=2)

btn_dot = Button(
    frame_button, text=".", width=6, height=2, bd=5, font=('Arial', 20, "bold"), bg="#4D4D4D",
    command=lambda: click_button("."))
btn_dot.grid(column=2, row=4)

window.mainloop()
