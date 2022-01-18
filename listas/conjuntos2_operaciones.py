#Conjuntos 
"""Para conjuntos vacios se inicia asi. 
a=set()
b=set()
"""

a={1,2,3}
b={3,5,6}

print(a==b)
print(len(a))

#Operaciones de conjuntos

#Union de conjuntos
c=a|b
print(c)

#Interseccion , los elementos que esta en ambos conjuntos
c=a & b
print(c)

#Diferencia: Elementos de a que no estan en b
c=a - b
print(c)

#Subconjuntos
a1={1,2,3}
b1={3,4,5}

c1={1,2,3,4,5}
print(a1.issubset(c))

#Superconjunto 
print(a1.issuperset(c))

#Ningun elemento en comun 
print(a1.isdisjoint(c))

#Inmutables
a1=frozenset({1,2,3}) #Como tuplas pero elementos unicos.
