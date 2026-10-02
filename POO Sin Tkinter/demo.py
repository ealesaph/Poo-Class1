from CuentaBancaria import CuentaBancaria

def demo_basica():
    
    print("=== Demo básica ===")
    cuenta = CuentaBancaria("Ana", 100)
    print(cuenta)                      # Cuenta de Ana: $100.00

    cuenta.depositar(50)
    print(cuenta)                      # Cuenta de Ana: $150.00

    cuenta.retirar(30)
    print(cuenta)                      # Cuenta de Ana: $120.00

    print(f"Saldo consultado: ${cuenta.consultar_saldo():.2f}")
    print()
    
def demo_errores():
    
    print("=== Demo de errores ===")
    cuenta = CuentaBancaria("Luis", 50)

    intentos = [
        ("Depositar -10",  lambda: cuenta.depositar(-10)),
        ("Retirar 1000",   lambda: cuenta.retirar(1000)),
        ("Retirar -5",     lambda: cuenta.retirar(-5)),
    ]

    for descripcion, accion in intentos:
        try:
            accion()
            print(f"{descripcion}: NO lanzó error")
        except ValueError as e:
            print(f"{descripcion}: {e}")
    print()
    
def demo_multiple():

    print("=== Demo con varias cuentas ===")
    cuentas = [
        CuentaBancaria("Ana",   100),
        CuentaBancaria("Luis",  200),
        CuentaBancaria("Marta", 0),
    ]

    cuentas[0].depositar(50)
    cuentas[1].retirar(80)
    cuentas[2].depositar(500)

    for c in cuentas:
        print(c)
    print()
    
def ejecutar_demo():
    
    demo_basica()
    demo_errores()
    demo_multiple()
    
if __name__ == "__main__":
    ejecutar_demo()