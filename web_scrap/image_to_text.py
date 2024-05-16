from PIL import Image
import pytesseract

# Ruta a la imagen
image_path = 'sources/sample.png'

# Abrir la imagen usando PIL
image = Image.open(image_path)

# Usar pytesseract para hacer OCR en la imagen
text = pytesseract.image_to_string(image, lang='spa')  # 'spa' para español

# Guardar el texto en un archivo .txt
with open('sources/output.txt', 'w', encoding='utf-8') as file:
    file.write(text)

print("Texto extraído y guardado en 'output.txt'")
