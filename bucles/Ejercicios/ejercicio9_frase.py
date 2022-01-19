#Mostrar una frase sin espacios
frase=input("Ingrese la frase: ")
frase2=""
#Quitar espacios
for i in frase:
    if i!=" ":
        frase2+=i  #Concatena
frase=frase2
print(f"Frase final: {frase}")
print(f"El numero de caracteres es {len(frase)}")

