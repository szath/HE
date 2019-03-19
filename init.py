import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

cur.execute(
    """create table movimientos(
        estado TEXT,
        dia INT,
        mes INT,
        año INT,
        hora INT,
        minuto INT,
        destino TEXT
    )"""    
)  #Creates table movimientos