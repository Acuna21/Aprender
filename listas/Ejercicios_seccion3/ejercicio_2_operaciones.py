#Ejercicio 2
'''
Ejercicio 2:
Escriba un programa que tenga dos listas y que, a continuación, cree las
siguientes listas (en las que no debe haber repeticiones):

- Lista de elementos que aparecen en las dos listas.
- Lista de elementos que aparecen en la primera lista, pero no en la segunda.
- Lista de elementos que aparecen en la segunda lista, pero no en la primera.
- Lista de elementos que aparecen en ambas listas.
'''
lista1=["Sara", "Maria", "Juan","Felipe","Medellin"]
lista2=["Barranquilla", "Bogota", "Medellin", "Cali","Sara"]
#No repetidos
conjunto1=set(lista1)
conjunto2=set(lista2)
#Lista de palabras que aparecen en las dos listas
conjunto_union=conjunto1|conjunto2
print(f"La union de las listas: {conjunto_union}")

#Palabras que aparecen en la primera lista, pero no en la segunda.
conjunto_diferencia=conjunto1-conjunto2
print(f"Los elementos del primer conjunto son: {conjunto_diferencia}")

#Plabras que aparecen en la segunda lista, pero no en la primera.
conjunto_diferencia2=conjunto2-conjunto1
print(f"Los elementos del segundo conjunto son: {conjunto_diferencia2}")

#Lista de palabras que aparecen en ambas listas
conjunto_inter=conjunto1&conjunto2
print(f"Elementos en ambas lsitas: {conjunto_inter}")