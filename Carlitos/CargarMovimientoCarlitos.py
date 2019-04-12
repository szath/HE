from tkinter import *
from tkintertable import TableCanvas, TableModel

import sqlite3
from sqlite3 import Error

top = Tk()

conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

labelEstado = Label(top, text="Estado")
labelFecha = Label(top, text="Fecha")
labelHora = Label(top, text="Hora")
labelDestino = Label(top, text="Destino")

labelEstado.grid(row=0)
labelFecha.grid(row=1)
labelHora.grid(row=2)
labelDestino.grid(row=3)

enEstado = Entry(top)
enFecha = Entry(top)
enHora = Entry(top)
enDestino = Entry(top)
enEstado.grid(row=0, column=1)
enFecha.grid(row=1, column=1)
enHora.grid(row=2, column=1)
enDestino.grid(row=3, column=1)

def callback():
    eget = e1.get()
    print(eget)

b = Button(top, text="CARGAR", width=10, command=callback)
b.grid(columnspan=2, sticky=EW)

top.geometry("180x120")
top.title("Cargar Movimientos")
top.mainloop()