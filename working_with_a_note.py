from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter import *

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

view_menu_sub.add_command(label='Тёмная', command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: chenge_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial')
font_menu_sub.add_command(label='Comic Sans MS')
font_menu_sub.add_command(label='Times New Roman')
view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
root.config(menu=view_menu)

# Добавляю списки меню
menu_bar.add_cascade(label="Файл", menu=file_menu)
menu_bar.add_cascade(label="Вид", menu=view_menu)

view_colors = {
    'dark':{
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
    },
    'light':{
        'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
    }

}



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
            spacing3=10 # добавила абзацы

            )

# добавляю скролл бар
scroll = Scrollbar(root, command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll.set)



file_name = NONE

def chenge_theme(theme):
    text['bg'] = view_colors[theme]['text_bg']
    text['fg'] = view_colors[theme]['text_fg']
    text['insertbackground'] = view_colors[theme]['cursor']
    text['selectbackground'] = view_colors[theme]['select_bg']


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