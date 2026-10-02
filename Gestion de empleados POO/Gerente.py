from EmpleadoFijo import EmpleadoFijo

class Gerente(EmpleadoFijo):
    #El gerente es el empleado fijo + 20% extra sobre el salario base
    def __init__(self, nombre='', salario_base=0, bonus=0):
        super().__init__(nombre, salario_base, bonus)
    
    def calcular_salario(self):
        base = super().calcular_salario() # Reutilizamos al padre
        return base + 0.20 * self.salario_base