rndEstado="Camioneta"
rndDia=1
rndMes=1
rndAño=2017
rndHora=0
rndMinuto=0
rndDestino=0

seqEstados=["Hockey","Camioneta","Salida"]

def diaAleatorio():
    rndEstado= random.choice(seqEstados)

rndTuple=(rndEstado, rndDia, rndMes, rndAño, rndHora, rndMinuto, rndDestino)

cur.execute(
   """INSERT INTO movimientos(estado,dia,mes,año,hora,minuto,destino)
    VALUES (?,?,?,?,?,?,?)
""", rndTuple )  """
 
conn.commit()
cur.close()