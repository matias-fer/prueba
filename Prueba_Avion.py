pasajeros = []
pasajes = []
rut = []
nombres = []
ganancias = ("Tipo de asiento", "Cantidad", "Total" )
lista=["A","B","C","D","E","F"]

##################################################################################
def comprar_pasajes():
    try:
        nombre = input("Ingresa tu nombre: ")
        rut_persona = int(input("Ingrese su rut: "))
        rut.append(rut_persona)
        nombres.append(nombre)
        comprar_pasajes = int(input("Cuantos pasajes desea comprar: "))
        for i in range(comprar_pasajes):
            print("1) Asiento Comun, 60.000")
            print("2) Espacio Adicional para piernas, 80.000")
            print("3) No Reclina, 50.000")
            seleccion_asiento=int(input("Selecciona opcion:"))
            pasajes.append(seleccion_asiento)
            print(nombre)
            print(rut)
            print(pasajes)
    except ValueError:
        print("Opcion invalida")
##################################################################################
def ubicaciones():
    for i in range(len(lista)):
        print(lista[i])
        for i in range(len(pasajes)):
            print(pasajes)

##################################################################################
def personas_por_rut():
    for i in range(len(rut)):
        print(rut[i])
    
##################################################################################
def ganancias_totales():
    print(ganancias)
    print("Asiento comun" )


while True:
    try:
        print("1) Comprar Pasajes")
        print("2) Mostrar Ubicaciones")
        print("3) Personas Por RUT")
        print("4) Ganancias")
        print("5) Salir")
        op = int(input("Opcion: "))
        if op==1:
            comprar_pasajes()
        elif op==2:
            ubicaciones()
        elif op==3:
            personas_por_rut()
        elif op==4:
            ganancias_totales()
        elif op==5:
            break
    except ValueError:
        print("Opcion invalida")