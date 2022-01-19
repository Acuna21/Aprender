#Suma de digitos
suma=0
def suma_digitos(num):
    if num==0:
        resultado=0
    else:
        resultado=suma_digitos(int(num/10))+(num%10)
    return resultado
valor=suma_digitos(165)
print(valor)