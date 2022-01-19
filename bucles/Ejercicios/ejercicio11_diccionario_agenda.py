#Ejercicio11
'''Ejercicio 11:
Hacer un programa que simule una agenda de contactos. Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono, el programa tendrá el siguiente menú de opciones:
1. Nuevo contacto
2. Borrar contacto
3. Ver contactos existentes
4. Salir
'''
diccionario_agenda={}
opcion=0
while(True):
    print()
    print("..MENÚ..")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    print("----------------------------")
    opcion=int(input("Que operacion desea realizar:\n"))
    print()
    if opcion==1:
        nombre=(input("Ingrese el nombre del contacto: "))
        telefono=input("Ingrese el telefono del contacto: ")
        if nombre not in diccionario_agenda:
            diccionario_agenda[nombre]= telefono
            print("Contacto agregado con éxito")
        else:
            print("El nombre de contacto ya existe.Intentelo nuevamente")
    elif opcion==2: 
        nombre_a_borrar=(input("Ingrese el nombre del contacto que desea borrar: "))

        if nombre_a_borrar in diccionario_agenda:
            del(diccionario_agenda[nombre_a_borrar])
            print("Contacto eliminado")
        else:
            print("El contacto no existe en la genda")
    elif opcion==3:
        print(f"Agenda de contactos ")
        for clave, valor in diccionario_agenda.items():
            print(f"Nombre:{clave}, Telefono: {valor}")
    elif opcion==4:
        print("Ha finalizado el programa. Gracias por utilizar la agenda de contactos")
        break
    else:
        print("Se equivoco de opcion, elija una correcta")




    
