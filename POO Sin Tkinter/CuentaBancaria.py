class CuentaBancaria:
    def __init__(self, titular = '', saldo = 0): # Valores Estandar
        self.titular = titular
        self._saldo = saldo #Encapsulamos el saldo para seguridad (Por Convención ponemos un _)
        
    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError('La Cantidad debe ser positiva')
        self._saldo += cantidad
    
    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= cantidad
        
    def consultar_saldo(self):
        return self._saldo

    def __str__(self):
        return f"Cuenta de {self.titular}: ${self._saldo:.2f}"