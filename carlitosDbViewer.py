import sqlite3
from sqlite3 import Error
import pandas as pd
import numpy as np
import datetime as dt
from tkinter import *
from tkinter import ttk



conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

#cur.execute("SELECT *FROM movimientosCarlitos")

#db = pd.DataFrame(cur)
#print(db)

cur.execute("""SELECT * FROM movimientosCarlitos
    WHERE date BETWEEN '2018-06-18 00:00:00' AND '2018-06-18 23:59:59'
""")

db = pd.DataFrame(cur)
print(db)

#Tkinter

ctop = Tk()

#TKINTER STYLE
style = ttk.Style(ctop)
# set ttk theme to "clam" which support the fieldbackground option
style.theme_use("clam")
#TREESTYLE
style.configure("Treeview", background="#200200200", 
                fieldbackground="#200200200", foreground="white")
#TREEHEADERSTYLE
style.configure("Treeview.Heading", background="#200200200", 
                fieldbackground="#200200200", foreground="white")

menu = Menubutton(ctop,bg="#600600600",fg="grey",activebackground="#300300300", text="Menu")
filemenu = Menu(menu,tearoff = 0 )
filemenu.add_command(label="quit", command=ctop.quit)
menu.config(menu=filemenu)

ctop.config (bg="grey")
menu.grid(row=0, column=0, ipadx=30)

ctop.iconbitmap('heicon.ico')
ctop.title("Carli")
ctop.geometry("1000x600")

tree = ttk.Treeview(ctop)

tree.heading("#0",text="tree", anchor="w")

tree.insert("", 0, "item", text="item")
tree.grid(row=10, column=10, padx = 200)


ctop.mainloop()