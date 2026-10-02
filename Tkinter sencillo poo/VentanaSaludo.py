import tkinter as tk
from tkinter import ttk, messagebox

from BaseVentana import BaseVentana

class VentanaSaludo(BaseVentana):
    # Queremos que pida un nombre y mueste un saludo.
    TITULO = 'Saludo'
    ANCHO = 320
    ALTO = 180
    
    def __init__(self, padre):
        self.nombre_var = tk.StringVar()
        super().__init__(padre)
        
    #Ahora viene el Widget específico de la ventana
    def construir(self):
        ttk.Label(self.frame, text="Escribe tu nombre:").pack(anchor="w")
        
        entrada = ttk.Entry(self.frame, textvariable=self.nombre_var)
        entrada.pack(fill="x", pady=5)
        entrada.focus()
        entrada.bind("<Return>", lambda e: self.saludar())
        
        ttk.Button(
            self.frame, text="Saludar", command=self.saludar
        ).pack(pady=5)
        
    #Hacemos el callback(Llamado/referencia) a si mismo
    def saludar(self):
        nombre = self.nombre_var.get().strip()
        if nombre:
            messagebox.showinfo("Saludo", f"¡Hola, {nombre}!", parent=self)
        else:
            messagebox.showwarning("Falta nombre", "Escribe algo.", parent=self)