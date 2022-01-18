#Diccionarios 
equipo={10:"James", 9:"Falcao", 4:"Quintero"}
print(equipo)
print(equipo[9])
print()
#Si no existe la clave que buscas
print(equipo.get(10, "No existe un jugador con ese número"))
print(equipo.get(1, "No existe un jugador con ese número"))

print()
#Busquedas
print(11 in equipo)


print()
#Imprimir solo las claves
print(equipo.keys())


print()
#Imprimir solo los valores
print(equipo.values())

#Cuantos jugadores hay
print(len(equipo))

#Vaciar diccionario
equipo.clear()
print(equipo)