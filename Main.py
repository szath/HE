from tkinter import *
from tkintertable import TableCanvas, TableModel

import sqlite3
from sqlite3 import Error


conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

ctop = Tk()
ctop.iconbitmap('heicon.ico')
ctop.title("HE")
ctop.geometry("400x200")
ctop.config(bg="#200200200")

menuFrame = Frame(ctop,bg="#200200200")
menuFrame.pack(fill="both")

menu = Menubutton(menuFrame,bg="#300300300",fg="grey",activebackground="#600600600", text="File")
filemenu = Menu(menu,tearoff = 0 )
filemenu.add_command(label="quit", command=ctop.quit)
menu.config(menu=filemenu)

menu2 = Menubutton(menuFrame,bg="#300300300",fg="grey",activebackground="#600600600", text="Options" )
optionMenu = Menu(menu2,tearoff = 0 )
optionMenu.add_command(label="quit", command=ctop.quit)
menu2.config(menu=optionMenu)

menu.grid(row=0, column=0, ipadx=2, sticky="w")
menu2.grid(row=0, column=1, ipadx=2, sticky="w")

#expandir workframe al maximo
workFrame = Frame(ctop,bg="#200200200", height="4000", width="4000")
workFrame.pack(side="left")

ctop.mainloop()