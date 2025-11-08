#Crear un programa que permita capturar n cantidad de ventas,
#  y registrar lproducto y precio para cada transacción. Mostrar o imprimir cada producto con su precio

msg = "Programa para capturar las transacciones de ventas de productos"
print("-" * 60)
print(msg)
#print("*" * 40)
print("-" * 60)

n = int(input("Digite la cantidad de ventas a capturar:\n"))
ventas = []
for i in range(n):
    producto = input(f"Digite el nombre del producto para la venta {i+1}:\n")
    precio = float(input(f"Digite el precio del producto {producto}:\n"))
    ventas.append((producto, precio))
print(ventas)