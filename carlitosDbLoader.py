import sqlite3
from sqlite3 import Error
import random

conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor

