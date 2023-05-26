import tkinter

#-------Ventana-------
ventana = tkinter.Tk()
ventana.title("Prueba")
ventana.geometry("700x500")
ventana.resizable(0,0)

#------botones
def saludo():
    tkinter.Label(ventana, text="hello word").pack

def salir():
    ventana.destroy

boton = tkinter.Button(ventana, text="Invocar saludo", command= saludo, fg="red")
boton.pack()
boton.place(x= 300, y= 250) #ubicar boton dentro de ventana






ventana.mainloop()



#tkinter._test()
