from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
import working_with_a_note as wwn

form = Tk()
form.title("Заметки")
form.geometry("500x500")

menu_bar = Menu(form)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Файл", menu=file_menu)

text = Text(form, width=500, height=500)
text.pack()

form.config(menu=menu_bar)
form.mainloop()
