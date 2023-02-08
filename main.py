from working_with_a_note import *

text.pack()

file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить как", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Выход")


root.config(menu=menu_bar)
root.mainloop()
