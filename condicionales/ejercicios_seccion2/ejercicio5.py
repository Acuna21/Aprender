""" Cajero
Hacer un programa que simule uun cajero automatico con un saldo inicial de $1000 y tendrá las siguientes opciones en el menú: 
1.Ingresar Dinero en la cuenta
2.Retirar dinero de la cuenta
3. Mostrar dinero disponible 
4. Salir"""
operacion=0
saldo=1000
while operacion!=4:
    operacion=int(input("Que operacion desea realizar: \n1.Ingresar Dinero en la cuenta\n2.Retirar dinero de la cuenta\n3. Mostrar dinero disponible\n4. Salir\n Operacion a realizar:"))
    print()
    if operacion==1:
        saldo_a_ingresar=float(input("Ingrese la cantidad de dinero que desea ingresar a su cuenta: "))
        saldo=saldo_a_ingresar+saldo
        print(f"Saldo ingresado correctamente. Dinero total de la cuenta {saldo}")
    elif operacion==2:
        saldo_a_retirar=float(input("Ingrese la cantidad de dinero que desea retirar de su cuenta: "))
        saldo-=saldo_a_retirar
        if saldo_a_retirar>saldo:
            print("No tiene la cantidad de dinero disponible")
        else: 
            (f"Saldo retirado correctamente. Dinero total de la cuenta {saldo}\n")
    elif operacion==3:
        print(f"Su saldo actual es: {saldo}\n")
    else:
        print("Ingrese una operacion corecta")
print("Ha salido correctamente. Vuelva pronto")
("Fin de las operaciones")




