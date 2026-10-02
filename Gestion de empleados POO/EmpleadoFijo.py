from Empleado import Empleado

class EmpleadoFijo(Empleado):
    # Crearemos un empleado con salario Base y un Bonus
    
    def __init__(self, nombre='', salario_base=0, bonus = 0):
        super().__init__(nombre, salario_base) # Acá Llamamos al padre
        self.bonus = bonus
        
    def calcular_salario(self):
        return self.salario_base + self.bonus
        
    #Heredamos el metodo __str__ tal cual así que no hay que escribirlo siempre