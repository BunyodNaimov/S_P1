from tkinter import Tk, Frame, Label, Entry, Button

window = Tk()
window.geometry('500x500')
frame = Frame(
    window,
    bg='yellow',
    padx=30,
    pady=30,
    highlightbackground="red",
    highlightthickness=5
)
frame.grid(column=0, row=0, padx=100, pady=100, )

username_label = Label(frame,
                       text="Username",
                       bg='yellow',
                       font=('Arial', 14, 'bold'),
                       )
username_label.grid(column=0, row=0, columnspan=2)

username_entry = Entry(frame, width=50)
username_entry.grid(column=0, row=1, columnspan=2)

gmail_label = Label(frame,
                    text="Gmail",
                    bg='yellow',
                    font=('Arial', 14, 'bold'),
                    )
gmail_label.grid(column=0, row=2, columnspan=2)

gmail_entry = Entry(frame, width=50)
gmail_entry.grid(column=0, row=3, columnspan=2)

age_label = Label(frame,
                  text="Age",
                  font=('Arial', 14, 'bold'),
                  )
age_label.grid(column=0, row=4)
age_entry = Entry(frame)
age_entry.grid(column=0, row=5)

phone_label = Label(frame,
                    text="Phone",
                    font=('Arial', 14, 'bold'),
                    )
phone_label.grid(column=1, row=4, columnspan=2)
phone_entry = Entry(frame)
phone_entry.grid(column=1, row=5, columnspan=2)

submit_btn = Button(frame, text="Submit")
submit_btn.grid(column=1, row=2)

for widjet in frame.winfo_children():
    widjet.grid_configure(padx=5, pady=5)


window.mainloop()