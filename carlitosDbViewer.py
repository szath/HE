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

#Getting SQL DATA


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

menuFrame = Frame(ctop,bg="#200200200")
menuFrame.pack(fill="both")

menu = Menubutton(menuFrame,bg="#600600600",fg="grey",activebackground="#300300300", text="File")
filemenu = Menu(menu,tearoff = 0 )
filemenu.add_command(label="quit", command=ctop.quit)
menu.config(menu=filemenu)

menu2 = Menubutton(menuFrame,bg="#600600600",fg="grey",activebackground="#300300300", text="Options")
optionMenu = Menu(menu2,tearoff = 0 )
optionMenu.add_command(label="quit", command=ctop.quit)
menu2.config(menu=optionMenu)


ctop.config (bg="grey")
menu.grid(row=0, column=0, ipadx=30, sticky="w")
menu2.grid(row=0, column=1, ipadx=30, sticky="w")

ctop.iconbitmap('heicon.ico')
ctop.title("Carlitos")

tree = ttk.Treeview(menuFrame)

tree.heading("#0",text="tree", anchor="w")

tree.insert("", 0, "item", text="item")
tree.grid(row=3, column=0, columnspan=10)


ctop.mainloop()