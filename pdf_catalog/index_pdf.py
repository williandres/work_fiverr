from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import lightgrey, black, white
from reportlab.lib.colors import HexColor


# Establecer el tamaño de página personalizado
custom_page_size = (197*(2.8345323741), 259*(2.8345323741))
c = canvas.Canvas("sources/assets/index.pdf", pagesize=custom_page_size)

# Dibujar el contenido en el PDF
w, h = custom_page_size

def title():
    # Configurar la fuente y el tamaño del título
    c.setFont("Helvetica-Bold", 50)  # Fuente Helvetica en negrita y tamaño 50
    c.drawString((w/2)-85, h-135, "Indice")

    # Desplazar la línea hacia la izquierda
    line_x1 = (w/2) - 82  # Nueva coordenada x1 (inicio de la línea)66
    line_x2 = line_x1 + 60  # Nueva coordenada x2 (final de la línea)
    line_y = h - 150  # La coordenada y se mantiene igual
    c.line(line_x1, line_y, line_x2, line_y)

    # Desplazar la línea hacia la izquierda
    line_x1 = (w/2) - 6  # Nueva coordenada x1 (inicio de la línea)
    line_x2 = line_x1 + 63  # Nueva coordenada x2 (final de la línea)
    line_y = h - 150  # La coordenada y se mantiene igual
    c.line(line_x1, line_y, line_x2, line_y)

    c.circle(265, h - 150, 2)

def border():
    # Agregar la imagen en el extremo derecho
    image_path = "sources/assets/border.png"
    image_width = 35  # Ancho de la imagen en puntos
    image_height = 900  # Alto de la imagen en puntos
    image_x = w - image_width  # Posición X de la imagen en el extremo derecho
    image_y = 0 # Posición Y de la imagen
    c.drawImage(image_path, image_x, image_y, width=image_width, height=image_height)

def catalog_header():
    # Dibujar el rectángulo con relleno detrás de las letras
    rect_x = 50
    rect_y = h - 241
    rect_width = 127
    rect_height = 27
    c.setFillColor(HexColor("#38C3FF"))
    c.setStrokeColor("transparent")
    c.rect(rect_x, rect_y, rect_width, rect_height, fill=1)

    # Dibujar el rectángulo con relleno detrás de las letras
    rect_x = 177
    rect_y = h - 240.5
    rect_width = 260
    rect_height = 26
    c.setFillColor(white)
    c.setStrokeColor(HexColor("#004E70"))
    c.rect(rect_x, rect_y, rect_width, rect_height, fill=1)

    #Columnas
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(96, h-234, "Pag")
    c.setFont("Helvetica", 18)
    c.drawString(273, h-234, "Seccion")

def catalog():
    items = {'#-1':'Sample 1','#-2':'Sample 2','#-3':'Sample 3','#-4':'Sample 4'}
    hor = 460
    for i in items:
        c.setFont("Helvetica", 14)
        c.drawString(102, hor, i)
        c.drawString(260, hor, items[i])
        hor -= 28

if __name__ == '__main__':
    title()
    border()
    catalog_header()
    catalog()
    c.showPage()
    c.save()


