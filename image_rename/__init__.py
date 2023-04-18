import os
from PIL import Image

# loop to open images and add an add metadata to each image
def main():
    for archivo in os.listdir("sources/img/"):
        if archivo.endswith(".jpg") or archivo.endswith(".webp") or archivo.endswith(".jpeg") or archivo.endswith(".gif") or archivo.endswith(".svg") or archivo.endswith(".bmp") or archivo.endswith(".tif") or archivo.endswith(".tiff") or archivo.endswith(".jfif") or archivo.endswith(".pjpeg") or archivo.endswith(".pjp") or archivo.endswith(".png"):
            ruta_archivo = os.path.join("sources/img/", archivo)
            imagen = Image.open(ruta_archivo)
            imagen.info["x"] = "y"
            imagen.info["af"] = "pada"
            imagen.save(f"sources/output/ijue.webp")


if __name__ == '__main__':
    main()