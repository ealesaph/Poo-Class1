import tkinter as tk
from tkinter import ttk

class BaseVentana(tk.Toplevel):
    #Clase base para todas las ventanas secundarias.
    
    TITULO = "Ventana"
    ANCHO = 300
    ALTO = 200
    
    def __init__(self, padre):
        super().__init__(padre)
        self.padre = padre
        
        self.title(self.TITULO)
        self.geometry(f"{self.ANCHO}x{self.ALTO}")
        self.resizable(False, False)
        self.transient(padre)
        
        self.frame = ttk.Frame(self, padding=15)
        self.frame.pack(fill="both", expand=True)
        
        self.construir()   # hook que sobrescriben las subclases
        
        ttk.Button(
            self.frame, text="Cerrar", command=self.destroy
        ).pack(side="bottom", pady=(10, 0))
        
        self.centrar()
    
    def construir(self):
        pass   # opcional para las subclases
    
    def centrar(self):
        self.update_idletasks()
        x = self.padre.winfo_x() + (self.padre.winfo_width()  - self.ANCHO) // 2
        y = self.padre.winfo_y() + (self.padre.winfo_height() - self.ALTO)  // 2
        self.geometry(f"{self.ANCHO}x{self.ALTO}+{x}+{y}")