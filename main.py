from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

from working_with_a_note import *

text.pack()

file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)


form.config(menu=menu_bar)
form.mainloop()
