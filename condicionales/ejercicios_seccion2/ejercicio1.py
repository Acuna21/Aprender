#Hacer un programa que ída 2 numeros y se de cuenta cual es par o si ambos son pares. 

numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese un numero: "))

if numero1%2==0 and numero2%2==0:
    print("Ambos números son pares")
elif numero1%2==0 and numero2%2!=0:
    print(f"El número {numero1} es par mientras que el número {numero2}  es impar")
elif numero1%2!=0 and numero2%2==0:
    print(f"El número {numero1} es impar mientras que el número {numero2}  es par")
else:
    print("Ningun número es par")
