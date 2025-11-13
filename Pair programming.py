import math

while True:
    print("\n===== MENÚ DE EJERCICIOS =====")
    print("1. Mostrar asignaturas")
    print("2. Mostrar asignaturas con mensaje 'Yo estudio'")
    print("3. Pedir notas y mostrarlas por asignatura")
    print("4. Números ganadores de lotería ordenados")
    print("5. Números del 1 al 10 en orden inverso")
    print("6. Asignaturas reprobadas (eliminar aprobadas)")
    print("7. Abecedario sin posiciones múltiplo de 3")
    print("8. Comprobar si una palabra es palíndromo")
    print("9. Contar vocales en una palabra")
    print("10. Mostrar precio mayor y menor")
    print("11. Producto escalar entre dos vectores")
    print("12. Media y desviación típica de una lista")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "0":
        print("Saliendo del programa...")
        break

    elif opcion == "1":
        asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
        print("Las asignaturas son:", asignaturas)

    elif opcion == "2":
        asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
        for asignatura in asignaturas:
            print(f"Yo estudio {asignatura}")

    elif opcion == "3":
        asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
        notas = []
        for asignatura in asignaturas:
            nota = input(f"¿Qué nota has sacado en {asignatura}? ")
            notas.append(nota)
        for i in range(len(asignaturas)):
            print(f"En {asignaturas[i]} has sacado {notas[i]}")

    elif opcion == "4":
        numeros = input("Introduce los números ganadores separados por comas: ")
        numeros = [int(n) for n in numeros.split(",")]
        numeros.sort()
        print("Números ganadores ordenados:", numeros)

    elif opcion == "5":
        numeros = list(range(1, 11))
        numeros.reverse()
        print("Números en orden inverso:", ", ".join(map(str, numeros)))

    elif opcion == "6":
        asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
        reprobadas = []
        for asignatura in asignaturas:
            nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
            if nota < 70:
                reprobadas.append(asignatura)
        print("Tienes que repetir:", reprobadas)

    elif opcion == "7":
        abecedario = list("abcdefghijklmnopqrstuvwxyz")
        nueva_lista = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0]
        print("Abecedario sin posiciones múltiplo de 3:")
        print(nueva_lista)

    elif opcion == "8":
        palabra = input("Introduce una palabra: ")
        if palabra == palabra[::-1]:
            print("Es un palíndromo")
        else:
            print("No es un palíndromo")

    elif opcion == "9":
        palabra = input("Introduce una palabra: ").lower()
        for vocal in "aeiou":
            print(f"{vocal}: {palabra.count(vocal)}")

    elif opcion == "10":
        precios = [50, 75, 46, 22, 80, 65, 8]
        print("El precio menor es:", min(precios))
        print("El precio mayor es:", max(precios))

    elif opcion == "11":
        v1 = [1, 2, 3]
        v2 = [-1, 0, 2]
        producto = sum(v1[i] * v2[i] for i in range(len(v1)))
        print("El producto escalar es:", producto)

    elif opcion == "12":
        numeros = input("Introduce una muestra de números separados por comas: ")
        numeros = [float(n) for n in numeros.split(",")]
        media = sum(numeros) / len(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
        desviacion = math.sqrt(varianza)
        print(f"Media: {media}")
        print(f"Desviación típica: {desviacion:.2f}")

    else:
        print("Opción no válida. Intenta de nuevo.")
