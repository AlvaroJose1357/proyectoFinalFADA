import tkinter

#-------Ventana-------
ventana = tkinter.Tk()
ventana.title("Prueba")
ventana.geometry("800x500")
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
botonAbrir.place(x= 5, y= 0) #ubicar boton dentro de ventana

botonGuardar = tkinter.Button(ventana, text="Invocar saludo", command= guardar, fg="red")
botonGuardar.pack()
botonGuardar.place(x= 95, y= 0)

botonEliminar = tkinter.Button(ventana, text="Invocar saludo", command= eliminar, fg="red")
botonEliminar.pack()
botonEliminar.place(x= 185, y= 0)





ventana.mainloop()

print("hola")
print("alvaro es gay")
print("alvaro es gay x 2")

#tkinter._test()
