#Escribe un programa que pida al usuario un número entero positivo. 
# El programa debe contar cuántos dígitos tiene el número utilizando un bucle while.

print("Ingrese un número entero positivo:")
numero = int(input())
while numero <= 0:
    print("Error -> Debe ser un número positivo.")
    numero = int(input("Ingrese un número entero positivo: "))
contador_digitos = 0
while numero > 0:
    numero //= 10
    contador_digitos += 1
print("El número tiene", contador_digitos, "dígitos.")
