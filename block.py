from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory, askopenfilename, asksaveasfilename
import calendar
import ctypes
import os

# Función para crear las carpetas de los 12 meses
def crear_carpetas_meses(directorio):
    # Verificar si el directorio existe
    if os.path.isdir(directorio):
        # Obtener los nombres de los meses
        nombres_meses = calendar.month_name[1:]

        # Crear las carpetas de los meses
        for mes in nombres_meses:
            carpeta_mes = os.path.join(directorio, mes)
            if not os.path.exists(carpeta_mes):
                os.mkdir(carpeta_mes)
        return True
    return False

# Funcion guardar archivos
def guardar_arc():
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    #Obtener nombre del archivo
    archivo = os.path.basename(filepath)
    #Extraer el nombre del archivo
    mes = obt_mes(archivo)
    #Crea la ruta de la carpeta del mes
    carpeta = os.path.join(os.getcwd(), mes)
    #Verifica la existencia de la carpeta
    if not os.path.exists(carpeta):
        os.mkdir(carpeta)

    #Guarda en la carpeta correspondiente
    ruta_guardar = os.path.join(carpeta, archivo)
    with open(ruta_guardar, "w") as output_file:
        text = text_edit.get(1.0, END)
        output_file.write(text)

    ventana.title(f"Bloc de Notas - {filepath}")

def guardar():
    filepath = ventana.title().replace("Bloc de Notas - ", "")
    if not filepath:
        guardar_arc()
    else:
        with open(filepath, "w") as output_file:
            text = text_edit.get(1.0, END)
            output_file.write(text)

#Funcion para obtener el mes del archivo

def obt_mes(archivo):
#Suponiendo que el mes esta al inicio del nombre del archivo    
    mes = archivo.split("_")[0]
    return mes
#Funcion para obtener los nombres de los meses y crear las carpetas    
def obt_nombre_mes(directorio):
    nombre_carpeta= []
    if os.path.isdir(directorio):
        nombre_carpeta = [carpeta for carpeta in os.listdir(directorio) if os.path.join(directorio, carpeta)]
    return nombre_carpeta

#actualizar listbox
def actualizar_archivos(event):
    indice_seleccionado = lista_mes.curselection()
    if indice_seleccionado:
        carpeta_seleccionada = lista_mes.get(indice_seleccionado)

        # Obtener la ruta completa del directorio seleccionado
        ruta_directorio = os.path.join(os.getcwd(), carpeta_seleccionada)

        # Limpiar la lista de archivos
        lista_archivos.delete(0, END)

        # Verificar que el directorio exista
        if os.path.isdir(ruta_directorio):
            contenido = os.listdir(ruta_directorio)
            for elemento in contenido:
                ruta_elemento = os.path.join(ruta_directorio, elemento)
                if os.path.isfile(ruta_elemento) and elemento.endswith(".txt"):
                    lista_archivos.insert(END, elemento)

# Abrir archivo seleccionado en modo de edición
def abrir_archivo_seleccionado(event):
    archivo_seleccionado = lista_archivos.get(lista_archivos.curselection())
    if archivo_seleccionado.endswith(".txt"):
        return

    directorio_seleccionado = lista_mes.get(lista_mes.curselection())
    ruta_archivo = os.path.join(os.getcwd(), directorio_seleccionado, archivo_seleccionado)

    if os.path.isfile(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8"):
            contenido = archivo.read()
            ruta_archivo.close()
            text_edit.delete(1.0, END)
            text_edit.insert(END, contenido)
        ventana.title(f"Bloc de Notas - {ruta_archivo}")

#tamaño de la ventana
user32 = ctypes.windll.user32
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

#Editar un archivo 
'''def abrir_archivo_seleccionado(event):
    # Obtener el índice del archivo seleccionado
    indice = lista_archivos.curselection()

    # Verificar si se ha seleccionado un archivo
    if indice:
        # Obtener el nombre del archivo seleccionado
        archivo_seleccionado = lista_archivos.get(indice[0])
        # Construir la ruta completa del archivo
        carpeta_seleccionada = lista_mes.get(lista_mes.curselection())
        ruta_archivo = os.path.join(os.getcwd(), carpeta_seleccionada, archivo_seleccionado)
        # Verificar si el archivo existe
        if os.path.isfile(ruta_archivo):
            # Abrir el archivo en la ventana de texto
            text_edit.delete(1.0, END)
            with open(ruta_archivo, "r") as file:
                contenido = file.read()
                text_edit.insert(END, contenido)
            # Actualizar el título de la ventana
            ventana.title(f"Bloc de Notas - {ruta_archivo}")'''
            
def abrir_archivo_seleccionado(event):
    # Obtener el índice del archivo seleccionado
    indice = lista_archivos.curselection()

    # Verificar si se ha seleccionado un archivo
    if indice:
        # Obtener el nombre del archivo seleccionado
        archivo_seleccionado = lista_archivos.get(indice[0])
        # Construir la ruta completa del archivo
        carpeta_seleccionada = lista_archivos.get(lista_mes.curselection())
        ruta_archivo = os.path.join(os.getcwd(), carpeta_seleccionada, archivo_seleccionado)
        # Verificar si el archivo existe
        if os.path.isfile(ruta_archivo):
            # Abrir el archivo en la ventana de texto
            for i in range(3):
                linea = ruta_archivo.readline()
                text_edit.insert(END, linea)
            # Actualizar el título de la ventana
            ventana.title(f"Bloc de Notas - {ruta_archivo}")

# Crear la interfaz gráfica
ventana = Tk()
ventana.title("Bloc de Notas - Epicardo ")
ventana.geometry(f"{width}x{height}")

text_edit = Text(ventana, width=145, height=70)
text_edit.pack(side=RIGHT)

lista_mes = Listbox(ventana, width=30, height=70)
lista_mes.pack(side=LEFT)
lista_mes.bind("<<ListboxSelect>>", actualizar_archivos)

lista_archivos = Listbox(ventana, width=30, height=70)
lista_archivos.pack(side=LEFT)
lista_archivos.bind("<Double-Button-1>", abrir_archivo_seleccionado)

#Directorios
def seleccionar_directorio():
    directorio = askdirectory()
    if directorio:
        actualizar_archivos(directorio)

def actualizar_archivos(directorio):
    lista_mes.delete(0, END)
    lista_archivos.delete(0, END)

    if os.path.isdir(directorio):
        contenido = os.listdir(directorio)
        for elemento in contenido:
            ruta_elemento = os.path.join(directorio, elemento)
            if os.path.isdir(ruta_elemento):
                lista_mes.insert(END, elemento)
            else:
                # Verificar que el archivo sea de tipo txt
                if elemento.endswith(".txt"):
                    lista_archivos.insert(END, elemento)

def seleccionar_directorio():
    directorio = askdirectory()
    if directorio:
        respuesta = messagebox.askquestion("Crear carpetas de meses",
                                            "¿Desea crear las carpetas de los 12 meses en el directorio seleccionado?")
        if respuesta == "yes":
            if crear_carpetas_meses(directorio):
                actualizar_meses(directorio)
        else:
            actualizar_archivos(directorio)
'''
def eliminar_archivos(directorio):
    lista_archivos.delete(0, END)'''
    
def actualizar_meses(directorio):
    lista_mes.delete(0, END)

    if os.path.isdir(directorio):
        contenido = os.listdir(directorio)
        for elemento in contenido:
            ruta_elemento = os.path.join(directorio, elemento)
            if os.path.isdir(ruta_elemento):
                lista_mes.insert(END, elemento)

# Crear menú de archivo
menu_bar = Menu(ventana)

file_menu = Menu(menu_bar, tearoff=0)
#file_menu.add_command(label="Abrir", command=abrir_arc)
file_menu.add_command(label="Guardar", command=guardar)
file_menu.add_command(label="Guardar como...", command=guardar_arc)

file_menu.add_separator()
file_menu.add_command(label="Seleccionar directorio", command=seleccionar_directorio)

menu_bar.add_cascade(label="Archivo", menu=file_menu)

# Agregar la barra de menú a la ventana
ventana.config(menu=menu_bar)

# Ejecutar la aplicación
ventana.mainloop()
