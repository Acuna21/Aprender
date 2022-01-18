#For: Numero determinado de repeticiones

for i in [1,6, 2,3,4,5]: #Recorre elemento por elemento
    print(f"Elemento: {i}")

#Valores del diccionario
diccionario={"Alejandro": 45, "Sara": 19}
for j in diccionario:
    print(f"{diccionario[j]}")


#Valores del diccionario clave y valor
print(f"{j} -> {diccionario[j]}")
for clave,valor in diccionario.items():
    print(f"{clave} -> {valor}") 
