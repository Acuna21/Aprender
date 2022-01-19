'''
Ejercicio 3:
Crear un programa que tenga una lista de clientes, cada cliente tiene su
Nombre, Apellido y DNI. El programa tendrá el siguiente menú de opciones:
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar cliente por DNI
4. Eliminar cliente
5. Salir
PD: Cada opción de menú se realizará con una función
'''

clientes=[]  #Lista de clientes

#Mis funciones
def agregar_cliente(clientes,nombre,apellido,DNI):
    diccionario_cliente={}
    diccionario_cliente["Nombre"]=nombre
    diccionario_cliente["Apellido"]=apellido
    diccionario_cliente["DNI"]=DNI
    clientes.append(diccionario_cliente)
def mostrar_cliente(clientes):
    for i in clientes:
        print(f"Nombre: {i['Nombre']}, Apellido: {i['Apellido']}, DNI: {i['DNI']}")
def mostrar_cliente_por_DNI(clientes, DNI):
    for i in clientes:
        if i['DNI']==DNI:
            print(f"Nombre: {i['Nombre']}, Apellido: {i['Apellido']}, DNI: {i['DNI']}")
            return True
        else:
            return False
def eliminar_cliente (clientes, DNI):
    for i in clientes:
        if i['DNI']==DNI:
            clientes.remove(i)
            return True
        else:
            return False

while True:
    print("""...Menú...
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar cliente por DNI
4. Eliminar cliente
5. Salir""")
    print()
    opcion=int(input("Que operacion desea realizar:\n"))
    print()
    if opcion==1:
        nombre=(input("Ingrese el nombre del cliente: "))
        apellido=(input("Ingrese el apellido del cliente: "))
        DNI=input("Ingrese el DNI del cliente: ")
        agregar_cliente(clientes,nombre,apellido,DNI)
        print("Cliente agregado")
        print()
    elif opcion==2: 
        mostrar_cliente(clientes)
    elif opcion==3:
        DNI=input("Ingrese el DNI del cliente que desea buscar: ")
        if mostrar_cliente_por_DNI(clientes, DNI):
            print("Cliente encontrado")
        else:
             print("Cliente no encontrado")
    elif opcion==4:
        DNI=input("Ingrese el DNI del cliente que desea eliminar: ")
        if eliminar_cliente(clientes, DNI):
            print("Cliente eliminado")
            print()
        else:
             print("El cliente no existe")
             print()       
    elif opcion==5:
        print("Ha fianlizado del programa")
        break
    else:
        print("Por favor, elija una opcion correcta")
        print()


        


        