from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sqlite3


# Начало блока 9
# Начало блока 5
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('journal', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def count(self):
        self.cursor.execute("select count(*) from journaltos")
        row_count = self.cursor.fetchone()
        return row_count
# Конец блока 5


db = Database()
root = Tk()
number = 0
photo_list = [
    ImageTk.PhotoImage(Image.open("media/lunaw.png")),
    ImageTk.PhotoImage(Image.open("media/lunab.png"))
]


# Функция смены темы/начало
def change_theme():
    current_bg = root.cget("bg")
    if current_bg == "white":
        root.configure(bg="black")
        theme_button.config(image=photo_list[1])
        button.config(bg="black", fg="white")
    elif current_bg == 'black':
        root.configure(bg="white")
        theme_button.config(image=photo_list[0])
        button.config(bg="white", fg="black")
# Функция смены темы/конец


def journal():
    pass
    


# Создание окна/начало
root.title("Исследовательская станция на необитаемом острове")
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
# Создание окна/конец
# Начало блока 1

button = Button(root, text="Сгенерировать пароль", command=journal, width=30, height=1, relief=FLAT)
button.grid(row=0, column=0, padx=10, pady=0, sticky=N+E)
# Конец блока 1

root.mainloop()
