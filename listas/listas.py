#Listas: Son arreglos o vectores. 
lista=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", 1,2,3,4,5]
print(lista[2])

#Elemento desde el ultimo elemento
print(lista[-1]) 

#Sublista de elementos
print(lista[0:3]) 
print()
print("Lista parte 2")
lista2=[1,2,3,4,5,6]
print(lista2)
print()
#Determinar tamaño de la lista(elementos)
print(len(lista2))

#Insetar elementos
lista2.append(7)
print((lista2))

#Insertar donde quiero que vaya el elemento
lista2.insert(4,6)
print((lista2))

#Extend agrega ua lista al fianl
lista2.extend([8,9,10])
print((lista2))

#Sumar una lista
lista3=lista+lista2
print((lista3))

#Buscar valor en lista
print(3 in lista)

#En que posicion esta
print(lista2.index(3))

#cuantas veces esta un valor
print(lista2.count(3))

#Eliminar un elemento con el indice
lista2.pop(5)
print((lista2))

#Eliminar un elemento con el valor
lista2.remove(2)
print((lista2))

#Lista alrever
lista2.reverse
print((lista2))

#Ordenar lista sort ascententemente 
