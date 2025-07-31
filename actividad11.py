propietarios ={}
cantidad_propietarios=int(input("¿Cuantos propietarios desea ingresar?: "))
for i in range(cantidad_propietarios):
    print(f"\nPropietario {i+1}")
    NIT = int(input("Ingrese numero de NIT"))
    nombre= input("Ingrese nombre completo del propietario: ")
    telefono= input("Ingrese numero de contacto: ")
    cantidad_vehiculos= int(input("Ingrese cantidad de vehiculos que posee: "))
    for j in range(cantidad_vehiculos):
        placa = input("Ingrese numero de placa del vehiculo: ")
        marca= input("Ingrese marca del vehiculo: ")
        modelo = input("Ingrese modelo del vehiculo: ")
        año = int(input("Ingrese año del vehiculo: "))
        impuesto_pagado = input("¿Pagó el impuesto (Si/No)?: ").lower()
    propietarios[NIT]= {
        "nombre": nombre,
        "telefono": telefono,
        "vehiculos": [
            {
                "placa": placa,
                "marca": marca,
                "modelo": modelo,
                "año": año,
                "impuesto pagado": impuesto_pagado
            }
        ]
    }
