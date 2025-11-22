#Dada una lista de 10 numeros, ingresada por el teclado,
# crea una nueva lista que contenga solo los números mayores a 15. 
# Imprime la lista original y la nueva lista.
#  Usa una función para capturar los valores de la lista.

def pedir_numeros():
    numeros = []
    for i in range(10):
        numeros.append(int(input(f"Ingresar un número {i + 1}:")))
    return numeros

originales = pedir_numeros()
mayores = [num for num in originales if num > 15]
print("Originales:", originales)
print("Mayores a 15:", mayores)
   
    

                                          
                                        



