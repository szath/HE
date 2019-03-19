from tkinter import *
from tkintertable import TableCanvas, TableModel

import sqlite3
from sqlite3 import Error


conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

top = Tk()

opt = Menu(top, activebackground="#CCCCCCFFF", bg="#700000000", title="Carlitos", fg="#900900900", activeforeground="#000000700")
fopt = Menu(opt, tearoff=0, bg="white", fg="black", activebackground="#B11ECCFFF", activeforeground="black")
fopt.add_command(label="Abrir", command=None)
fopt.add_command(label="Imprimir", command=None)
opt.add_cascade(label="Carlitos", menu=fopt)

top.iconbitmap('heicon.ico')
top.title("Hockey Equipment")
top.geometry("1000x600")

top.configure(bg="#600600600", menu=opt)

top.mainloop()