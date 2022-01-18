#Tuplas: Listas inmuutables. No se pueden modificar. No se agregan mas valores. 

#Se puede BUSCAR Con index

tupla=(4, "Lunes", 6, 10)
print(tupla)

print(tupla.index("Lunes"))

#Tranformar tupla a lista
lista=list(tupla)
print(lista)

#Tranformar lista a tupla
tupla=tuple(lista)
print(tupla)