#Ejercicio tienda
precio=float(input("Ingrese el precio total de la tienda, para realizar su descuento: "))
descuento=precio*0.15
precio_total=precio-descuento
print(f"El precio total a pagar con su descuento aplicado es:{precio_total:.2f}")