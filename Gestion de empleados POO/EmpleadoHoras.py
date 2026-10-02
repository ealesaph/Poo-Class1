from Empleado import Empleado

class EmpleadoPorHoras(Empleado):
    #Empleado por Boleta
    def __init__(self, nombre='', tarifa_hora = 50000, horas_trabajadas = 0):
        super().__init__(nombre, salario_base = 0)
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas
        
    def calcular_salario(self):
        return self.tarifa_hora * self.horas_trabajadas