#Condicionales combiandos
edad=int(input("Ingrese su edad: "))

if edad>0 and edad<150:
    print("Edad correcta")
    if edad>=18:
        print("Ustes es mayor de edad")
    else:
        print("Usted no es mayor de edad")
else: 
    print("Edad incorrecta.")
    
    


