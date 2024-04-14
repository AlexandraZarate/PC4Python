import requests
import zipfile
from io import BytesIO
import os

def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print("Error al descargar la imagen. Código de estado:", response.status_code)
            return None
    except Exception as e:
        print("Error al descargar la imagen:", e)
        return None

def save_image_to_zip(image_data, filename):
    try:
        with zipfile.ZipFile(f"{filename}.zip", "w") as zip_file:
            zip_file.writestr(os.path.basename(filename), image_data)
        print("Imagen almacenada como archivo zip:", f"{filename}.zip")
    except Exception as e:
        print("Error al guardar la imagen como archivo zip:", e)

def unzip_file(zip_filename, output_dir):
    try:
        with zipfile.ZipFile(zip_filename, "r") as zip_ref:
            zip_ref.extractall(output_dir)
        print("Archivo zip descomprimido en el directorio:", output_dir)
    except Exception as e:
        print("Error al descomprimir el archivo zip:", e)

def main():
    # URL de la imagen
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    
    # Descargar la imagen
    image_data = download_image(url)
    if image_data is None:
        return

    # Nombre del archivo de imagen
    image_filename = "image.jpg"
    
    # Guardar la imagen como un archivo zip
    save_image_to_zip(image_data, image_filename)

    # Descomprimir el archivo zip
    unzip_file(f"{image_filename}.zip", "unzipped")

if __name__ == "__main__":
    main()
