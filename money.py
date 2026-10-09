while True:
    saldo = 100
    historial = []
    while saldo > 10:
        print( "usted puede ... revisar su saldo, extraer dinero , ingresar dinero")
        que_deseas = int(input("que accion desea realisar "))


        if que_deseas == 1: 
            print("usted selecciono observar su saldo")
            print(saldo)
            historial.append("revisar su saldo")
            print(historial)
            

        if que_deseas == 2: 
            historial.append("Extraer dinero")
            print(historial)
            historial = ["retirar dinero"]
            print("usted selecciono extraer dinero")
            seleccionar_dinero = int(input("coloque la cantidad de dinero que desea extraer"))
            print("esta es la cantidad de dinero que extrallo " + str(seleccionar_dinero))
            saldo = saldo - seleccionar_dinero
            print("esta es la cantidad de dinero que le queda" + str(saldo))
        elif saldo == 10:
           print("lo sentimos se gasto toda su plata consiga chamba")

        if que_deseas == 3:
            historial.append("Ingresar dinero")
            print(historial)
            historial = ["ingresar dinero"]
            print("usted selecciono ingresar dinero a su saldo")
            ingresar_dinero = int(input("coloque la cantidad de dinero que desea agregar"))
            print("esta es la cantidad de dinero que agrego a su saldo" + str(ingresar_dinero))
            saldo = saldo + ingresar_dinero
            print("esta es la cantidad de dinero que hay en su saldo " + str(saldo))

    reiniciar = int(input("usted desea reiniciar?")) 
    if reiniciar == 1:
        print("usted elijio reiniciar")
        break 