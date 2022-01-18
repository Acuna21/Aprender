#Hacer un programa que pída 3 numeros determine cual es el mayor
mayor=0
numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese un numero: "))
numero3=int(input("Ingrese un numero: "))

if numero1>numero2 and numero1>numero3:
    print(f"El número mayor es {numero1}")
elif numero2>numero1 and numero2>numero3:
    print(f"El número mayor es {numero2}")
else: 
    print(f"El número mayor es {numero3}")
