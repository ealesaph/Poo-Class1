class Empleado:
    
    def __init__(self, nombre = '', salario_base = 0):
        self.nombre = nombre
        self.salario_base = salario_base
        
    def calcular_salario(self):
        #Metodo que sobreescribiremos en las subclases.
        return self.salario_base
    
    def tipo(self):
        #Devuelve el nombre de la clase real (util para mostrar)
        return self.__class__.__name__
    
    def __str__(self):
        return (f'{self.nombre} ({self.tipo()}) -'
                f'${self.calcular_salario():.2f}')