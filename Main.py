from tkinter import *
from tkintertable import TableCanvas, TableModel

import sqlite3
from sqlite3 import Error

almostBlack = "#200200200"
darkGrey = "#300300300"
grey = "#600600600"


conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

ctop = Tk()
ctop.iconbitmap('heicon.ico')
ctop.title("HE")
ctop.geometry("400x200")
ctop.config(bg="#200200200")

menuFrame = Frame(ctop,bg=darkGrey)
menuFrame.pack(fill="both")

menu = Menubutton(menuFrame,bg=darkGrey,fg="grey",activebackground=grey, text="File")
filemenu = Menu(menu,tearoff = 0 )
filemenu.add_command(label="quit", command=ctop.quit)
menu.config(menu=filemenu)

menu2 = Menubutton(menuFrame,bg=darkGrey,fg="grey",activebackground=grey, text="Options" )
optionMenu = Menu(menu2,tearoff = 0 )
optionMenu.add_command(label="quit", command=ctop.quit)
menu2.config(menu=optionMenu)

menu.grid(row=0, column=0, ipadx=2, sticky="w")
menu2.grid(row=0, column=1, ipadx=2, sticky="w")

#expandir workframe al maximo
workFrame = Frame(ctop,bg=almostBlack, height="4000", width="4000")
workFrame.pack(side="left")

#FullScreen theater mode
#ctop.attributes('-fullscreen', True)

#Get Aprox Wind size
#w, h = ctop.winfo_screenwidth(), ctop.winfo_screenheight()
#ctop.geometry("%dx%d+0+0" % (w, h))

#Risize Bind
"""def resize(event):
    print("New size is: {}x{}".format(event.width, event.height))

ctop.bind("<Configure>", resize)"""









#Maximize ctop
ctop.state('zoomed')



ctop.mainloop()