import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

cur.execute(
    """SELECT estado
    FROM movimientos"""
)

print( cur.fetchall() )