from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()

    # Obtener la lista de fuentes disponibles
    available_fonts = figlet.getFonts()

    # Solicitar al usuario el nombre de la fuente o seleccionar aleatoriamente si no se proporciona
    font_choice = input("Ingrese el nombre de la fuente (o presione Enter para una selección aleatoria): ")
    if font_choice == "":
        font_choice = random.choice(available_fonts)
        print("Se ha seleccionado aleatoriamente la fuente:", font_choice)
    elif font_choice not in available_fonts:
        print("La fuente ingresada no está disponible. Seleccione una de las siguientes fuentes:")
        print(available_fonts)
        return

    # Solicitar al usuario el texto
    text_to_render = input("Ingrese el texto que desea imprimir: ")

    # Establecer la fuente seleccionada
    figlet.setFont(font=font_choice)

    # Imprimir el texto utilizando la fuente seleccionada
    print(figlet.renderText(text_to_render))

if __name__ == "__main__":
    main()
