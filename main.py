from tkinter import *
from tkinter import filedialog as fd
from tkinter.filedialog import askdirectory
from parsing import parser
from XML_CREATOR import create_xml

import xml.etree.ElementTree as ET
import os.path
import tkinter.messagebox as mb


def find_mask(file_name):
    f = open(file_name, 'rb')
    a = f.readline()
    a = list(map(int, a))
    s = ""
    while not (a[0] == 49 and a[1] == 50 and a[2] == 52 and a[3] == 48) and len(a) > 4:
        a = f.readline()
        a = list(map(int, a))
    if (a[0] == 49 and a[1] == 50 and a[2] == 52 and a[3] == 48) and len(a) > 4:
        a = a[4:20]
        s = ""
        for i in range(len(a)):
            string = str(bin(a[i]))[2:]
            s += "0" * (8 - len(string))
            s += string
    f.close()
    return s


def check_name(dst):
    i = 0
    s = dst + "/" + "final_file" + str(i) + ".xml"
    while os.path.exists(s):
        i += 1
        s = dst + "/" + "final_file" + str(i) + ".xml"
    return s


def sumcurrency(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    s = 0
    for i in range(len(root)):
        s+=int(root[i][1].text)
    root.text = 'Financial transaction 1240, Transactions summ: '+str(s)
    tree.write(file_path)


def choose_file():
    file_name = fd.askopenfilename()
    global dst
    dst = askdirectory()
    if len(file_name) > 0 and len(dst) > 0:
        mask = find_mask(file_name)
        name = check_name(dst)
        create_xml(name)
        if mask == "":
            msg = "Не удалось выполнить обработку файла"
            mb.showerror("Ошибка", msg)
            os.remove(name)
            return -1
        if parser(file_name, name) == -1:
            msg = "Не удалось выполнить обработку файла"
            mb.showerror("Ошибка", msg)
            os.remove(name)
        else:
            sumcurrency(name)
            msg = "Обработка выполнена успешно"
            mb.showinfo("Выполнено", msg)
    else:
        msg = "Не верно указаны директории"
        mb.showerror("Ошибка", msg)


root = Tk()
root["bg"] = "DarkCyan"
root.title("Обработка Клирингового Файла")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 200
h = h - 300
root.geometry('400x400+{}+{}'.format(w, h))
root.resizable(width=False, height=False)
b1 = Button(text="Выбрать файл для обработки", command=choose_file, height=3, width=30)
b1.place(x=95, y=100)
root.mainloop()
