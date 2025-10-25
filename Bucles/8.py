#Escribe un programa que imprima la serie de Fibonacci hasta el enésimo término, 
# donde el valor de n lo ingresa el usuario, utilizando un bucle for.
n = int(input("Ingrese el valor de n para la serie de Fibonacci: "))
a, b = 0, 1
print("Serie de Fibonacci hasta el término", n, ":")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
