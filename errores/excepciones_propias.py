#Lanzar nuestras propias excepciones

def VerificandoEdad(edad):
    if edad<0:
        raise ValueError("La edad no puede ser negativa")
    elif edad<18:
        print("Eres muy joven")
    elif edad<30:
        print("Eres joven")
    elif edad<50:
        print("Eres madura")
edad=int(input("Ingrese edad: "))
try:
    VerificandoEdad(edad)
except ValueError as EdadNegativa:
    print(EdadNegativa)


print()
print("Programa terminado")


