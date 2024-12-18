import tkinter as tk
from loginHandler import handleLogin



def showLoginPage(root):
    def login():
        username = entryUsername.get()
        password = entryPassword.get()
        handleLogin(username=username, password=password)

    root.geometry("500x400")


    font_style = ("Arial", 14)


    labelUsername = tk.Label(root, text="Kullanıcı Adı:", font=font_style)
    labelUsername.pack(pady=15)


    entryUsername = tk.Entry(root, font=font_style)
    entryUsername.pack(pady=10)


    labelPassword = tk.Label(root, text="Parola:", font=font_style)
    labelPassword.pack(pady=15)


    entryPassword = tk.Entry(root, show="*", font=font_style)
    entryPassword.pack(pady=10)


    loginButton = tk.Button(root, text="Giriş Yap", command=login,font=font_style, width=15, height=2)
    loginButton.pack(pady=20)
