clientes = {}
pagos = {}


def datos_inquilino():
    cedula = input("ingresa tu cedula: ")
    nombre = input("ingresa tu nombre: ")
    apellido = input("ingresa tu apellido: ")
    monto_ingreso = int(input("ingrese el monto de su salario fijo: "))
    costo_departamento = int(input("ingrese el costo del apartamento que es de su interes: "))
    costo_mantenimiento = int(input("ingrese el costo del mantenimiento del apartamento de su interes: "))
    interesado = [cedula, nombre, apellido, monto_ingreso, costo_departamento, costo_mantenimiento]
    return interesado



while True:
    menu = input("""Bienvenido a nuestro programa de control de condominios:
        seleccione una de las opciones existentes:
    
        1. añadir un cliente
        2. realizar pagos
        3. salir
        :
        """)
    
        
    if menu == "1":
        interesado = datos_inquilino()
        if interesado[3] - interesado[4] < 0:
            print("")
            print("***********************************************************************************************************************************************************************************")
            print("lo siento, no puede adquirir este departamento")
            print("***********************************************************************************************************************************************************************************")
            print("")
        else:
            clientes[interesado[0]] = interesado
            print("")
            print("***********************************************************************************************************************************************************************************")
            print(f"felicidades, se encuentra en la lista de nuevos clientes, debe realizar el deposito de 3 cuotas por adelantado, es decir, su monto de deposito actual es de {interesado[4] * 3}")
            print("***********************************************************************************************************************************************************************************")
            print("")
            
            deudas = [interesado[4], interesado[5]]
            pagos[interesado[0]] = deudas




    elif menu == "2":
        print("")
        print("_ _ _ __ _ _ __ _ _ __ _ _ __ _ _ __ _ _ __ _ _ __ _ _ __ _ _ __ _ _ __ _ _ __ _ _ __ _ _ _")
        cedula_cliente = input("ingresa la cedula del cliente a pagar: ")
        deudas = pagos[cedula_cliente]

        print(f"el inquilino propietario de la cedula {cedula_cliente} debe realizar un pago de {deudas[0]} pesos de alquiler y {deudas[1]} de mantenimiento")

        pago = input("¿el usuario ha pagado lo debido? ingrese 1 para si, o ingrese 0 para no: ")
        if pago == "1":
            print("registrado")
            info_cliente = clientes[cedula_cliente]
            f = open("reportes.txt", "a")
            f.write(f"""El inquilino {info_cliente[1]} {info_cliente[2]} ha pagado su monto de alquiler de {info_cliente[4]} y
su mantenimiento de {info_cliente[5]}.

**************************************************************************************************************************""")
            f.close()
            f = open("pagos.txt", "a")
            f.write(
                f"""inquilino: {info_cliente[1]} {info_cliente[2]} 
                pago alquiler: {info_cliente[4]}
                mantenimiento:{info_cliente[5]}.

            **************************************************************************************************************************""")
            f.close()
        elif pago == "0":
            print("se le cobrara una mora de 1000 pesos en su pago")


    elif menu == "3":
        print("gracias por visitarnos!")
        break

    else:
        print("esto no es una opcion, elija una opcion existente")