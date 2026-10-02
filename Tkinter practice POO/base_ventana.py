import tkinter as tk
from tkinter import ttk

class BaseVentana(tk.Toplevel):
    # Vamos a definir el Titulo como un Str, Ancho y alto como INT
    TITULO = 'Ventana'
    ANCHO = 300
    ALTO = 200

def __init__(self, padre):
    super().__init__(padre)
    self.padre = padre
    
    #Config Común a TODAS las ventanas
    self.title(self.TITULO)
    self.geometry(f'{self.ANCHO}x{self.ALTO}')
    self.resizable(False, False)
    self.transient(padre)
    
    # PLantilla común: frame principal + zona para contenido + botón cerrar
    self._construir_plantilla()
    
# Métodos 'plantilla'
def _construir_plantilla(self):
    #Frame Principal
    self.frame_principal = ttk.Frame(self, padding=15)
    self.frame_principal.pack(fill='both', expand=True)
    
    #Zona donde las subclases ponen SUS widgets
    self.frame_contenido = ttk.Frame(self.frame_principal)
    self.frame_contenido.pack(fill='both', expand=True)
    
    #Footer corriente con botón cerrar
    self._construir_pie()
    
    #Hook para que las subclases añadan lo suyo
    self._construir_contenido(self.frame_contenido)
    
def _construir_pie(self):
    pie = ttk.Frame(self.frame_principal)
    