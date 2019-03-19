import sqlite3
from sqlite3 import Error
import random
import pandas as pd

conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

"""f = open("datosCarlitosGdrive.txt", "r")
myList = []
for line in f:
    myList.append(line)
print(myList)"""

df = pd.read_csv("datosCarlitosGdrive.txt")
print(df)

currentLine = 0
