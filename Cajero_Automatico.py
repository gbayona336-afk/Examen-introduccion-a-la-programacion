"""
Cajero Automático
"""

#Funcion para consultar saldo
def ConsultarSaldo(saldo):
    print("Su saldo actual es: $", saldo)

#Funcion para depositar dinero
def DepositarDinero(saldo):
    monto = float(input("Ingrese el monto a depositar: "))

    if monto > 0:
        saldo = saldo + monto
        print("Deposito exitoso")
        print("Nuevo saldo $", saldo)
    else:
        print("Error: el monto debe ser mayor que cero")

    return saldo

#Funcion para retirar dinero
def Retirar(saldo):
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Error: el monto debe ser mayor que cero")
    elif monto > saldo:
        print("Error: saldo insuficiente")
    else:
        saldo = saldo - monto
        print("Retiro exitoso")
        print("Nuevo saldo $", saldo)

    return saldo

#Algoritmo Principal
def CajeroAutomatico():

    #Entrada
    saldo = 1000
    opcion = -1

    #Proceso
    while opcion != 0:
        print("\n===== Cajero Automático =====")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("0. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            ConsultarSaldo(saldo)
        elif opcion == 2:
            saldo = DepositarDinero(saldo)
        elif opcion == 3:
            saldo = Retirar(saldo)
        elif opcion == 0:
            print("Gracias por usar el Cajero Automatico")
        else:
            print("Opcion no valida")
    #Salida
    print("Saldo final: $", saldo)

#Ejecutar el Programa
CajeroAutomatico()