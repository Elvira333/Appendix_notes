from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter import *

root = Tk()
root.title("Заметки")
root.geometry("500x500")
root.iconbitmap('Wordpad.ico')

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Файл", menu=file_menu)

text = Text(root,
            width=500,
            height=500,
            bg='black',  # темная тема окна
            fg='lime',   # цвет текста лайм
            padx=10,    # добавление отступов по краям
            pady=10,
            wrap=WORD,   # правильный перенос по словам
            insertbackground='brown', # добавление курсора
            selectbackground='#8D917A', # изменение цвета выделения текста
            spacing3=10 # добавила абзацы

            )

# добавляю скролл бар
scroll = Scrollbar(root, command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll.set)
file_name = NONE

def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)

def save_as():
    out = asksaveasfile(mode='w', defaultextension='.json')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Ой", "Нельзя сохранить файл!")

def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)