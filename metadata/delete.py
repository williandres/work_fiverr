from PIL import Image
import exifread

def remove_metadata(image_path, output_path):
    image = Image.open(image_path)

    # Crea una copia de la imagen sin los metadatos
    image_without_metadata = Image.new(image.mode, image.size)
    image_without_metadata.putdata(list(image.getdata()))

    # Guarda la imagen sin metadatos
    image_without_metadata.save(output_path)

    print("Metadatos eliminados con éxito.")

def print_metadata(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)
    if tags:
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                print(f"{tag}: {tags[tag]}")
    else:
        print("No se encontraron metadatos.")

def check(filename):
    image = Image.open(filename)
    print(image.info)

# Ejemplo de uso
image_path = "/home/willian/Downloads/work/puta.png"
output_path = "/home/willian/Downloads/work/picha.png"

check(output_path)
#print_metadata(output_path)
#remove_metadata(image_path, output_path)
