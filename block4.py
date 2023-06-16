import tkinter as tk
from tkinter import filedialog, messagebox
import os

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

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        folder_listbox.delete(0, tk.END)
        file_listbox.delete(0, tk.END)
        folder_contents = os.listdir(directory)
        for item in folder_contents:
            if os.path.isdir(os.path.join(directory, item)):
                folder_listbox.insert(tk.END, item)
        folder_listbox.bind('<<ListboxSelect>>', lambda event: update_file_listbox(directory))

def update_file_listbox(directory):
    selected_folder = folder_listbox.get(folder_listbox.curselection())
    folder_path = os.path.join(directory, selected_folder)
    file_listbox.delete(0, tk.END)
    if os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        for file in files:
            file_listbox.insert(tk.END, file)

def open_file(event):
    folder_selection = folder_listbox.curselection()
    if folder_selection:
        folder_index = int(folder_selection[0])
        folder = folder_listbox.get(folder_index)
        selection = file_listbox.curselection()
        if selection:
            index = int(selection[0])
            selected_file = file_listbox.get(index)
            directory = filedialog.askdirectory()
            if directory:
                file_path = os.path.join(directory, folder, selected_file)
                try:
                    with open(file_path, 'r') as file:
                        text_editor.delete('1.0', tk.END)
                        text_editor.insert(tk.END, file.read())
                except IOError:
                    messagebox.showerror("Error", "No se pudo abrir el archivo.")
            else:
                messagebox.showwarning("Advertencia", "No se seleccionó ningún directorio.")
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ninguna carpeta.")

def save_file():
    pass

def save_file_as():
    pass

# Crear la ventana principal
root = tk.Tk()
root.title("Bloc de Notas")

# Crear los widgets
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Seleccionar directorio", command=select_directory)
file_menu.add_command(label="Guardar", command=save_file)
file_menu.add_command(label="Guardar como...", command=save_file_as)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
root.config(menu=menu_bar)

folder_listbox = tk.Listbox(root, width=40)
file_listbox = tk.Listbox(root, width=40)
text_editor = TextEditor(root, width=80, height=20)

# Configurar el evento de doble clic en el listbox de archivos
file_listbox.bind("<Double-Button-1>", open_file)

# Posicionar los widgets en la ventana
folder_listbox.grid(row=0, column=0, padx=10, pady=10)
file_listbox.grid(row=0, column=1, padx=10, pady=10)
text_editor.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Iniciar la aplicación
root.mainloop()
