#Funciones: Bloques de codigos que sirven para reutilizar el codigo 
#Funciones sin retorno
def saludar (nombre):
    print(f"Hola {nombre}")
#Llmar funcion
saludar("Sara")
saludar("Flor")

def tabla_multiplizar(num):
    for i in range (1,11):
        print(f"{num}*{i}={num*i}")
tabla_multiplizar(3)


