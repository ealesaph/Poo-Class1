class Empresa:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar(self, empleado):
        self.empleados.append(empleado)
        
    def listar(self):
        #Devuelve la lista completa.
        return self.empleados

    def nomina_total(self):
        #Suma de todos los salarios.
        return sum(e.calcular_salario() for e in self.empleados)

    def buscar(self, nombre):
        #Busca por nombre (case-insensitive). Devuelve el primero o None.
        for e in self.empleados:
            if e.nombre.lower() == nombre.lower():
                return e
        return None