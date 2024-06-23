deudores = {}

for _ in range(5):
    rut = input("Ingrese el RUT (sin puntos ni guión): ")
    deuda = int(input("Ingrese la cantidad de la deuda:$"))
    deudores[rut] = deuda

print("Deudores:", deudores)

while True:
    rut = input("Ingrese el RUT para abonar (o ingrese 0 para finalizar): ")
    if rut == "0":
        break
    if rut in deudores:
        abono = int(input("Ingrese abono:$"))
        if abono > 0:
            if abono <= deudores[rut]:
                deudores[rut] -= abono
                if deudores[rut] == 0:
                    print("La deuda de",rut,"se pago y se ha eliminado de los deudores.")
                    del deudores[rut]
                else:
                    print("Nuevo saldo de deuda para",rut,"es :$", deudores[rut])
            else:
                print("El abono supera la deuda.")
        else:
            print("El abono debe ser mayor que cero.")
    else:
        print("El RUT ingresado no se encuentra registrado.")

print("Personas que quedaron debiendo y sus deudas a pagar:",deudores)