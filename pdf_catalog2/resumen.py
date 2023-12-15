import os
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import lightgrey, black, white
from reportlab.lib.colors import HexColor
import PyPDF2
import math
import rest as res
import catalog_pdf as cp
import roman

# Establecer el tamaño de página personalizado
custom_page_size = (197*(2.8345323741), 259*(2.8345323741))
c = canvas.Canvas("sources/assets/resumen.pdf", pagesize=custom_page_size)

# Dibujar el contenido en el PDF
w, h = custom_page_size

def read():
    carpeta = "sources"
    archivos = os.listdir(carpeta)
    archivo_excel = next((archivo for archivo in archivos if archivo.endswith('.xlsx') or archivo.endswith('.xls')), None)

    if archivo_excel:
        ruta_completa = os.path.join(carpeta, archivo_excel)
        xls = pd.ExcelFile(ruta_completa)
        data = pd.read_excel(xls, 'Resumen')

        # Eliminar filas que contienen NaN
        data = data.dropna()
        return data
    else:
        print("No se encontró un archivo Excel en la carpeta.")
        return None

def order(dt):
    dt = dt.sort_values(by=["Linea", "Sublineas", "Tipo"])
    return dt

def main():
    data = order(read())
    seccion = [grupo for _, grupo in data.groupby('Tipo')]
    return seccion

def template(n):
    image_path = "sources/assets/border_resumen.png"
    image_width = 35  # Ancho de la imagen en puntos
    image_height = 900  # Alto de la imagen en puntos
    image_x = w - image_width  # Posición X de la imagen en el extremo derecho
    image_y = 0 # Posición Y de la imagen
    c.drawImage(image_path, image_x, image_y, width=image_width, height=image_height)

    c.setFont("Courier", 12)
    c.setFillColor(black)
    c.drawString(480, 20, f'{roman.toRoman(n)}')

    image_path = "sources/assets/header_resumen.png"
    image_width = 560  # Ancho de la imagen en puntos
    image_height = 110  # Alto de la imagen en puntos
    image_x = 0 # Posición X de la imagen en el extremo derecho
    image_y = h-110 # Posición Y de la imagen
    c.drawImage(image_path, image_x, image_y, width=image_width, height=image_height)

def content(objeto,n):
    # Imagen
    imagen = objeto.at[objeto["Imagen"].first_valid_index(), "Imagen"]
    image_path = "sources/images/" + imagen
    c.drawImage(image_path, 140, 260, width=225, height=225)

    # Titulo
    titulo = objeto.iat[0, -1]
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(black)
    f = 0
    for i in cp.dividir_texto(titulo,10).split("?"):
        c.drawString((227 + len(i)*3 ) - (len(i)-1)**2, 540-f , f'{i.upper()}')
        f += 20

    #Labels
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(black)
    c.drawString(70, 235, f'CODIGO')
    c.drawString(150, 235, f'REFERENCIA')
    c.drawString(260, 235, f'MARCA')
    c.drawString(335, 235, f'DESCRIPCION')

    h = 210
    c.setFont("Helvetica", 11)
    #Content
    for i in range(0,len(objeto)):
        codigo = objeto.iat[i, 0]
        referencia = objeto.iat[i, 1]
        marca = objeto.iat[i, -2]
        descripcion = objeto.iat[i, 2]
        if h > 50:
            c.drawString(70, h, str(codigo))
            c.drawString(150, h, referencia)
            j = 0
            for z in cp.dividir_texto(marca,10).split("?"):
                c.drawString(260, h - 10*j, z)
                j += 1
            j = 0
            for z in cp.dividir_texto(descripcion,24).split("?"):
                c.drawString(335, h - 10*j, z)
                j += 1
            h -= 50
        else:
            c.showPage()
            n += 1
            template(n)
            #Labels
            c.setFont("Helvetica-Bold", 13)
            c.setFillColor(black)
            c.drawString(70, 540, f'CODIGO')
            c.drawString(150, 540, f'REFERENCIA')
            c.drawString(260, 540, f'MARCA')
            c.drawString(335, 540, f'DESCRIPCION')
            c.setFont("Helvetica", 11)
            h = 515
            c.drawString(70, h, str(codigo))
            c.drawString(150, h, referencia)
            j = 0
            for z in cp.dividir_texto(marca,10).split("?"):
                c.drawString(260, h - 10*j, z)
                j += 1
            j = 0
            for z in cp.dividir_texto(descripcion,24).split("?"):
                c.drawString(335, h - 10*j, z)
                j += 1
            h -= 50
    return n



def resumen(catalogo):
    n = 1 #Contador de paginas
    for i in catalogo:
        template(n)
        n = content(i,n)
        n += 1
        c.showPage()

def opciones():
    while True:
        n = input("""Ingrese alguna de las siguientes opciones: 
                    [1] Agregar antes de la contraportada
                    [2] Agregar despues de la portada y el indice
                    [3] Agregar un numero de pagina en especifico
                    [4] Dejar solo en la carpeta 'Assets'
                
                  Su respuesta: """)
        if n.isdigit():
            if 2 == int(n):
                res.insert_pdf_page(2,'sources/catalogo_productos.pdf', 'sources/assets/resumen.pdf')
                break
            if 1 == int(n):
                with open('sources/catalogo_productos.pdf', 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    num_paginas = len(pdf_reader.pages)
                res.insert_pdf_page(num_paginas - 1,'sources/catalogo_productos.pdf', 'sources/assets/resumen.pdf')
                break
            if 3 == int(n):
                while True:
                    x = input("En que numero de pagina lo desea agregar: ")
                    if x.isdigit():
                        res.insert_pdf_page(int(x),'sources/catalogo_productos.pdf', 'sources/assets/resumen.pdf')
                        break
                    else:
                        if x.lower() == 'exit':
                            break
                        else:
                            print("Por favor, ingrese un número válido o escriba 'Exit' para cancelar.")
                break
            if 4 == int(n):
                break
        else:
            print("Por favor, ingrese una opcion válida")

if __name__ == '__main__':
    resumen(main())
    c.save()
    opciones()