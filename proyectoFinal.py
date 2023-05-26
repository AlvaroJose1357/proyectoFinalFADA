import tkinter

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

#-------Ventana-------
if __name__ == '__main__':

    ventana = Tk()
ventana.title("Prueba: Bloc de Notas")
ventana.geometry("800x500")
ventana.resizable(0,0)
ventana.mainloop()

#-----------Menubar-----------

menubar = Menu(ventana)
ventana.config(menu=menubar)

archivo = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Archivo", menu=archivo)

archivo.add_command(label="Nuevo", command=nuevo)
archivo.add_command(label="Abrir     ", command=abrir)

archivo.add_command(label="Guardar     ", command=guardar)

archivo.add_command(label="Salir     ", command=ventana.quit)
#------botones
'''def abrir():
    tkinter.Label(ventana, text="Aqui va abrir").pack()

def guardar():
    tkinter.Label(ventana, text="Aqui va Guardar").pack()

def eliminar():
    tkinter.Label(ventana, text="Aqui va Eliminar").pack()

botonAbrir = tkinter.Button(ventana, text="Invocar saludo", command= abrir, fg="red")
botonAbrir.pack()
botonAbrir.place(x= 5, y= 0) #ubicar boton dentro de ventana

botonGuardar = tkinter.Button(ventana, text="Invocar saludo", command= guardar, fg="red")
botonGuardar.pack()
botonGuardar.place(x= 95, y= 0)

botonEliminar = tkinter.Button(ventana, text="Invocar saludo", command= eliminar, fg="red")
botonEliminar.pack()
botonEliminar.place(x= 185, y= 0)'''





ventana.mainloop()

print("hola")
print("alvaro es gay")


#tkinter._test()
