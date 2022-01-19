#Ejercicio 7, juego
import random 
aleatorio=random.randint(0,100)
aux=False
contador=0
while True:
    numero=int(input("Ingrese el número: "))
    contador+=1
    if numero>aleatorio:
        print("No es el número. Digita un numero menor")
    elif numero<aleatorio:
        print("No es el número. Digita un numero mayor")
    else:
        print("Número adivinado. Ha acertado.¡Felicidades!")
        break
print(f"Cantidad de intentos: {contador}")