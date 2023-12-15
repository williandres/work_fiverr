from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import lightgrey, black, white
from reportlab.lib.colors import HexColor
import math

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

    tt, st = tittle.split(': ')
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(white)
    c.drawString(15, h-52, f'{tt}')
    c.setFont("Helvetica", 14)
    z = 20
    for i in dividir_texto(st, 32).split('?'):
        c.drawString(15, h-52-z, f'{i}')
        z += 14

def dividir_texto(texto, longitud):
    tx = str(texto)
    palabras = tx.split()
    lineas = []
    linea_actual = palabras[0]

    for palabra in palabras[1:]:
        if len(linea_actual) + len(palabra) + 1 <= longitud:
            # Agregar la palabra a la línea actual si no supera la longitud límite
            linea_actual += " " + palabra
        else:
            # Agregar la línea actual y comenzar una nueva línea con la palabra actual
            lineas.append(linea_actual)
            linea_actual = palabra

    # Agregar la última línea
    lineas.append(linea_actual)

    return '?'.join(lineas)

def content(data_page):
    ver = 475
    hor = 40
    n = 0
    for i in data_page:
        n += 1
        image_path = "sources/images/" + str(i.iloc[8])
        try:
            c.drawImage(image_path, hor, ver, width=110, height=110)
        except:
            pass
        descripcion(i, ver, hor)
        hor += 150
        if n == 3:
            hor = 40
            ver -= 180
            n = 0

def dividir_string(texto, max_caracteres_por_linea):
    tx = str(texto)
    palabras = tx.split()
    lineas = []
    linea_actual = palabras[0]

    for palabra in palabras[1:]:
        if len(linea_actual) + 1 + len(palabra) <= max_caracteres_por_linea:
            linea_actual += " " + palabra
        else:
            lineas.append(linea_actual)
            linea_actual = palabra

    if linea_actual:
        lineas.append(linea_actual)

    return "\n".join(lineas)

def descripcion(data,ver,hor):
    c.setFillColor(black)
    #Codigo - Referencia
    c.setFont("Helvetica-Bold", 9)
    c.drawString(hor + 28, ver - 10, f'{data.iloc[0]} ({data.iloc[1]})')

    #Nombre
    z = 20
    c.setFont("Helvetica", 8)
    for i in dividir_string(data.iloc[2],23).split("\n"):
        c.drawString(hor + (56-(len(i)*2)), ver - z, f'{i}')
        z += 10

    #Marca
    c.setFillColor(HexColor("#004E70"))
    c.setFont("Helvetica-Bold", 9)
    c.drawString(hor + 50 - len(data.iloc[9]), ver - z, f'{data.iloc[9]}')


def page(paja, waves, tittle):
    template(waves, tittle)
    content(paja)
    c.showPage()

def pages(items):
    data = items[0]
    paja = []
    num = 0
    waves = 2 + math.ceil(len(items[1])/49)
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