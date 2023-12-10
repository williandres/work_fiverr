from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import lightgrey, black, white
from reportlab.lib.colors import HexColor
import math

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

def catalog(datas,x):
    group = datas[1]
    init = x + math.ceil(len(group)/49)
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

    #Creando los titulos y los subtitulos
    original_dict = dicts
    new_dict = {}
    titulos = []
    for key, value in original_dict.items():
        left, right = value.split(': ')
        new_dict[key] = right
        titulos.append(left)
    cuentas = {}
    for elemento in titulos:
        if elemento in cuentas:
            cuentas[elemento] += 1
        else:
            cuentas[elemento] = 1
    lista = list(new_dict.items())
    n = 0
    for key, value in cuentas.items():
        titulo = ("", key)
        lista.insert(n,titulo)
        n += int(value) + 1

    for i in lista:
        if hor > 30:
            c.setFont("Helvetica", 9)
            c.drawString(84 - 5*i[0].find("-"), hor, i[0])
            if i[0] == '':
                c.setFont("Helvetica-Bold", 9)
                c.drawString(140, hor, i[1])
            else:
                c.drawString(160, hor, '• ' + i[1])
            hor -= 10
        else:
            c.showPage()
            x += 1
            template(x)
            hor = 520

def template(n):
    title()
    border(n)
    catalog_header()

def main(items):
    template(2)
    catalog(items, 2)
    c.save()