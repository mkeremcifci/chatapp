import tkinter as tk
from loginPage import showLoginPage

def main():
    root = tk.Tk()
    root.title("Chatapp")
    showLoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()