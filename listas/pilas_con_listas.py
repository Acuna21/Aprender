"""Pilas: Escturctura de datos e python no existen directamente. Se pueden simular.

Tipo de dato tipo LIFO,ultimo en entrar primero en salir. 

Ej: Pila de libros. 
"""
pila=[1,2,3]
print(pila)

#Agregar elementos
pila.append(4)
pila.append(5)
print(pila)

#Sacar elementos por el final
pila.pop()
print(pila)

#Retornando
n=pila.pop()
print(f"Sacanado el elemento: {n}")