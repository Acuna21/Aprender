#Tabla de multilicar
lista=[]
lista=list(range(0,11))
num=int(input("Ingrese el número para hallar su tabla de multiplicar: "))
aux=0
for i in lista:
    lista[aux]*=num
    aux+=1
print(lista)