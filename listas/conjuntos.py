"""Conjuntos: SON una coleccion desordenada.
 No siguen un orden. Agrega el valor donde quiera 
"""
conjunto=set()
conjunto={1,2,3,"Hola",4.56,1,2,3}

#Si se crea directemente con llaves lo toma como diccionarios. Por eso primero el.

conjunto.add(6) 
#No siguen un orden. Agrega el valor donde quiera. 

#Para eliminar elemento
conjunto.discard(6)

print(conjunto)