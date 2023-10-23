numero = int(input("Introduce un numero: "))
if numero > 10:
    numero2 = int(input("Introduce otro numero: "))
    if numero2 > 10:
        print(numero+numero2)
    else:
        numero2 = int(input("Introduce otro numero: "))

else:
    numero = int(input("Introduce un numero: "))
    if numero > 10:
        print("El numero es mayor que 10.")




