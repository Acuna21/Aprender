#Hacer un programa que pída un caracter e indique si es una vocal o no
caracter=str(input("Ingrese un caracter: "))
caracter=caracter.lower()
 
if caracter=="o" or caracter=="a" or caracter=="e" or caracter=="i" or caracter=="u":
    print("El caracter ingresado es una vocal")
else:
    print("El caracter ingresado es una consonante")
