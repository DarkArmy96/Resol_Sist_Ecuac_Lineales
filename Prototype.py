import tkinter as tk
from tkinter import messagebox
import numpy as np

def resolver_sistema():
    try:
        # Obtener el tamaño de la matriz 'a' del usuario
        n = int(entry_num_ecuaciones.get())
        
        # Obtener los valores de la matriz 'a' del usuario
        a = []
        for i in range(n):
            row = []
            for j in range(n):
                val = float(matriz_entries[i][j].get())
                row.append(val)
            a.append(row)
        
        # Convertir a matriz NumPy
        a = np.array(a)
        
        # Obtener los valores del vector 'b' del usuario
        b = []
        for i in range(n):
            val = float(vector_entries[i].get())
            b.append(val)
        
        # Convertir a vector NumPy
        b = np.array(b)
        
        # Resolver el sistema de ecuaciones
        x = np.linalg.solve(a, b)
        np.set_printoptions(precision=2)
        
        # Mostrar la solución
        resultado_var.set(f"La solución es: {x}")
        
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Sistemas de Ecuaciones Lineales")

# Establecer el tamaño inicial de la ventana
ventana.geometry("600x400")

# Definir una fuente estándar
font_standard = ("Arial", 14)

# Frame para la matriz 'a'
frame_matriz = tk.Frame(ventana)
frame_matriz.pack(pady=10)

# Etiqueta y entrada para el número de ecuaciones
tk.Label(ventana, text="Número de ecuaciones:", font=font_standard).pack()
entry_num_ecuaciones = tk.Entry(ventana, font=font_standard)
entry_num_ecuaciones.pack()

# Función para crear las entradas de la matriz 'a' dinámicamente
def crear_entradas_matriz():
    num_ecuaciones = int(entry_num_ecuaciones.get())
    
    # Limpiar frame si ya hay widgets
    for widget in frame_matriz.winfo_children():
        widget.destroy()
    
    global matriz_entries
    matriz_entries = []
    for i in range(num_ecuaciones):
        fila_entries = []
        for j in range(num_ecuaciones):
            entry = tk.Entry(frame_matriz, width=5, font=font_standard)
            entry.grid(row=i, column=j, padx=5, pady=5)
            fila_entries.append(entry)
        matriz_entries.append(fila_entries)

# Botón para crear las entradas de la matriz 'a'
tk.Button(ventana, text="Crear matriz 'a'", command=crear_entradas_matriz, font=font_standard).pack()

# Frame y entradas para el vector 'b'
frame_vector = tk.Frame(ventana)
frame_vector.pack(pady=10)

# Función para crear las entradas del vector 'b' dinámicamente
def crear_entradas_vector():
    num_ecuaciones = int(entry_num_ecuaciones.get())
    
    # Limpiar frame si ya hay widgets
    for widget in frame_vector.winfo_children():
        widget.destroy()
    
    global vector_entries
    vector_entries = []
    for i in range(num_ecuaciones):
        entry = tk.Entry(frame_vector, width=10, font=font_standard)
        entry.grid(row=0, column=i, padx=5, pady=5)
        vector_entries.append(entry)

# Botón para crear las entradas del vector 'b'
tk.Button(ventana, text="Crear vector 'b'", command=crear_entradas_vector, font=font_standard).pack()

# Botón para resolver el sistema de ecuaciones
tk.Button(ventana, text="Resolver sistema", command=resolver_sistema, font=font_standard).pack()

# Variable para mostrar el resultado
resultado_var = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_var, wraplength=400, font=font_standard)
resultado_label.pack(pady=10)

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()
