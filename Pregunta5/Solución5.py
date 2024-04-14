def guardar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "w") as file:
            for i in range(1, 11):
                file.write(f"{numero} x {i} = {numero * i}\n")
        print(f"Tabla de multiplicar del {numero} guardada en tabla-{numero}.txt")
    except Exception as e:
        print("Error al guardar la tabla de multiplicar:", e)

def mostrar_tabla(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            print(f"Tabla de multiplicar del {numero}:\n")
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def mostrar_linea_tabla(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            lines = file.readlines()
            if linea <= len(lines):
                print(f"Línea {linea} de la tabla de multiplicar del {numero}:\n")
                print(lines[linea - 1])
            else:
                print(f"La línea {linea} no existe en la tabla de multiplicar del {numero}.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def main():
    while True:
        print("\n1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de tabla de multiplicar")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla_multiplicar(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                mostrar_tabla(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea que desea mostrar: "))
            if 1 <= numero <= 10 and 1 <= linea <= 10:
                mostrar_linea_tabla(numero, linea)
            else:
                print("Los números deben estar entre 1 y 10.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
