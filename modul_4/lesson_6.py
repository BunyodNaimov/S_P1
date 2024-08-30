from tkinter import Tk, Label
from PIL import ImageTk, Image


window = Tk()
window.geometry('500x500')
window.title('PDP Junior')

logo = ImageTk.PhotoImage(file='PDP Junior.png')
window.iconphoto(False, logo)



window.mainloop()