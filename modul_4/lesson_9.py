from tkinter import Tk, Spinbox

from customtkinter import CTkComboBox

window = Tk()
window.geometry("500x450")

combo = CTkComboBox(window,
                    values=["Choice", "Pyhon", "Java", "C++", "Golang"],
                    font=("Stencil", 15),
                    state="readonly",
                    width=200,
                    height=30,
                    fg_color="green",
                    bg_color="black",
                    justify="center",
                    )
combo.place(x=100, y=100)
combo.set("Python")

spinbox = Spinbox(window,
                  from_=0,
                  to=20,
                  font=("Helvetica", 15, "bold"),
                  bd=8,
                  bg="yellow",
                  fg="#06D607",
                  state="readonly",
                  readonlybackground="yellow",
                  justify="center",
                  highlightbackground='red',
                  highlightthickness=5,
                  highlightcolor='green')
spinbox.place(x=100, y=150, width=200, height=50)


window.mainloop()
