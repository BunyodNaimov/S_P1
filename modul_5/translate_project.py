from tkinter import Tk, Label, Frame, Text, Button, END
from customtkinter import CTkComboBox

from PIL import ImageTk
from googletrans import Translator, LANGUAGES

window = Tk()
window.title("Google Tarjimon")
window.geometry("1070x400")
window.config(background="#626692")

logo = ImageTk.PhotoImage(file='google_translate_logo.png')
window.iconphoto(True, logo)

# label_photo = ImageTk.PhotoImage(file='png.png')
# image_label = Label(window, image=label_photo)
# image_label.place(x=482, y=130)


language_list = list(LANGUAGES.values())
language_keys = LANGUAGES.keys()

combobox = CTkComboBox(window,
                       values=language_list,
                       text_color="#387CFF",
                       font=("Roboto", 18), width=210)
combobox.place(x=125, y=20)
combobox.set("Select Language")

label = Label(window,
              text="Select Language",
              font=("segoe", 30, 'bold'),
              fg="#387CFF", width=18, bd=5)
label.place(x=20, y=55)

frame = Frame(window, bg="black", bd=5)
frame.place(x=20, y=120, width=440, height=210)

text_vidjet = Text(frame,
                   font=("roboto", 20),
                   bg="white", fg="#387CFF")
text_vidjet.place(x=0, y=0, width=430, height=200)

# o'ng tomoni
combobox2 = CTkComboBox(window,
                        values=language_list,
                        text_color="#387CFF",
                        font=("Roboto", 18), width=210)
combobox2.place(x=730, y=20)
combobox2.set("Select Language")

label2 = Label(window,
               text="Select Language",
               font=("segoe", 30, 'bold'),
               fg="#387CFF", width=18, bd=5)
label2.place(x=610, y=52)

frame2 = Frame(window, bg="black", bd=5)
frame2.place(x=610, y=118, width=440, height=210)

text_vidjet2 = Text(frame2,
                    font=("roboto", 20),
                    bg="white", fg="#387CFF")
text_vidjet2.place(x=0, y=0, width=430, height=200)


def translate_new():
    edit_text = text_vidjet.get(1.0, END)
    tarjimon = Translator()
    translated_text = tarjimon.translate(edit_text,
                                         src=combobox.get(),
                                         dest=combobox2.get())
    text_vidjet2.delete(1.0, END)
    text_vidjet2.insert(END, translated_text.text)


# translate button
button = Button(window,
                font=("roboto", 15),
                text="Translate",
                bg="#387CFF", fg="white",
                width=10, height=2,
                command=translate_new
                )
button.place(x=475, y=260)

window.mainloop()
