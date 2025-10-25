#Escribe un programa que pida al usuario ingresar una contraseña y 
# repita la solicitud mientras la contraseña ingresada sea incorrecta. 
# El programa debe continuar hasta que el usuario ingrese la contraseña correcta. 
# Utiliza una estructura whilepara simular un do while.

contraseña_correcta = "Juan@07"
contraseña_ingresada = ""
while True:
    contraseña_ingresada = input("Ingresa la contraseña: ")
    if contraseña_ingresada == contraseña_correcta:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")

