#Ejercico 1-Eliminar elemento repetidos
#Escriba un programa donde tengo una lista y que, a continuación elimine los elementos repetidos por último mostrar la lista.
#Manera 1
lista=[0,1,2,3,4,5,6,7,7,8,9,0,2,1,"Lunes", "Martes", "Miercoles", "Jueves", "Viernes","Lunes"]
conjunto=set(lista)
#Se convierte en lista nuevamente
lista=list(conjunto) 
print(lista)

#Manera 2
lista1=[0,1,2,3,4,5,6,7,7,8,9,0,2,1]
lista1=list(set(lista1))
print(lista1)