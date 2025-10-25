# Escribe un programa que pida al usuario un número entero y 
# luego imprima todos los números desde ese número hasta el 0 en orden descendente utilizando un bucle while.

numero = int(input("Introduce un número entero: "))
while numero >= 0:
    print(numero)
    numero -= 1
