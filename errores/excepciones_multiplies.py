#Excepciones multiples
def dividir():
        while True:
            try:
                numero1=int(input("Ingrese un numero: "))
                numero2=int(input("Ingrese un numero: "))
                resultado=numero1/numero2
                print(f"Resultado: {resultado}")
            except ValueError:
                print("Error-->Digite correctamente los numeros numericos.")
            except ZeroDivisionError:
                print("Error-->No se puede dividir entre 0.")
            else:
                break   
dividir()

