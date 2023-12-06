import os
import pandas as pd

def read():
    carpeta = "sources"
    archivos = os.listdir(carpeta)
    archivo_excel = next((archivo for archivo in archivos if archivo.endswith('.xlsx') or archivo.endswith('.xls')), None)

    if archivo_excel:
        ruta_completa = os.path.join(carpeta, archivo_excel)
        data = pd.read_excel(ruta_completa)
    return data

def order(dt):
    dt = dt.sort_values(by=["Linea", "Sublineas"])
    return dt

def main():
    data = order(read())
    seccion = data.groupby(["Linea", "Sublineas"]).size().reset_index(name='Conteo')
    return [data,seccion]

if __name__ == '__main__':
    main()