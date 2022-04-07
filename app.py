from tkinter import *
from tkinter import filedialog as fd
import tkinter.messagebox as mb


def choose_file():
    file_name = fd.askopenfilename()
    mb.showinfo("путь к файлу", file_name)
    print(file_name)


root = Tk()
root.resizable(width=False, height=False)
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Выбрать файл", command=choose_file)
b1.place(x=100, y=40)

root.mainloop()
