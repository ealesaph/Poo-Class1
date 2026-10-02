import tkinter as tk
from tkinter import ttk

class BaseVentana(tk.Toplevel):
    TITULO = 'Ventana'
    ANCHO = 300
    ALTO = 200
    
    def __init__(self, padre):
        super().__init__(padre)
        self.padre = padre
        
        # Configuración común
        self.title(self.TITULO)
        self.geometry(f"{self.ANCHO}x{self.ALTO}")
        self.resizable(False, False)
        self.transient(padre)
        
        # Frame principal donde vivirán los widgets
        self.frame = ttk.Frame(self, padding=15)
        self.frame.pack(fill="both", expand=True)
        
        # Método que las subclases SOBRESCRIBEN
        self.construir()
        
        # Pie común: botón cerrar
        ttk.Button(
            self.frame, text="Cerrar", command=self.destroy
        ).pack(side="bottom", pady=(10, 0))
        
        # Centrar respecto al padre
        self.centrar()
        
        #Hook para que las subclases implementen sus Widgets
        def construir(self):
            pass #Para que las subclases lo sobrescriben
        
        def centrar(self):
        # Utilidad Heredable (Para Centrar la ventan respecto a su padre.)
            self.update_idletasks()
            x = self.padre.winfo_x() + (self.padre.winfo_width()  - self.ANCHO) // 2
            y = self.padre.winfo_y() + (self.padre.winfo_height() - self.ALTO)  // 2
            self.geometry(f"{self.ANCHO}x{self.ALTO}+{x}+{y}")