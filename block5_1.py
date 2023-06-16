import tkinter as tk
from tkinter import filedialog, messagebox
import os
from tkinter import ttk

class TextEditor(tk.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(wrap=tk.WORD)  # Habilitar ajuste de línea automático
        self.bind("<Control-a>", self.select_all)  # Ctrl+A para seleccionar todo

    def select_all(self, event):
        self.tag_add(tk.SEL, "1.0", tk.END)
        self.mark_set(tk.INSERT, "1.0")
        self.see(tk.INSERT)
        return "break"

def update_file_tree():
    directory = filedialog.askdirectory()
    if directory:
        create_folders = messagebox.askyesno("Crear carpetas", "¿Deseas crear una carpeta por cada mes?")
        if create_folders:
            create_monthly_folders(directory)
        else:
            file_tree.delete(*file_tree.get_children())
            populate_file_tree(directory)

def create_monthly_folders(directory):
    lang_choice = messagebox.askquestion("Idioma de los meses", "¿Deseas que las carpetas tengan el nombre de los meses en español?")
    if lang_choice == "yes":
        months = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
    else:
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

    for month_num, month_name in enumerate(months, start=1):
        month_directory = os.path.join(directory, month_name)
        os.makedirs(month_directory, exist_ok=True)

    file_tree.delete(*file_tree.get_children())
    populate_file_tree(directory)

def populate_file_tree(directory, parent=""):
    items = os.listdir(directory)
    for item in items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            folder_id = file_tree.insert(parent, "end", text=item, open=False)
            populate_file_tree(item_path, folder_id)
        else:
            file_tree.insert(parent, "end", text=item, values=(item_path,))

def open_file(event):
    selected_item = file_tree.focus()
    if selected_item:
        item_type = file_tree.item(selected_item)["text"]
        if item_type != "":
            file_path = file_tree.item(selected_item)["values"][0]
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    text_editor.configure(state="normal")  # Habilitar el widget de texto
                    text_editor.delete('1.0', tk.END)
                    text_editor.insert(tk.END, content)
            except IOError:
                messagebox.showerror("Error", "No se pudo abrir el archivo.")
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

def save_file():
    pass

def save_file_as():
    pass

def on_tree_select(event):
    selected_item = file_tree.focus()
    if selected_item:
        item_type = file_tree.item(selected_item)["text"]
        if item_type != "":
            file_path = file_tree.item(selected_item)["values"][0]
            if os.path.isfile(file_path):
                return
    event.widget.selection_remove(selected_item)

# Crear la ventana principal
root = tk.Tk()
root.title("Bloc de notas 5.0 - Definitive  Deluxe Goty Edition")

# Crear los widgets
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir directorio", command=update_file_tree)
file_menu.add_command(label="Guardar", command=save_file)
file_menu.add_command(label="Guardar como", command=save_file_as)
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
