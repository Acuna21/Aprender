cadena=input("Ingrese una cadena: ")
cadena=cadena.lower()
lista=[]
for i in cadena:
    if i not in lista:#Saber si aun no esta en lalista
        lista.append(i)
print(f"Lista de caracteres sin repetir, {lista}")