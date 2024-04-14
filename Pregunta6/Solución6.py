def contar_lineas_codigo(archivo):
    try:
        with open(archivo, "r") as file:
            lineas = file.readlines()
            contador_lineas_codigo = 0
            for linea in lineas:
                # Eliminar espacios en blanco al principio y final de la línea
                linea = linea.strip()
                # Excluir líneas en blanco y comentarios
                if linea and not linea.startswith("#"):
                    contador_lineas_codigo += 1
            return contador_lineas_codigo
    except FileNotFoundError:
        print("El archivo no existe.")
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")

    # Verificar si la ruta termina con ".py"
    if not ruta_archivo.endswith(".py"):
        print("El archivo no es un archivo Python (.py).")
        return

    try:
        numero_lineas = contar_lineas_codigo(ruta_archivo)
        if numero_lineas is not None:
            print(f"Número de líneas de código en {ruta_archivo}: {numero_lineas}")
    except Exception as e:
        print("Ocurrió un error:", e)

if __name__ == "__main__":
    main()
