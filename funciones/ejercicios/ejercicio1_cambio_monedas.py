#ejercicio 1
'''
Ejercicio 1: Desarrollar un programa que pueda calcular el valor del tipo
de cambio de moneda (de tu moneda – hacia dólar y viceversa).
'''

#Mis funciones
def convertir_de_cop_a_dolares(cop):
    return cop/4,300
def convertir_de_dolares_a_cop(dolar):
    return 4,300*dolar

while True:
    print("""..Menu...
1. Convertir de Cop a dólares
2. Convertir de dólares a cop
3. Salir""")
    opcion=int(input("Ingrese la operación que desea realizar: "))
    print()
    if opcion==1:
        cop=float(input("Ingrese la cantidad de pesos colombianos que desea convertir: "))
        print(f"Dólares--> ${convertir_de_cop_a_dolares(cop)}")
    elif opcion==2:
        dolar=float(input("Ingrese la cantidad de dolares  que desea convertir a pesos colombianos: "))
        print(f"Pesos colombianos--> ${convertir_de_dolares_a_cop(dolar)}")
    elif opcion==3:
        print("Fin del programa")
        break
    else:
        print("Escoja una opcion valida")
        print()
        




