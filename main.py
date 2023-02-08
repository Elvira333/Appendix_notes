from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

form = Tk()
form.title("Заметки")
form.geometry("500x500")

menu_bar = Menu(form)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Файл", menu=file_menu)

form.config(menu=menu_bar)
form.mainloop()
