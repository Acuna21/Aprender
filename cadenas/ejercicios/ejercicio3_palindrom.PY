cadena=input("Ingrese una cadena: ")
#Convertir minuscula
cadena=cadena.lower()
#Quitar espacios
cadena=cadena.replace(" ","")

#Invertir cadena
cadena_inver=cadena[::-1]

if cadena==cadena_inver:
    print("La cadena es un palindrome")
else:
    print("La cadena N0 es un palindrome")