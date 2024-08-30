from tkinter import Tk, PhotoImage, Label, Entry, Button, Spinbox, Radiobutton, StringVar, IntVar
from PIL import ImageTk, Image
from customtkinter import CTkEntry
from tkinter import messagebox
from customtkinter import CTkButton, CTkLabel, CTkComboBox
import webbrowser
from country import country

window = Tk()
window.title("Registration")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.config(background="#0076F1")
center_x = int(width / 2 - 500 / 2)
center_y = int(height / 2 - 600 / 2)
window.geometry(f"500x600+{center_x}+{center_y}")
rl = Label(window, text="Register Form", font=("Goudy Old Style", 33, "bold"), bg="#0076F1")
rl.place(x=120, y=10)
fne = CTkEntry(window, width=180, height=35, justify="center", font=("Goudy Old Style", 15, "bold"), text_color="gray",
               placeholder_text="Firs Name", placeholder_text_color="gray")
fne.place(x=40, y=100)
lne = CTkEntry(window, width=180, height=35, justify="center", font=("Goudy Old Style", 15, "bold"), text_color="gray",
               placeholder_text="Last Name", placeholder_text_color="gray")
lne.place(x=265, y=100)
ele = CTkEntry(window, width=405, height=35, justify="center", font=("Goudy Old Style", 15, "bold"), text_color="gray",
               placeholder_text="Email Address", placeholder_text_color="gray")
ele.place(x=40, y=180)
cb = CTkComboBox(window, values=country,
                 font=("Goudy Old Style", 20),
                 state="readonly",
                 height=30,
                 width=180,
                 justify="center",
                 text_color="gray")
cb.place(x=40, y=260)
cb.set("Chooise")
als = Spinbox(window, from_=1, to=100, justify="center", bg="#343638", fg="gray", )
als.place(x=280, y=260, width=160, height=30)
pe = CTkEntry(window, width=180, height=35, justify="center", font=("Goudy Old Style", 15, "bold"), text_color="gray",
              placeholder_text="Password", placeholder_text_color="gray", show="*")
pe.place(x=40, y=330)
gv = StringVar(value="Male")
cpe = CTkEntry(window, width=180, height=35, justify="center", font=("Goudy Old Style", 15, "bold"), text_color="gray",
               placeholder_text="Password Confir", placeholder_text_color="gray", show="*")
cpe.place(x=270, y=330)
mr = Radiobutton(window, text="Male", variable=gv, value="Male", font=("Goudy Old Style", 15, "bold"), bg="#0076F1",
                 fg="gray", activebackground="#0076F1")
mr.place(x=140, y=390)
fr = Radiobutton(window, text="Female", variable=gv, value="Female", font=("Goudy Old Style", 15, "bold"), bg="#0076F1",
                 fg="gray", activebackground="#0076F1")
fr.place(x=250, y=390)


def get_user():
    fn = fne.get()
    ln = lne.get()
    e = ele.get()
    c = cb.get()
    a = als.get()
    p = pe.get()
    cp = cpe.get()

    if fn and ln and e and c and a:
        if p == cp:
            messagebox.showinfo(title="Saqlandi",
                                message="Malumotlaringiz Saqlandi")
        else:
            messagebox.showerror(title="Xatolik",
                                 message="Parolingiz bir xil bo'lish kerak")
    else:
        messagebox.showerror(title="Xatolik",
                             message="Iltimos Kiritmagan Narsangizni Kiriting")


btn = CTkButton(window, text="Submit", bg_color="#0000CD", text_color="gray", command=get_user, width=500, height=50)
btn.place(x=0, y=450)


def open_facebook():
    webbrowser.open_new("https://www.facebook.com/profile.php?id=61563767707611&mibextid=LQQJ4d")


def open_instagram():
    webbrowser.open_new("https://www.instagram.com/yahikuma?igsh=MWF4NDV5NzM0NzB1cg%3D%3D&utm_source=qr")


def open_youtube():
    webbrowser.open_new("https://youtube.com/channel/UC07DXU0uQpNAhmC-y5VRzqQ?si=EWCG_3E2gihDZ5Mu")


fi = Image.open("facebook.png")
size = fi.resize((90, 40))
fp = ImageTk.PhotoImage(size)
fb = Button(window, image=fp, command=open_facebook)
fb.place(x=90, y=530)
ii = Image.open("images (1).jfif")
size1 = ii.resize((90, 40))
ip = ImageTk.PhotoImage(size1)
ib = Button(window, image=ip, command=open_instagram)
ib.place(x=200, y=530)
yi = Image.open("Youtube.logo.png")
size2 = yi.resize((90, 40))
yp = ImageTk.PhotoImage(size2)
yb = Button(window, image=yp, command=open_youtube)
yb.place(x=310, y=530)
window.mainloop()
