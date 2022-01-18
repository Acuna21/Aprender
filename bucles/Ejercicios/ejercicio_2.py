'''
Ejercicio 2:
Llenar una lista con los números del 1 al 10, luego modificar los elementos
de la lista multiplicándolos por un valor que el usuario digite.
'''
lista=list(range(1,11))
print(lista)
numero=int(input("Ingrese un número por el cual desea multiplicar la lista: "))
aux=0
for i in lista:
    lista[aux]*=numero
    aux+=1
print(f"Lista multuplicada por {numero}")
#Imprimir los elementos
for i in lista:
    print(f"{i}",end="-")
