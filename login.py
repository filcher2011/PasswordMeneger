import customtkinter as ctk
import pickledb
import os
from tkinter import messagebox
import sqlite3

db = pickledb.load('user.db', True)

app = ctk.CTk()
app.title('Авторизация')
app.geometry('250x300')
app.resizable(width=False, height=False)

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")

def login():
    def loginUser():
        user = loginInput.get()
        password = passInput.get()
        if user == db.get('username') and password == db.get('password'):
            os.system('python view0.py')
        else:
            messagebox.showerror('Ошибка', 'Неверный логин или пароль')

    label = ctk.CTkLabel(app, text="Авторизация", font=("Arial", 18)).pack()
    null = ctk.CTkLabel(app,text="").pack()
    loginInput = ctk.CTkEntry(app, placeholder_text="Введите логин")
    loginInput.pack()
    passInput = ctk.CTkEntry(app, placeholder_text="Введите пароль")
    passInput.pack()
    null = ctk.CTkLabel(app,text="").pack()
    login = ctk.CTkButton(app, text="Войти", command=loginUser).pack()
    ending = ctk.CTkButton(app, text="Сброс", command=delit).pack()
    ctk.CTkLabel(app,text="После удаления").pack()
    ctk.CTkLabel(app,text="Перезагрузите приложение").pack()

def delit():
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('views')
    cursor = connection.cursor()

    # Удаляем всё
    cursor.execute('DELETE FROM viewq')

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()
    db.rem("username")
    db.rem("password")
    db.set("logins", False)
def register():
    def regUser():
        user = loginInput.get()
        password = passInput.get()
        if user != " " and password != " ":
            db.set('username', user)
            db.set('password', password)
            db.set('logins', True)
            os.system('python view0.py')
        else:
            messagebox.showerror('Ошибка', 'Неверный логин или пароль')

    label = ctk.CTkLabel(app, text="Вход", font=("Arial", 18)).pack()
    null = ctk.CTkLabel(app,text="").pack()
    loginInput = ctk.CTkEntry(app, placeholder_text="Введите логин")
    loginInput.pack()
    passInput = ctk.CTkEntry(app, placeholder_text="Введите пароль")
    passInput.pack()
    null = ctk.CTkLabel(app,text="").pack()
    login = ctk.CTkButton(app, text="Войти", command=regUser).pack()

if db.get('logins') == True:
    login()
else:
    register()

if __name__ == '__main__':
    app.mainloop()