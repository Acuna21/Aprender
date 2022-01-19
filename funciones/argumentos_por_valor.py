#Argumentos por valor o por referencia
def doblar_valor(numero):
    return numero*2

#Argumento por valor
n=5
resultado=doblar_valor(n)
print(resultado)


#Argumentos por referencias-COLECCIONES,LISTAS

#Se envian por referencia cualquier modificacion de la funcion afecta a lo externo. 
def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i]*=2
n=[5,10,15,20]
doblar_valores(n)
print(n)