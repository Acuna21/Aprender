'''
Ejercicio 3:
Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de
insertar. Por último, muestra los números ordenados de menor a mayor
'''
lista=[]
salir=False
while(not salir):
    numero=int(input("Ingrese un número: "))
    if numero==0:
        salir=True
    else:
        lista.append(numero)
#Ordenar la lista
lista.sort()
print(f"Lista ordenada: {lista}")




