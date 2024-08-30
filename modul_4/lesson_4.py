# # from tkinter import Tk
# # from tkcalendar import Calendar
# # from customtkinter import CTkButton, CTkLabel
# #
# # window = Tk()
# # window.geometry('450x400')
# # window.title('Kalendar loyihasi')
# #
# #
# # def show_selected_date():
# #     selected_date = cal.get_date()
# #
# #     lb = CTkLabel(window, text=f"Tanlangan sana: {selected_date}", text_color='red')
# #     lb.place(x=150, y=350)
# #
# #
# # cal = Calendar(window, selectmode='day', year=2024, month=7, day=22)
# # cal.place(x=0, y=0, width=450, height=300)
# #
# # btn = CTkButton(window, text=f"Sanani ko'rsatish ", command=show_selected_date)
# # btn.place(x=310, y=300)
# #
# # window.mainloop()
#
# # from tkinter import Tk, Label
# # import time
# #
# # window = Tk()
# # window.geometry('450x200')
# # window.title('Soat loyihasi')
# #
# #
# # def update_time():
# #     current_time = time.strftime("%H:%M:%S")
# #     soat_label.config(text=current_time)
# #     soat_label.after(1000, update_time)
# #
# #
# # soat_label = Label(window, font=("Helvetica", 60), bg="black", fg="white")
# # soat_label.place(x=70, y=40)
# # update_time()
# #
# # window.mainloop()
#
# from tkinter import Tk, Label, Entry, Button
#
# window = Tk()
# window.geometry('500x450')
#
#
# def info():
#     num1 = int(entry.get())
#     num2 = int(entry1.get())
#
#     label3 = Label(window, text=f"{num1} + {num2} = {num1 + num2}")
#     label3.place(x=50, y=100)
#
#
# label1 = Label(window, text="1-chi sonni kiriting:", font=('Arial', 15))
# label1.place(x=50, y=20)
# entry = Entry(window, )
# entry.place(x=220, y=30)
#
# label2 = Label(window, text="2-chi sonni kiriting:", font=('Arial', 15))
# label2.place(x=50, y=60)
# entry1 = Entry(window, )
# entry1.place(x=220, y=70)
# btn = Button(window, text="Clik me", command=info)
# btn.place(x=220, y=100)
#
# window.mainloop()

# from tkinter import Tk
# from customtkinter import CTkEntry
# from tkinter import Tk, Label, Entry, Button
#
# window = Tk()
# window.config(bg='white')
# width = window.winfo_screenwidth()
# height = window.winfo_screenheight()
# center_x = int(width / 2 - 500 / 2)
# center_y = int(height / 2 - 450 / 2)
# window.geometry(f"500x450+{center_x}+{center_y}")
# window.title("Hafiza")
# window.resizable(width=False, height=False)
#
#
# def get_user():
#     num1 = int(entry1.get())
#     num2 = int(entry2.get())
#
#     label_name = Label(window, text=f"{num1} + {num2} = {num1 + num2}", fg="red")
#
#     label_name.place(x=140, y=140)
#
#
# label = Label(window,
#               text="1-sonni kiriting:",
#               font=("Gabriola", 15, "bold"),
#               fg="black")
# label.place(x=100, y=80)
# entry1 = CTkEntry(window, corner_radius=20,
#                   font=("Showcard Gothic", 15))
# entry1.place(x=250, y=90)
# label = Label(window,
#               text="2-sonni kiriting:",
#               font=("Gabriola", 15, "bold"),
#               fg="black")
# label.place(x=100, y=180)
# entry2 = CTkEntry(window, corner_radius=20,
#                   font=("Showcard Gothic", 15))
# entry2.place(x=250, y=190)
#
# button = Button(window, text="Click me", command=get_user,
#                 font=("Gabriola", 10))
# button.place(x=135, y=200)
# window.mainloop()

# from tkinter import Tk, Label, Entry, Button
#
# window = Tk()
# width = window.winfo_screenwidth()
# height = window.winfo_screenheight()
# center_x = int(width / 2 - 500 / 2)
# center_y = int(height / 2 - 450 / 2)
# window.geometry(f"500x450+{center_x}+{center_y}")
# entry = Entry(window)
# text = Label(window, text="1-chi sonni kiriting",
#              font=("Modern No. 20", 15))
# text.place(x=0, y=37)
#
# entry.place(x=165, y=45)
# entry1 = Entry(window)
# text1 = Label(window, text="2-chi sonni kiriting",
#               font=("Modern No. 20", 15))
# text1.place(x=0, y=73)
#
# entry1.place(x=165, y=81)
# entry2 = Entry(window)
# entry2.place(x=165, y=82)
#
#
# def get_user():
#     entry_1 = entry.get()
#     label_1 = Label(window, text=f"{entry}+{entry_1}={entry + entry_1}", fg="red")
#     label_1.place(x=0, y=0)
#
#
# window.mainloop()

