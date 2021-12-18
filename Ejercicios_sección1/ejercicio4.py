from math import pi
#Ejercico 4:Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la circunferencia.
radio=int(input("Ingrese el radio del circulo: "))
area=pi*(radio**2)
longitud=2*pi*radio
print(f"Su área es {area:.2f} y su longitud es {longitud:.2}")