import sqlite3
from sqlite3 import Error
import random
import pandas as pd
import numpy as np
import datetime as dt

conn = sqlite3.connect('hetest.db') #connects to the db in the working folder
cur = conn.cursor() #creates db cursor



"""f = open("datosCarlitosGdrive.txt", "r")
myList = []
for line in f:
    myList.append(line)
print(myList)"""

carlitosTxtDb = pd.read_csv("datosCarlitosGdrive.txt")
#print(carlitosTxtDb)

loadLength = carlitosTxtDb.shape[0] #lineas a cargar

#carliCol = pd.DataFrame(carlitosTxtDb,[0])
#print(carliCol)
#print(carliCol.values)

#for x in range (0, loadLength): #Actual Loop
for x in range (0, 34): #Test Loop

    print("Line ", x)

    #Cargar los Datos a Variables desde el Frame de Panda para poder operar
    carliCol = pd.DataFrame(carlitosTxtDb,[x])
    lineValues = carliCol.values[0]

    horaMovimiento = lineValues[2]
    tipoMovimiento = lineValues[0]

    if not pd.isnull(lineValues[1]) : #pd.isnull interactua con nan values que vienen del panda
       fechaActual = lineValues[1]

    destino = lineValues[3]

    #print(horaMovimiento,tipoMovimiento,fechaActual,destino)

    #Manipular la Fecha y hora // string to text

    fechas = fechaActual.split("/")
    dia = fechas[0]
    mes = fechas[1]
    try:
        año = fechas[2]
    except IndexError:
        if x < 775: #correccion fechas cargadas mal, asumimos el año segun epoca
            año = 2018
        else:
            año = 2019 
    #print(fechas)
    #print(año)

    horas = horaMovimiento.split(":")
    hora = horas[0]
    minuto = horas[1]
    try:
        segundo = horas[2]
    except IndexError: #algunas fechas no estan cargadas correctamente
        segundo = 0

    fechaSQL = str(año)+"-"+str(mes)+"-"+str(dia)+" "+str(hora)+":"+str(minuto)+":"+str(segundo)
    print(fechaSQL)

    #Cargar los Datos a SQL

    cur.execute(
    """INSERT INTO movimientosCarlitos VALUES (?,?,?,?)""", (tipoMovimiento,fechaSQL,destino,0)
    ,  )

conn.commit()
conn.close()