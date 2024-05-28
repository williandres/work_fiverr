from PIL import Image
import pytesseract

# Abrir la imagen
screenshot = Image.open('539.png')

# Configuración personalizada para Tesseract
custom_config = r'--oem 3 --psm 6'

# Usar Tesseract para extraer el texto con la configuración personalizada
text = pytesseract.image_to_string(screenshot, config=custom_config, lang='eng')

# Guardar el texto en un archivo .txt
with open('texto_extraido2.txt', 'w', encoding='utf-8') as file:
    file.write(text)

