#Colas

"""
Estrutura de datostipo FIFO,es decir, el primero en entrar.

Ej=Cola de bancos
"""

cola=["Sara", "Juana", "Paulo", "Beto"]
print(cola)

#Agregar elementos al final de la lista
cola.append("Mario")
print(cola)

#Sacar elementos por elprincipio de la cola
n=cola.pop(0)
print(f"Estan atendiendo a {n}")

