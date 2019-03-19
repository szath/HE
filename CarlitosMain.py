from tkinter import *
from tkintertable import TableCanvas, TableModel

import sqlite3
from sqlite3 import Error

top = Tk()

conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

top.geometry("800x600")
top.title("Carlitos")
top.mainloop()