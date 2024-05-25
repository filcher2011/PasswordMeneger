from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import random




# Начало блока 9
# Начало блока 5
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('views', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def count(self):
        self.cursor.execute("select count(*) from viewq")
        row_count = self.cursor.fetchone()
        return row_count
    def register(self, company, password):
        self.cursor.execute(f'INSERT INTO viewq (company, password) VALUES (?, ?)', (company, password))
        self.conn.commit()
        root.destroy()
        return True
# Конец блока 5


db = Database()
root = Tk()
number = 0
photo_list = [
    ImageTk.PhotoImage(Image.open("media/lunaw.png")),
    ImageTk.PhotoImage(Image.open("media/lunab.png"))
]


def desided(password):
    alfavit_EU =  'abcdefghigklmnopqrstuvyxwz12345678№;#%*90ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    smeshenie = 7
    message = password
    itog = ''
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else:
            itog += i
    return (itog)


def add():
    meat = txt1.get(1.0, END)
    cereal = desided(gen)
    db.register(meat, cereal)

gen = ''
# Функция смены темы/начало
def change_theme():
    current_bg = root.cget("bg")
    if current_bg == "white":
        root.configure(bg="black")
        theme_button.config(image=photo_list[1])
        button.config(bg="black", fg="white")
        text.config(bg="black", fg="white")
        lbl.config(bg="black", fg="white")
        txt1.config(bg="black", fg="white")
        btn.config(bg="black", fg="white")
    elif current_bg == 'black':
        root.configure(bg="white")
        theme_button.config(image=photo_list[0])
        button.config(bg="white", fg="black")
        text.config(bg="white", fg="black")
        lbl.config(bg="white", fg="black")
        txt1.config(bg="white", fg="black")
        btn.config(bg="white", fg="black")
# Функция смены темы/конец


def journal():
    global gen
    gen = ''
    for i in range(16): #Количество символов (16)
        gen = gen + random.choice('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ№;#%*?') #Символы, из которых будет составлен пароль
    text = Label(width=20, height=1, text=gen, bg='white')
    text.grid(row=1, column=0)

# Создание окна/начало
root.title("Генерация")
icon = PhotoImage(file="media\icon.png")
root.iconphoto(False, icon)
w = root.winfo_screenwidth() // 2 - 350
h = root.winfo_screenheight() // 2 - 200
root.geometry(f'700x400+{w}+{h}')
root.minsize(700, 400)
root.maxsize(700, 400)
root.configure(bg="white")
theme_button = Button(root, text="Тема", command=change_theme, image=photo_list[0], relief=FLAT)
theme_button.place(relx=.9, rely=.0)

text = Label(width=20, height=1, text=gen, bg='white')
text.grid(row=1, column=0)
lbl = Label(width=20, height=1, text='Название', bg='white')
lbl.grid(row=2, column=0)
txt1 = Text(width=20, height=1)
txt1.grid(row=3, column=0)
btn = Button(root, text="Ввести в базу данных", command=add, width=30, height=1, relief=FLAT, bg="white")
btn.grid(row=4, column=0)
button = Button(root, text="Сгенерировать пароль", command=journal, width=30, height=1, relief=FLAT, bg="white")
button.grid(row=0, column=0, padx=10, pady=0, sticky=N+E)

root.mainloop()






