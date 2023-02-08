from main import form, text
from tkinter import *

file_name = NONE


def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)
