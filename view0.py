from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sqlite3


# Начало блока 9
# Начало блока 5
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('views', check_same_thread=False)
        self.cursor = self.conn.cursor()


class Database1(Database):
    def geti(self):
        global temper
        global ocad
        temper = []
        ocad = []
        self.cursor.execute("select count(*) from viewq")
        row_count = self.cursor.fetchone()
        row_count = int(row_count[0])
        self.cursor.execute("SELECT * FROM viewq")
        al = self.cursor.fetchall()
        for i in range(row_count):
            a = al[i]
            temper.append(a[0])
            b = al[i]
            ocad.append(b[1])

def ensided(password):
    alfavit_EU =  'abcdefghigklmnopqrstuvyxwz12345678№;#%*90ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    smeshenie = 7
    message = password
    itog = ''
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto - smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else:
            itog += i
    return (itog)

db = Database()
db1 = Database1()
root = Tk()
number = 0
photo_list = [
    ImageTk.PhotoImage(Image.open("media/lunaw.png")),
    ImageTk.PhotoImage(Image.open("media/lunab.png"))
]
db1.geti()
columns = ("name", "password")
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)


# Функция смены темы/начало
# Функция смены темы/конец
# Создание окна/начало
root.title("Просмотр паролей")
icon = PhotoImage(file="media\icon.png")
root.iconphoto(False, icon)
w = root.winfo_screenwidth() // 2 - 350
h = root.winfo_screenheight() // 2 - 200
root.geometry(f'700x400+{w}+{h}')
root.minsize(700, 400)
root.maxsize(700, 400)
root.configure(bg="white")

# определяем заголовки с выпавниваем по левому краю
tree.heading("name", text="Название", anchor=W)
tree.heading("password", text="Пароль", anchor=W)
# настраиваем столбцы
tree.column("#1", stretch=NO, width=70)
tree.column("#2", stretch=NO, width=200)
for i in range(len(temper)):
    tree.insert("", END, values=(temper[i], ensided(ocad[i])))
root.mainloop()
