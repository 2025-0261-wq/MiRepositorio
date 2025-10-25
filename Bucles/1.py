#Escribe un programa que pida al usuario que ingrese un número entero positivo. 
# El programa debe mostrar todos los números del 1 hasta el número ingresado, 
# uno por uno, utilizando un bucle while.

print("Ingrese un número entero positivo:")
numero = int(input())
while numero <= 0:
    print("Error -> Debe ser un número positivo.")
    numero = int(input("Ingrese un número entero positivo: "))

contador = 1
while contador <= numero:
    print(contador)
    contador += 1
    
    