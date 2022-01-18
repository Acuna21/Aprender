#Diccionarios 
"""
Colección de los elementos se guardan desordenados. Se utilizan como los diccionarios que vemos.

Caracteristicas principales
1. Clave --->No se puede duplicar
2.Valor
"""
#Diccionario vacios
diccionario={}
print(diccionario)

diccionario={"azul":"blue", "rojo":"red", "verde":"green"}
print(diccionario)

#Mostrar el valor de las claves
print(diccionario["azul"])

#Agregar valor
diccionario["amarillo"]="yellow"
print(diccionario)

#Eliminar elementos
del(diccionario["rojo"])

"""
---------------Ejemplo de agenda---------------
"""
dicci_agenda={"Sara":{"edad":19, "estatura":1.60,"peso":51}, "Neyis":[40,1.68,70], "Mary":[28,1.68,58]}

print(dicci_agenda)
print(dicci_agenda["Sara"])

