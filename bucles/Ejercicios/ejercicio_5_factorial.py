#Factorial de un numero positivos
num=int(input("Ingrese el número para hallar su factorial: "))
while num<0:
    num=int(input("Ingrese el número para hallar su factorial. Debe ser positivo: "))
aux=False
factorial=1
while not aux:
    factorial=factorial*num
    num=num-1
    if num==1:
        aux=True
print(f"El factorial es: {factorial}")