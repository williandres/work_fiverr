import os
import pandas as pd

def read():
    carpeta = "sources"
    archivos = os.listdir(carpeta)
    archivo_excel = next((archivo for archivo in archivos if archivo.endswith('.xlsx') or archivo.endswith('.xls')), None)

    if archivo_excel:
        ruta_completa = os.path.join(carpeta, archivo_excel)
        xls = pd.ExcelFile(ruta_completa)
        data = pd.read_excel(xls, 'Imprimir')

        # Eliminar filas que contienen NaN
        data = data.dropna()
        return data
    else:
        print("No se encontró un archivo Excel en la carpeta.")
        return None

def order(dt):
    dt = dt.sort_values(by=["Linea", "Sublineas"])
    return dt

def main():
    data = order(read())
    seccion = data.groupby(["Linea", "Sublineas"]).size().reset_index(name='Conteo')
    return [data,seccion]

if __name__ == '__main__':
    main()