from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from tkinter import ttk
from tkinter.filedialog import askdirectory, asksaveasfilename

'''Esto define la clase TextEditor que hereda de la clase tk.Text. La clase tk.Text es una clase predefinida en tkinter que proporciona una caja de texto editable en una interfaz gráfica.
'''
class TextEditor(tk.Text):
    def __init__(self, *args, **kwargs): # método de inicialización de la clase. Acepta cualquier número de argumentos posicionales y argumentos con nombre. Los argumentos *args y **kwargs se utilizan para pasar cualquier número de argumentos a la clase base tk.Text.
        super().__init__(*args, **kwargs) # Llama al método __init__ de la clase base tk.Text para inicializar la funcionalidad básica del widget de texto.
        self.config(wrap=tk.WORD)  # Habilitar ajuste de línea automático. wrap=tk.WORD indica que el ajuste de línea se realiza en función de palabras completas.
        self.bind("<Control-a>", self.select_all)  # Ctrl+A para seleccionar todo

    def select_all(self, event):
        self.tag_add(tk.SEL, "1.0", tk.END) # Agrega la etiqueta tk.SEL (que representa la selección de texto) desde el comienzo del texto ("1.0") hasta el final del texto (tk.END)
        self.mark_set(tk.INSERT, "1.0")# Mueve la marca de inserción tk.INSERT (que indica la posición del cursor) al comienzo del texto ("1.0"). Esto colocará el cursor al inicio del texto después de seleccionarlo todo.
        self.see(tk.INSERT)# Asegura que el cursor y la selección de texto sean visibles desplazando automáticamente la vista del widget de texto si es necesario.
        return "break"

'''Meses'''
#Funcion para obtener el mes del archivo
def obt_mes(archivo):
#Suponiendo que el mes esta al inicio del nombre del archivo    
    mes = archivo.split("_")[0]
    return mes

def crear_carpetas_mes(directory):
    elección_de_lengua = messagebox.askquestion("Idioma de los meses", "¿Deseas que las carpetas tengan el nombre de los meses en español?")
    if elección_de_lengua == "yes":
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
    else:
        meses = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
    for month_num, month_name in enumerate(meses, start=1): #utiliza para obtener tanto el índice del mes como su nombre
        month_directory = os.path.join(directory, month_name)#construye la ruta del directorio del mes
        os.makedirs(month_directory, exist_ok=True)# crear el directorio del mes.
    file_tree.delete(*file_tree.get_children())
    rellenar_arbol_archivo(directory)

def refrescar_arbol(func, directory):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        rellenar_arbol_archivo(directory)
    return wrapper

# Guardar - Guardar como
# Funcion "guardar"
def guardar():
    # Obtener el contenido del editor de texto
    contenido = text_editor.get("1.0", tk.END)
    # Obtener la ruta del archivo actualmente abierto
    selected_item = file_tree.focus()
    if selected_item: # verifica si se ha seleccionado un elemento en el árbol de archivos.
        item_type = file_tree.item(selected_item)["text"] #obtiene el tipo de elemento del árbol de archivos
        if item_type != "": #verifica que el tipo de elemento no esté vacío. Si el tipo de elemento está vacío, significa que no se ha seleccionado un archivo válido y no se realiza ninguna acción
            file_path = file_tree.item(selected_item)["values"][0]# obtiene la ruta del archivo seleccionado desde los valores asociados al elemento del árbol de archivos
            if os.path.isfile(file_path): #  verifica si la ruta del archivo es un archivo válido utilizando la función
                # Guardar el contenido en el archivo
                with open(file_path, "w") as file:
                    file.write(contenido)
                messagebox.showinfo("Éxito", "El archivo se ha guardado correctamente.")
            else:
                messagebox.showwarning("Advertencia", "No se ha seleccionado un archivo válido.")
        else:
            messagebox.showwarning("Advertencia", "No se ha seleccionado un archivo válido.")
    else:
        messagebox.showwarning("Advertencia", "No se ha seleccionado un archivo válido.")


# Funcion "guardar como" 
def guardar_arc():
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]) #del módulo tkinter.filedialog para solicitar al usuario la ruta de guardado. 
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
    with open(ruta_guardar, "w") as output_file: #Abre el archivo en modo escritura utilizando la ruta especificada 
        text = text_editor.get(1.0, END) #Obtiene el contenido del editor de texto.
        output_file.write(text)#  Escribe el contenido en el archivo.
    messagebox.showinfo("Éxito", "El archivo se ha guardado correctamente.")

#Funcion "Eliminar"

def eliminar(event=None):
    seleccion_item = file_tree.focus() # Obtener el ítem seleccionado en el árbol de archivos
    if seleccion_item:
        tipo_item = file_tree.item(seleccion_item)["text"] #Obtener el tipo de ítem
        if tipo_item != "":
            ruta_archivo = file_tree.item(seleccion_item)["values"][0] # Obtener la ruta del archivo seleccionado utilizando el atributo "values" del ítem
            if os.path.isfile(ruta_archivo): # si la ruta corresponde a un archivo existente
                #elimina archivo
                resultado = messagebox.askquestion("Eliminar archivo", "¿Estás seguro de que quieres eliminar este archivo?")
                if resultado == "yes":
                    os.remove(ruta_archivo)
                    messagebox.showinfo("Exito","Archivo eliminado correctamente")
            else:
                messagebox.showwarning("Advertencia", "No se ha seleccionado un archivo válido.")
        else:
            messagebox.showwarning("Advertencia", "No se ha seleccionado un archivo válido.")
    else:
        messagebox.showwarning("Advertencia", "No se ha seleccionado un archivo válido.")

# arbol 
# actualize el arbol de nodos cada que se seleccione un directorio, actuliza el arbol
def update_file_tree():
    directory = filedialog.askdirectory() # Solicita al usuario que seleccione un directorio
    if directory:
        create_folders = messagebox.askyesno("Crear carpetas", "¿Deseas crear una carpeta por cada mes?")
        if create_folders:
            crear_carpetas_mes(directory)
        else:
            file_tree.delete(*file_tree.get_children())
            rellenar_arbol_archivo(directory)

# mostrar el arbol de archivos y carpetas
def rellenar_arbol_archivo(directory, parent=""):
    items = os.listdir(directory) #Obtiene la lista de elementos en el directorio
    for item in items:
        item_path = os.path.join(directory, item)# Construye la ruta completa del elemento utilizando os.path.join
        if os.path.isdir(item_path): # Verifica si el elemento es un directori
            folder_id = file_tree.insert(parent, "end", text=item, open=False) #inserta un nodo en el árbol de archivos con el nombre del directorio. El identificador del padre es el valor de parent.
            rellenar_arbol_archivo(item_path, folder_id) #realiza una llamada recursiva a rellenar_arbol_archivo para explorar el contenido del directorio.
        else:
            file_tree.insert(parent, "end", text=item, values=(item_path,)) #inserta un nodo en el árbol de archivos con el nombre del archivo. El identificador del padre es el valor de parent. Además, se proporciona el valor de item_path como una tupla de valores para el nodo

#abrir el archivo seleccionado 
def open_file(event):
    selected_item = file_tree.focus() # Obtener el ítem seleccionado en el árbol de archivos
    if selected_item:
        item_type = file_tree.item(selected_item)["text"] #Obtener el tipo de ítem
        if item_type != "":
            file_path = file_tree.item(selected_item)["values"][0] 
            try:
                with open(file_path, 'r') as file: # Intenta abrir el archivo en modo de lectura
                    content = file.read() # lee su contenido y lo almacena en la variable
                    text_editor.configure(state="normal")  # Habilitar el widget de texto
                    text_editor.delete('1.0', tk.END)
                    text_editor.insert(tk.END, content)
            except IOError:
                messagebox.showerror("Error", "No se pudo abrir el archivo.")
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")


def on_tree_select(event):
    selected_item = file_tree.focus() # Obtener el ítem seleccionado en el árbol de archivos
    if selected_item:
        item_type = file_tree.item(selected_item)["text"] #Obtener el tipo de ítem
        if item_type != "":
            file_path = file_tree.item(selected_item)["values"][0] # Obtener la ruta del archivo seleccionado utilizando el atributo "values" del ítem
            if os.path.isfile(file_path): # realiza la vinculación del evento "<Delete>"
                root.bind("<Delete>", eliminar)  # usando la tecla Delete
                return
    event.widget.selection_remove(selected_item)# remueve la selección del elemento en el árbol para que no se resalte

# Crear la ventana principal
root = tk.Tk() 
root.title("Bloc de notas 5.0 - mamadisimo")

# Crear los widgets
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Guardar", command=guardar)
file_menu.add_command(label="Guardar como...", command=guardar_arc)
file_menu.add_command(label="Abrir directorio", command=update_file_tree)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
root.config(menu=menu_bar)

file_tree = ttk.Treeview(root, columns=("path",))
file_tree.heading("#0", text="Carpetas y archivos")
file_tree.column("#0", width=300)
file_tree.bind("<Double-Button-1>", open_file)
file_tree.bind("<<TreeviewSelect>>", on_tree_select)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=file_tree.yview)
file_tree.configure(yscrollcommand=scrollbar.set)

file_tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

text_editor = TextEditor(root, width=80, height=20)
text_editor.grid(row=1, column=0, padx=10, pady=10)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Iniciar la aplicación
root.mainloop()
