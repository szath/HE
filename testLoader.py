import sqlite3
from sqlite3 import Error
import random
import pandas as pd
import numpy as np
import datetime as dt

conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

for i in range (0,300) :
    print(i)
    idMov = i
    date = dt.datetime.now()
    tipoPago = 1
    monto = random.randint(0,300000)
    cuenta = random.randint(0,500)

    cur.execute(
        """INSERT INTO caja VALUES (?,?,?,?,?)""", (idMov,date,tipoPago,monto,cuenta)
    ,  )



conn.commit()
conn.close()