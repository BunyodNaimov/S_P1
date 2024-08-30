from tkinter import Tk, Label, Button
from PIL import ImageTk, Image

window = Tk()
window.geometry('650x620')

photo = Image.open("python.png")
photo2 = Image.open("turtle.jpg")
photo3 = Image.open("tkinter.jpg")
photo4 = Image.open("pygame.jpg")
photo5 = Image.open("aiogram.jpg")

photos = [photo, photo2, photo3, photo4, photo5]
photos_list = []
for photo in photos:
    size = photo.resize((650, 620))
    p = ImageTk.PhotoImage(size)
    photos_list.append(p)

current_index_p = 0
photo_label = Label(window, image=photos_list[current_index_p])
photo_label.place(x=10, y=10)


def change_photo(photo):
    global current_index_p
    new_index = current_index_p + photo
    if 0 <= new_index < len(photos_list):
        current_index_p = new_index
        photo_label.config(image=photos_list[current_index_p])

    if current_index_p > 0:
        back_btn['state'] = 'normal'
    else:
        back_btn['state'] = 'disabled'

    if current_index_p < len(photos_list) - 1:
        next_btn['state'] = 'normal'
    else:
        next_btn['state'] = 'disabled'


def next_photo():
    change_photo(1)


def back_photo():
    change_photo(-1)


next_p = Image.open("next.png")
next_size = next_p.resize((140, 50))
next_image = ImageTk.PhotoImage(next_size)
next_btn = Button(window, image=next_image, command=next_photo, bd=8)
next_btn.place(x=450, y=530)


back_p = Image.open("back.png")
back_size = back_p.resize((140, 50))
back_image = ImageTk.PhotoImage(back_size)
back_btn = Button(window, image=back_image, command=back_photo, bd=8)
back_btn.place(x=60, y=530)


quit_p = Image.open("exit.png")
quit_size = quit_p.resize((140, 50))
quit_image = ImageTk.PhotoImage(quit_size)
quit_btn = Button(window, image=quit_image, command=window.quit)
quit_btn.place(x=255, y=530)

window.mainloop()
