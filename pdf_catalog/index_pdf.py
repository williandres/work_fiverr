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

def border(n):
    # Dibujar el rectángulo con relleno detrás de las letras
    rect_x = 126
    rect_y = h - 200.3
    rect_width = 355
    rect_height = 25.7
    c.setFillColor(white)
    c.setStrokeColor(HexColor("#004E70"))
    c.rect(rect_x, rect_y, rect_width, rect_height, fill=1)

    # Agregar la imagen en el extremo derecho
    image_path = "sources/assets/border.png"
    image_width = 35  # Ancho de la imagen en puntos
    image_height = 900  # Alto de la imagen en puntos
    image_x = w - image_width  # Posición X de la imagen en el extremo derecho
    image_y = 0 # Posición Y de la imagen
    c.drawImage(image_path, image_x, image_y, width=image_width, height=image_height)
    c.setFont("Courier", 12)
    c.setFillColor(black)
    c.drawString(480, 20, f'{n}')


def catalog_header():
    # Dibujar el rectángulo con relleno detrás de las letras
    rect_x = 50
    rect_y = h - 201
    rect_width = 70
    rect_height = 27
    c.setFillColor(HexColor("#38C3FF"))
    c.setStrokeColor("transparent")
    c.rect(rect_x, rect_y, rect_width, rect_height, fill=1)


    #Columnas
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(67, h-194, "Pag")
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(245, h-194, "S e c c i o n")

def catalog(datas):
    group = datas[1]
    init = 3
    dicts = {}
    for indice, fila in group.iterrows():
        if fila.iloc[2]%9 != 0 and fila.iloc[2] < 9:
            final = init
        if fila.iloc[2]%9 == 0:
            final = init + (fila.iloc[2]//9) - 1
        else:
            final = init + (fila.iloc[2]//9)
        value = f'{fila.iloc[0]}: {fila.iloc[1]}'
        key = f'{init} - {final}'
        init = final + 1
        dicts[key] = value
    hor = 520
    for i in dicts:
        c.setFont("Helvetica", 9)
        c.drawString(65, hor, i)
        c.drawString(140, hor, dicts[i])
        hor -= 10

def main(items):
    title()
    border(2)
    catalog_header()
    catalog(items)
    c.showPage()
    c.save()