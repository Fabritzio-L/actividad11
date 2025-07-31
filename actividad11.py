propietarios ={}
cantidad_propietarios=int(input("¿Cuantos propietarios desea ingresar?: "))
for i in range(cantidad_propietarios):
    print(f"\nPropietario {i+1}")
    nit = int(input("Ingrese numero de NIT: "))
    nombre= input("Ingrese nombre completo del propietario: ")
    telefono= input("Ingrese numero de contacto: ")
    cantidad_vehiculos= int(input("Ingrese cantidad de vehiculos que posee: "))
    vehiculos={}
    for j in range(cantidad_vehiculos):
        print(f"\nVehiculo #{j+1}")
        placa = input("Ingrese numero de placa del vehiculo: ").upper()
        marca= input("Ingrese marca del vehiculo: ")
        modelo = input("Ingrese modelo del vehiculo: ")
        año = int(input("Ingrese año del vehiculo: "))
        impuesto_pagado = input("¿Pagó el impuesto (Si/No)?: ").lower()
        vehiculos[placa]={
            "marca": marca,
            "modelo": modelo,
            "año": año,
            "impuesto": impuesto_pagado
        }
    propietarios[nit]= {
        "nombre": nombre,
        "telefono": telefono,
        "vehiculos":vehiculos
    }
print("\nRegistro de propietarios y sus vehiculos")
for nit, datos in propietarios.items():
    print(f"\nNIT: {nit}")
    print(f"Nombre: {datos["nombre"]}")
    print(f"Numero de contacto: {datos["telefono"]}")
    print("\nVehiculos")
    for placa, data in datos["vehiculos"].items():
        print(f"-Placa: {placa}|{data["marca"]} {data["modelo"]}({data["año"]})|Impuesto: {data["impuesto"]}")

