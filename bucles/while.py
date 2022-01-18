#Bucle while
import math
numero=int(input("Ingrese un número: "))

while(numero<0):
    numero=int(input("Ingrese nuevamente un número. Recuerde que debe ser positivo: "))
print(f"\n Su raiz cuadrada es: {(math.sqrt(numero)):.2f}")
