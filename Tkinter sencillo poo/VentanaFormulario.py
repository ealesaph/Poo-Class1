import tkinter as tk
from tkinter import ttk, messagebox

from BaseVentana import BaseVentana

class VentanaFormulario(BaseVentana):
    #Formulario simple: nombre, email, edad. Con validación básica.
    
    TITULO = "Formulario"
    ANCHO = 360
    ALTO = 260
    
    def __init__(self, padre):
        # Variables de control (una por campo)
        self.nombre_var = tk.StringVar()
        self.email_var  = tk.StringVar()
        self.edad_var   = tk.StringVar()
        super().__init__(padre)
    
    def construir(self):
        # --- Campo: nombre ---
        ttk.Label(self.frame, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(self.frame, textvariable=self.nombre_var, width=25).grid(row=0, column=1, pady=5)
        
        # --- Campo: email ---
        ttk.Label(self.frame, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(self.frame, textvariable=self.email_var, width=25).grid(row=1, column=1, pady=5)
        
        # --- Campo: edad ---
        ttk.Label(self.frame, text="Edad:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(self.frame, textvariable=self.edad_var, width=25).grid(row=2, column=1, pady=5)
        
        # --- Botón guardar ---
        ttk.Button(
            self.frame, text="Guardar", command=self.guardar
        ).grid(row=3, column=0, columnspan=2, pady=10)
    
    # --- Callback principal ---
    def guardar(self):
        datos = self.obtener_datos()
        
        # Validamos antes de "guardar"
        error = self.validar(datos)
        if error:
            messagebox.showwarning("Datos inválidos", error, parent=self)
            return
        
        # Aquí MÁS ADELANTE llamaremos a la BD.
        # Por ahora, solo mostramos los datos.
        messagebox.showinfo(
            "Datos recibidos",
            f"Nombre: {datos['nombre']}\n"
            f"Email: {datos['email']}\n"
            f"Edad: {datos['edad']}",
            parent=self
        )
        self.limpiar()
    
    # --- Métodos auxiliares ---
    def obtener_datos(self):
        """Devuelve un dict con los valores del formulario."""
        return {
            "nombre": self.nombre_var.get().strip(),
            "email":  self.email_var.get().strip(),
            "edad":   self.edad_var.get().strip(),
        }
    
    def validar(self, datos):
        """Devuelve None si todo OK, o un mensaje de error."""
        if not datos["nombre"]:
            return "El nombre no puede estar vacío."
        if not datos["email"]:
            return "El email no puede estar vacío."
        if "@" not in datos["email"]:
            return "El email no parece válido."
        if not datos["edad"].isdigit():
            return "La edad debe ser un número."
        return None
    
    def limpiar(self):
        """Vacía los campos del formulario."""
        self.nombre_var.set("")
        self.email_var.set("")
        self.edad_var.set("")