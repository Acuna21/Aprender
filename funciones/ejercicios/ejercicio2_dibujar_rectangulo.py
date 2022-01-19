#Ejercicio 2
"""
Ejercicio 2: Hacer un programa que pida la anchura y altura de un
rectángulo y con ayuda de una función lo dibuje con *.
"""
#Mis funciones
def dibujar(ancho,altura):
    for i in range(altura):
        for j in range (ancho):
            print(" *", end="")
        print()
ancho=int(input("Ingrese la anchura del rectangulo: "))
altura=int(input("Ingrese la altura del rectangulo: "))
dibujar(ancho,altura)
