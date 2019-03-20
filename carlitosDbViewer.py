import sqlite3
from sqlite3 import Error
import pandas as pd
import numpy as np
import datetime as dt

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