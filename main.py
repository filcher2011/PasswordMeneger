import customtkinter as ctk
import os

app = ctk.CTk()

ctk.set_default_color_theme("dark-blue")

ctk.set_appearance_mode("dark")
def createPasswordFunc():
    os.system('python generate.py')

def readPasswordFunc():
    os.system('python login.py')
    

app.geometry('600x300')
app.title("Менеджер паролей — filcher & Nifko")

createPassword = ctk.CTkButton(app, text="Создать пароль", command=createPasswordFunc).grid(row=0, column=0, padx=10, pady=(100, 10), sticky="nsew")
readPassword = ctk.CTkButton(app, text="Просмотреть пароли", command=readPasswordFunc).grid(row=0, column=1, padx=10, pady=(100, 10), sticky="nsew")

description = ctk.CTkLabel(app, text="Данный менеджер паролей абсолютно безопасный. \nВсе пароли шифруются и сохраняются в шифрованном виде. \nПрограмма также полностью бесплатная, и с открытым исходным кодом.").grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 10), sticky="nsew")

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

if __name__ == '__main__':
    app.mainloop()