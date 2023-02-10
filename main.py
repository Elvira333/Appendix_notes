from tkinter import messagebox, filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import *


def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)


def save_file():
    out = asksaveasfile(mode='w', defaultextension='.json')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror(".....", "Что-то пошло не так! Попробуйте ещё раз")


def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла',
                                           filetypes=(('Текстовые документы (*.json)', '*.json'), ('Все файлы', '*.*')))
    if file_path:
        text.delete('1.0', END)
        text.insert('1.0', open(file_path).read())


def chenge_theme(theme):
    text['bg'] = view_colors[theme]['text_bg']
    text['fg'] = view_colors[theme]['text_fg']
    text['insertbackground'] = view_colors[theme]['cursor']
    text['selectbackground'] = view_colors[theme]['select_bg']


def chenge_fonts(fontss):
    text['font'] = fonts[fontss]['font']


def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()

file_name = NONE

# основное окно
root = Tk()
root.title("Заметки")
root.geometry("500x700")
root.iconbitmap('Wordpad.ico')

# создаю меню бар
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
root.config(menu=file_menu)


# создаю вложенные списки с выбором для "Темы" и для "Шрифтов"
view_menu = Menu(menu_bar, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)

# Добавляю списки меню
menu_bar.add_cascade(label="Файл", menu=file_menu)
menu_bar.add_cascade(label="Вид", menu=view_menu)

file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить как", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=notepad_exit)

view_menu_sub.add_command(label='Тёмная', command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: chenge_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: chenge_fonts('TNR'))
view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)

root.config(menu=view_menu)
root.config(menu=menu_bar)

# Текст и главное окно
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
            spacing3=10, # добавила абзацы
            font='Arail 14 bold'
            )

# скролл бар
scroll = Scrollbar(root, command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll.set)
text.pack()

# словарь для тем
view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
    }

}

# словарь для шрифтов
fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'TNR': {
        'font': ('Times New Roman', 14, 'bold')
    }

}

root.mainloop()










