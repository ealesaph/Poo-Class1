import tkinter as tk
from tkinter import ttk, messagebox

from BaseVentana import BaseVentana

class VentanaCalculadora(BaseVentana):
    TITULO = 'Calculadora'
    ANCHO = 320
    ALTO = 420
    
    def __init__(self, padre):
            # --- Estado de la calculadora ---
            # Guardamos el "número actual" como StringVar para mostrarlo en pantalla
            self.pantalla_var = tk.StringVar(value="0")
            
            # Estado interno de la operación
            self.operador = None        # '+', '-', '*', '/' o None
            self.operando = None        # Primer número (float) o None
            self.nuevo_numero = True    # ¿El próximo dígito empieza un número nuevo?
            
            super().__init__(padre)
        
        # ---------------------------------------------------------
        #  Construcción de la UI
        # ---------------------------------------------------------
    def construir(self):
        # --- Pantalla (Entry de solo lectura) ---
        pantalla = ttk.Entry(
            self.frame,
            textvariable=self.pantalla_var,
            font=("Arial", 20, "bold"),
            justify="right",
            state="readonly"     # El usuario NO puede escribir directamente
        )
        pantalla.pack(fill="x", pady=(0, 10), ipady=8)
        
        # --- Rejilla de botones ---
        botones = ttk.Frame(self.frame)
        botones.pack(fill="both", expand=True)
        
        # Distribución de botones: (texto, fila, columna, colspan)
        layout = [
            ("C",  0, 0, 1), ("←", 0, 1, 1), ("÷", 0, 2, 1), ("×", 0, 3, 1),
            ("7",  1, 0, 1), ("8", 1, 1, 1), ("9", 1, 2, 1), ("-", 1, 3, 1),
            ("4",  2, 0, 1), ("5", 2, 1, 1), ("6", 2, 2, 1), ("+", 2, 3, 1),
            ("1",  3, 0, 1), ("2", 3, 1, 1), ("3", 3, 2, 1), ("=", 3, 3, 2),
            ("0",  4, 0, 2), (".", 4, 2, 1),
        ]
        
        for texto, fila, col, span in layout:
            self.crear_boton(botones, texto, fila, col, span)
        
        # Configurar expansión de la rejilla
        for i in range(5):
            botones.rowconfigure(i, weight=1)
        for j in range(4):
            botones.columnconfigure(j, weight=1)
    
    def crear_boton(self, contenedor, texto, fila, col, colspan):
        #Crea un botón y lo conecta a la acción correcta.
        boton = ttk.Button(
            contenedor,
            text=texto,
            command=lambda t=texto: self.al_pulsar(t)
        )
        boton.grid(
            row=fila, column=col, columnspan=colspan,
            sticky="nsew", padx=2, pady=2
        )
    
    # ---------------------------------------------------------
    #  Manejo de pulsaciones (enrutador)
    # ---------------------------------------------------------
    def al_pulsar(self, tecla):
        #Enruta la tecla pulsada al método correspondiente.
        if tecla.isdigit():
            self.agregar_digito(tecla)
        elif tecla == ".":
            self.agregar_punto()
        elif tecla in ("+", "-", "×", "÷"):
            self.elegir_operador(tecla)
        elif tecla == "=":
            self.calcular()
        elif tecla == "C":
            self.limpiar_todo()
        elif tecla == "←":
            self.borrar_ultimo()
    
    # ---------------------------------------------------------
    #  Lógica de la calculadora
    # ---------------------------------------------------------
    def agregar_digito(self, digito):
        #Añade un dígito al número que estamos escribiendo.
        actual = self.pantalla_var.get()
        
        if self.nuevo_numero:
            # Empezamos un número nuevo
            self.pantalla_var.set(digito)
            self.nuevo_numero = False
        else:
            # Continuamos el número actual (evitando "0" a la izquierda)
            if actual == "0":
                self.pantalla_var.set(digito)
            else:
                self.pantalla_var.set(actual + digito)
    
    def agregar_punto(self):
        #Añade el separador decimal si no existe ya.
        actual = self.pantalla_var.get()
        
        if self.nuevo_numero:
            self.pantalla_var.set("0.")
            self.nuevo_numero = False
        elif "." not in actual:
            self.pantalla_var.set(actual + ".")
    
    def elegir_operador(self, op):
        #Guarda el operando y el operador pendiente.
        # Si ya había un operador pendiente y el usuario NO ha escrito
        # un número nuevo, solo cambiamos el operador
        if not self.nuevo_numero:
            # Calculamos el resultado pendiente si ya había operación
            if self.operador is not None and self.operando is not None:
                self.calcular()
            
            self.operando = float(self.pantalla_var.get())
        
        self.operador = op
        self.nuevo_numero = True   # El próximo dígito empieza número nuevo
    
    def calcular(self):
        #Ejecuta la operación pendiente y muestra el resultado.
        if self.operador is None or self.operando is None:
            return   # No hay nada que calcular
        
        try:
            segundo = float(self.pantalla_var.get())
        except ValueError:
            return   # La pantalla no tiene un número válido
        
        try:
            resultado = self._operar(self.operando, segundo, self.operador)
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir por cero.", parent=self)
            self.limpiar_todo()
            return
        
        # Mostramos el resultado sin ".0" si es entero
        self.pantalla_var.set(self._formatear(resultado))
        
        # Reiniciamos el estado
        self.operando = None
        self.operador = None
        self.nuevo_numero = True
    
    def _operar(self, a, b, op):
        #Realiza la operación matemática. Separado para poder testearlo.
        if op == "+": return a + b
        if op == "-": return a - b
        if op == "×": return a * b
        if op == "÷":
            if b == 0:
                raise ZeroDivisionError
            return a / b
        raise ValueError(f"Operador desconocido: {op}")
    
    def _formatear(self, numero):
        #Devuelve un string sin .0 innecesario.
        if numero == int(numero):
            return str(int(numero))
        return str(numero)
    
    # ---------------------------------------------------------
    #  Utilidades
    # ---------------------------------------------------------
    def limpiar_todo(self):
        #Resetea todo el estado de la calculadora.
        self.pantalla_var.set("0")
        self.operador = None
        self.operando = None
        self.nuevo_numero = True
    
    def borrar_ultimo(self):
        #Borra el último carácter del número actual.
        actual = self.pantalla_var.get()
        
        if self.nuevo_numero:
            return   # No borramos si estamos empezando un número nuevo
        
        if len(actual) <= 1 or (len(actual) == 2 and actual.startswith("-")):
            self.pantalla_var.set("0")
            self.nuevo_numero = True
        else:
            self.pantalla_var.set(actual[:-1])