#Calculadora con dos numeos
numero1=float(input("Ingrese un numero: "))
numero2=float(input("Ingrese un segundo numero: "))
caracter=str(input("Ingrese que operacion desea realizar.  \n Recuerde que: \n S, suma \n R, resta \n P o M, multiplicacion \n D, division: \n "))
caracter=caracter.lower()
suma=resta=multiplicacion=division=0
if caracter=="s":
    suma=numero1+numero2
    print(f"La suma de los dos numeros da como resultado: {suma}")
elif caracter=="r":
    resta=numero1-numero2
    print(f"La resta de los dos numeros da como resultado: {resta}")
elif caracter=="p" or caracter=="m":
    multiplicacion=numero1*numero2
    print(f"La multiplicacion de los dos numeros da como resultado: {multiplicacion}")
elif caracter=="d":
    if numero2==0:
        numero2=int(input("Ingrese nuevamente el numero 2 ya que debe ser mayor que 0: "))
    division=numero1/numero2
    print(f"La division de los dos numeros da como resultado: {division:.3f}")
else:
    print("Se equivoco de opciones. Elija una correcta")




