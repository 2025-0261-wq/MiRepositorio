"""""Crea un programa que permita crear, leer y actualizar archivos de texto. 
El archivo debe tener la siguiente estructura:
NOMBRE: XXXXX
MATRICULA: XXXXXX
CORREO: XXXXXX
TELEFONO: XXXXXXX
Crea un menu de opciones con las siguientes opciones:
crear archivo
guardar registros
leer archivo
actualizar nombre ( permite escribir un nombre y lo busca en el archivo para reemplazarlo con otro valor)
cerrar """""
import os
# Crear el archivo
archivo = None
def crear_archivo ():
    global archivo
    nombre = input("nombre del archivo:")
    archivo = nombre + ".txt"
    with open(archivo, 'w') as f:
     f.write()
     print("Archivo creado.")
     def guardar_registros():
      if not archivo:
        print("Primero crea un archivo.")
        return
    nombre = input("NOMBRE: ")
    matricula = input("MATRICULA: ")
    correo = input("CORREO: ")
    telefono = input("TELEFONO: ")
    
    with open(archivo, 'a') as f:
        f.write(f"NOMBRE: {nombre}\n")
        f.write(f"MATRICULA: {matricula}\n")
        f.write(f"CORREO: {correo}\n")
        f.write(f"TELEFONO: {telefono}\n\n")
        print("Registro guardado.")
    #Menú de opciones
    def leer_archivo():
     if not archivo:
        print("Primero crea un archivo.")
        return
    
    with open(archivo, 'r') as f:
        print(f.read())

def actualizar_nombre():
    if not archivo:
        print("Primero crea un archivo.")
        return
    
    buscar = input("Nombre a buscar: ")
    nuevo = input("Nuevo nombre: ")
    
    with open(archivo, 'r') as f:
        contenido = f.read()
    
    if f"NOMBRE: {buscar}" in contenido:
        contenido = contenido.replace(f"NOMBRE: {buscar}", f"NOMBRE: {nuevo}")
        with open(archivo, 'w') as f:
            f.write(contenido)
        print("Nombre actualizado.")
    else:
        print("Nombre no encontrado.")

# Menu principal
while True:
    print("\n--- MENU ---")
    print("1. Crear archivo")
    print("2. Guardar registros")
    print("3. Leer archivo")
    print("4. Actualizar nombre")
    print("5. Cerrar")  
    
    opcion = input("Opcion: ")
    
    if opcion == '1':
        crear_archivo()
    elif opcion == '2':
        guardar_registros()
    elif opcion == '3':
         leer_archivo()
    elif opcion == '4':
        actualizar_nombre()
    elif opcion == '5':
        print("Adios!")
        break
    else:
        print("Opcion invalida.")


