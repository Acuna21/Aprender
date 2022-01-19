#ERRORES
"""Errores
1. Errores por el programador más comunes
#Sintaxis
#Semanticos

2. Errores por el usuario
"""

#EXCEPCIONES
"""
Tener en cuenta las excepciones para el usuario, cuando vaya a usar el programa
"""
while True:  
     try:
          numero=int(input("Ingrese un numero: "))
          print(f"La suma es: {numero+10}")
     except:
          print("Ingreso un valor incorrecto")
     else:  #Se ejecuta si no hay excepciones
          print("Programa terminado")
          break
     finally: #Se ejecuta siempre
          print("Iteracion finalizada")