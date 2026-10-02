import tkinter as tk
from tkinter import ttk

from VentanaCalculadora import VentanaCalculadora

class Aplicacion(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Mi Aplicación")
        self.geometry("420x340")
        self.resizable(False, False)
        
        self.construir()
        self.centrar()
    
    def construir(self):
        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)
        
        ttk.Label(
            frame, text="Menú principal",
            font=("Arial", 16, "bold")
        ).pack(pady=(0, 20))
        
        ttk.Button(
            frame, text="Calculadora",
            command=lambda: VentanaCalculadora(self)
        ).pack(fill="x", pady=5)
        
        ttk.Button(
            frame, text="Salir",
            command=self.destroy
        ).pack(fill="x", pady=(20, 0))
    
    def centrar(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - self.winfo_width())  // 2
        y = (self.winfo_screenheight() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")