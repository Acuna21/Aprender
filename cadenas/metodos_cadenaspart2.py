#Metodos para las cadenas

#Mi cadena comienza con 
cadena="Hola mundo".startswith("h")
print(cadena)

cadena="Hola mundo".startswith("hola")
print(cadena)

#Mi cadena termina con 
cadena="Hola mundo".endswith("o")
print(cadena)

cadena="Hola mundo".startswith("mundo")
print(cadena)

#Separa los elementos de la cadena, cada vez que vea un espacio
cadena="Hola mundo".split()
print(cadena)

#Separa los elementos de la cadena, cada vez que vea un espacio un -
cadena="Hola-mundo".split("-")
print(cadena)

#Separar cada elemento con un simbolo
cadena="".join("alejandro")
print(cadena)

#Remplazar
cadena="Hola-mundo".replace("a","1")
print(cadena)

