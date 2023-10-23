from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import lightgrey, black, white
from reportlab.lib.colors import HexColor

# Establecer el tamaño de página personalizado
custom_page_size = (197*(2.8345323741), 259*(2.8345323741))
c = canvas.Canvas("sources/assets/catalog.pdf", pagesize=custom_page_size)

# Dibujar el contenido en el PDF
w, h = custom_page_size

def template(n, tittle):
    image_path = "sources/assets/border.png"
    image_width = 35  # Ancho de la imagen en puntos
    image_height = 900  # Alto de la imagen en puntos
    image_x = w - image_width  # Posición X de la imagen en el extremo derecho
    image_y = 0 # Posición Y de la imagen
    c.drawImage(image_path, image_x, image_y, width=image_width, height=image_height)
    c.setFont("Courier", 12)
    c.setFillColor(black)
    c.drawString(480, 20, f'{n}')

    image_path = "sources/assets/header.png"
    image_width = 560  # Ancho de la imagen en puntos
    image_height = 110  # Alto de la imagen en puntos
    image_x = 0 # Posición X de la imagen en el extremo derecho
    image_y = h-110 # Posición Y de la imagen
    c.drawImage(image_path, image_x, image_y, width=image_width, height=image_height)

    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(white)
    c.drawString(15, h-100, f'{tittle}')


def page(paja, waves, tittle):
    template(waves, tittle)
    c.showPage()

def pages(items):
    data = items[0]
    paja = []
    num = 0
    waves = 3
    index = 0
    seccion = int(items[1].iloc[index, 2])
    for indice, fila in data.iterrows():
        num +=1
        paja.append(fila)
        seccion -= 1
        if len(paja) == 9 or seccion == 0:
            page(paja, waves, str(items[1].iloc[index, 0]) + ": " + str(items[1].iloc[index, 1]))
            waves += 1
            paja = []
            if seccion == 0:
                index += 1
                try:
                    seccion = int(items[1].iloc[index, 2])
                except:
                    pass

def main(items):
    pages(items)
    c.save()