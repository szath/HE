import sqlite3
from sqlite3 import Error
import pandas as pd
import numpy as np
from datetime import datetime
#from dateutil import parser
from tkinter import *
from tkinter import ttk



conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

#cur.execute("SELECT *FROM movimientosCarlitos")

#db = pd.DataFrame(cur)
#print(db)

#SQL
fromdate = '2018-06-18 00:00:00'
tildate = '2018-06-18 23:59:59'

#get datetime from sql like string
pythondate = datetime.strptime(tildate, '%Y-%m-%d %H:%M:%S')
#pythondate = parser.parse(tildate)
print(type(pythondate))
print(pythondate)


cur.execute("""SELECT * FROM movimientosCarlitos
    WHERE date BETWEEN ? AND ?
""", (fromdate, tildate) )

db = pd.DataFrame(cur) #Load Db to Panda Dataframe
lenghtdb = db.shape[0]
print(lenghtdb)


#print(db)

