#Ejercicio 4
inicio=int(input("Ingrese el número desde donde quiere sumar: "))
final=int(input("Ingrese el número hasta donde quiere llegar sumar: "))
suma=0
for i in range (inicio,final+1):
    if i%2==0:
        suma=suma+i
print(f"La suma de numeros pares dentro del rango es: {suma}")