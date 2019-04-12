import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

cur.execute(
    """create table caja(
        idMovimiento INT PRIMARY KEY,
        date DATETIME,
        tipopago INT,
        monto INT,
        cuenta INT 
    )""" 
)

