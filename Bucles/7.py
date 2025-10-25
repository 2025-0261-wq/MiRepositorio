#Escribe un programa que pida al usuario un número entero positivo y
#  luego imprima todos los números impares desde 1 hasta el número ingresado utilizando un bucle while.

num = int(input("Ingrese un número entero positivo: "))
if num > 0:
    i = 1
    while i <= num:
        print(i)
        i += 2
else:
    print("Por favor, ingrese un número entero positivo.")
    