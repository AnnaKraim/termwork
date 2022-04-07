from tkinter import *
from tkinter import filedialog as fd
import tkinter.messagebox as mb

def find_mask(file_name):
    f = open(file_name, 'rb')
    a = f.readline()
    a = list(map(int,a))
    while not(a[0]==49 and a[1] == 50 and a[2] == 52 and a[3] == 48):
        a = f.readline()
        a = list(map(int, a))
    a = a[4:20]
    s = ""
    for i in range(len(a)):
        string = str(bin(a[i]))[2:]
        s+="0"*(8-len(string))
        s+=string
    f.close()
    return s

def choose_file():
    file_name = fd.askopenfilename()
    mask = find_mask(file_name)

root = Tk()
root.resizable(width=False, height=False)
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Выбрать файл", command=choose_file)
b1.place(x=100, y=40)

root.mainloop()
