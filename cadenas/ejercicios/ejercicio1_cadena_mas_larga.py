#Ejercicio 1--Cadena más larga
cadena1=input("Ingrese una cadena: ")
cadena2=input("Ingrese una cadena: ")
longitud1=len(cadena1)
longitud2=len(cadena2)
if longitud1>longitud2:
    print(f"La cadena más larga es: {cadena1}")
elif longitud2>longitud1:
    print(f"La cadena más larga es: {cadena2}")
else:
    print("Ambas cadenas son iguales en longitud")
