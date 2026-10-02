from tkinter import ttk
from BaseVentana import BaseVentana

class VentanaContador(BaseVentana):
    #Un contador sencillo con botones +1, -1 y un reseteo del contador
    TITULO = 'Contador'
    ANCHO = 260
    ALTO = 220
    
    def __init__(self, padre):
        self.contador = 0
        super().__init__(padre)
        
    def construir(self):
        # La etiqueta grande para que muestre el valor
        self.label = ttk.Label(
            self.frame, text='0', font=(
                'Arial',
                32,
                'bold'
            )
        )
        self.label.pack(pady=10)
        
        # Frame con los botones
        botones = ttk.Frame(self.frame)
        botones.pack()
        
        ttk.Button(botones, text="+1",   command=self.incrementar).grid(row=0, column=0, padx=3)
        ttk.Button(botones, text="-1",   command=self.decrementar).grid(row=0, column=1, padx=3)
        ttk.Button(botones, text="Reset", command=self.resetear).grid(row=0, column=2, padx=3)
        
    # --- Método auxiliar (DRY) ---
    def actualizar(self):
        self.label.config(text=str(self.contador))
        
        # --- Callbacks ---
    def incrementar(self):
        self.contador += 1
        self.actualizar()
    
    def decrementar(self):
        self.contador -= 1
        self.actualizar()
    
    def resetear(self):
        self.contador = 0
        self.actualizar()
    
    