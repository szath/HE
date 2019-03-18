from tkinter import *
from tkintertable import TableCanvas, TableModel

top = Tk()

opt = Menu(top, activebackground="#CCCCCCFFF", bg="#700000000", title="CAJA", fg="#900900900", activeforeground="#000000700")
fopt = Menu(opt, tearoff=0, bg="white", fg="black", activebackground="#B11ECCFFF", activeforeground="black")
fopt.add_command(label="Abrir", command=None)
fopt.add_command(label="Imprimir", command=None)
opt.add_cascade(label="Caja", menu=fopt)

top.iconbitmap('he_2016_logo.ico')
top.title("Hockey Equipment")
top.geometry("1600x900")

top.configure(bg="#600600600", menu=opt)

top.mainloop()