import os
from PIL import Image


def remove_metadata(image_path):
    image = Image.open(image_path)

    # Crea una copia de la imagen sin los metadatos
    image_without_metadata = Image.new(image.mode, image.size)
    image_without_metadata.putdata(list(image.getdata()))

    # Reemplaza la imagen original con la nueva imagen sin metadatos
    os.remove(image_path)
    image_without_metadata.save(image_path)


def process_directory(directory_path):
    nums = 0
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(root, file_name)

                # Elimina los metadatos de la imagen original
                remove_metadata(image_path)
                nums += 1

                print(f"Metadatos eliminados: {image_path} {nums}")


# Ejemplo de uso
directory_path = "/home/willian/Downloads/work/ali_sww"
process_directory(directory_path)
