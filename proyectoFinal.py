import tkinter

#-------Ventana-------
ventana = tkinter.Tk()
ventana.title("Prueba")
ventana.geometry("700x500")
ventana.resizable(0,0)

#------botones
def abrir():
    tkinter.Label(ventana, text="Aqui va abrir").pack()

def guardar():
    tkinter.Label(ventana, text="Aqui va Guardar").pack()

def eliminar():
        ventana.destroy()

botonAbrir = tkinter.Button(ventana, text="Invocar saludo", command= abrir, fg="red")
botonAbrir.pack()
botonAbrir.place(x= 100, y= 50) #ubicar boton dentro de ventana

botonGuardar = tkinter.Button(ventana, text="Invocar saludo", command= guardar, fg="red")
botonGuardar.pack()
botonGuardar.place(x= 350, y= 50)

botonEliminar = tkinter.Button(ventana, text="Invocar saludo", command= eliminar, fg="red")
botonEliminar.pack()
botonEliminar.place(x= 600, y= 50)





ventana.mainloop()



#tkinter._test()
