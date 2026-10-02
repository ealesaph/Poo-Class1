from Empresa import Empresa
from EmpleadoFijo import EmpleadoFijo
from EmpleadoHoras import EmpleadoPorHoras
from Gerente import Gerente

def pedir_texto(mensaje):
    """Pide un texto no vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("No puede estar vacío.")
        
def pedir_float(mensaje, minimo=0):
    """Pide un número decimal >= minimo."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < minimo:
                print(f"   Debe ser >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("  Introduce un número válido.")


def pedir_int(mensaje, minimo=0):
    """Pide un número entero >= minimo."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"  Debe ser >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("  Introduce un número entero.")


# ---------------------------------------------------------
#  Opciones del menú
# ---------------------------------------------------------
def agregar_fijo(empresa):
    print("\n--- Nuevo empleado fijo ---")
    nombre = pedir_texto("Nombre: ")
    salario = pedir_float("Salario base: ")
    bonus = pedir_float("Bonus (0 si no hay): ")
    empresa.agregar(EmpleadoFijo(nombre, salario, bonus))
    print(f" {nombre} agregado como EmpleadoFijo.")


def agregar_horas(empresa):
    print("\n--- Nuevo empleado por horas ---")
    nombre = pedir_texto("Nombre: ")
    tarifa = pedir_float("Tarifa por hora: ")
    horas = pedir_int("Horas trabajadas: ")
    empresa.agregar(EmpleadoPorHoras(nombre, tarifa, horas))
    print(f" {nombre} agregado como EmpleadoPorHoras.")


def agregar_gerente(empresa):
    print("\n--- Nuevo gerente ---")
    nombre = pedir_texto("Nombre: ")
    salario = pedir_float("Salario base: ")
    bonus = pedir_float("Bonus (0 si no hay): ")
    empresa.agregar(Gerente(nombre, salario, bonus))
    print(f" {nombre} agregado como Gerente.")


def listar_empleados(empresa):
    print(f"\n--- Empleados de {empresa.nombre} ---")
    if not empresa.listar():
        print("  (No hay empleados)")
        return
    for i, emp in enumerate(empresa.listar(), start=1):
        print(f"  {i}. {emp}")


def mostrar_nomina(empresa):
    print(f"\n--- Nómina total de {empresa.nombre} ---")
    print(f"  Total: ${empresa.nomina_total():.2f}")


def buscar_empleado(empresa):
    print("\n--- Buscar empleado ---")
    nombre = pedir_texto("Nombre a buscar: ")
    emp = empresa.buscar(nombre)
    if emp:
        print(f" Encontrado: {emp}")
    else:
        print(" No se encontró ningún empleado con ese nombre.")


# ---------------------------------------------------------
#  Bucle principal del menú
# ---------------------------------------------------------
def mostrar_menu():
    print("""
╔════════════════════════════════════╗
║   SISTEMA DE EMPLEADOS             ║
╠════════════════════════════════════╣
║  1. Agregar empleado fijo          ║
║  2. Agregar empleado por horas     ║
║  3. Agregar gerente                ║
║  4. Listar empleados               ║
║  5. Buscar empleado                ║
║  6. Mostrar nómina total           ║
║  0. Salir                          ║
╚════════════════════════════════════╝""")


def ejecutar_menu():
    """Bucle principal. Crea la empresa y despacha opciones."""
    empresa = Empresa("Acme S.A.")

    opciones = {
        "1": agregar_fijo,
        "2": agregar_horas,
        "3": agregar_gerente,
        "4": listar_empleados,
        "5": buscar_empleado,
        "6": mostrar_nomina,
    }

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "0":
            print("\n¡Hasta luego!")
            break

        accion = opciones.get(opcion)
        if accion is None:
            print("  Opción no válida.")
            continue

        accion(empresa)
        input("\nPulsa Enter para continuar...")