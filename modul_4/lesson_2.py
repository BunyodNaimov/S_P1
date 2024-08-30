from tkinter import Tk, Label

window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
center_x = int(width / 2 - 500 / 2)
center_y = int(height / 2 - 450 / 2)
window.geometry(f"500x450+{center_x}+{center_y}")
window.resizable(width=False, height=False)

label = Label(window,
              text="Python",
              font=("Gabriola", 70, "bold"))
# label.place(x=80, y=50)
discount_label = Label(window,
                       text="12$",
                       font=("Gabriola", 30, "overstrike"),
                       fg="red",
                       bg="black")
discount_label.place(x=100, y=55)

price_label = Label(window,
                    text="10$",
                    font=("Gabriola", 40))

price_label.place(x=140, y=50)

window.mainloop()
