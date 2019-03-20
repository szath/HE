import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

cur.execute(
    """create table cuentaCarlitos(
        idPago INT PRIMARY KEY,
        monto INT
    )""" 
)

cur.execute(
    """create table movimientosCarlitos(
        estado TEXT,
        date DATETIME,
        destino TEXT,
        idPago INT,
        FOREIGN KEY (idPago) REFERENCES cuentaCarlitos (idPago)
    )"""    
)  #Creates table movimientos

