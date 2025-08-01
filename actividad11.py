propietarios ={}
cantidad_propietarios=int(input("¿Cuantos propietarios desea ingresar?: "))
for i in range(cantidad_propietarios):
    print(f"\nPropietario {i+1}")
    nit = input("Ingrese numero de NIT: ")
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
        impuesto = input("¿Pagó el impuesto (Si/No)?: ").lower()
        vehiculos[placa]={
            "marca": marca,
            "modelo": modelo,
            "año": año,
            "impuesto": impuesto
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
buscar_nit= input("\nIngrese el nit del propietario a buscar: ")
if buscar_nit in propietarios:
    print(f"Nombre: {propietarios[buscar_nit]["nombre"]}")
    print(f"Telefono: {propietarios[buscar_nit]["telefono"]}")
    for placa, data in propietarios[buscar_nit]["vehiculos"].items():
        print(f"-Placa: {placa}|{data["marca"]} {data["modelo"]}({data["año"]})|Impuesto: {data["impuesto"]}")
else:
    print("Nit no encontrado.")
pagados=0
no_pagados=0
for datos in propietarios.values():
    for i in datos["vehiculos"].values():
        if i["impuesto"] in ["si","sí"]:
            pagados+=1
        else:
            no_pagados+=1
print(f"\nVehiculos con impuesto pagado: {pagados}")
print(f"Vehiculos sin el impuesto pagado: {no_pagados}")