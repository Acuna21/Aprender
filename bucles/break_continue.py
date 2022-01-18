#Intrucciones continue y break
"""
Continue-->Obviar lo que encuentre después de "continue" y sigue con la interacción del bucle

Break--> Rompe el bucle inmediatamente
"""
for i in range (0, 10):
    if i==5:
        continue
    print(i)
print()

for j in range (0, 10):
    if j==7:
        break
    print(j)
print("Se acabo el programa")