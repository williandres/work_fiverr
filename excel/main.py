import csv
import os

def default(l):
    row = [0 for x in l]
    row[0] = l[0]
    return row

def arrd(l):
    l[1] = "Arrendador"

    return l

def arrt(l):
    l[1] = "Arrendatario"

    return l
def fia(l):
    l[1] = "Fiador"

    return l
def ase(l):
    l[1] = "Asesor inmobiliario"

    return l

def new_csv(f):
    file = [[
            'CONTRATO (FOLIO)',
            'PERSONALIDAD',
            '¿RENOVACION?',
            'NOMBRE',
            'TOTAL',
            'IMPUESTO',
            'DOMICILIO',
            'NUMERO CONTACTO 1',
            'NUMERO CONTACTO 2',
            'CORREO ELECTRONICO',
            'DOMICILIO INMUEBLE',
            'MONTO RENTA',
            'SE PAGA APARTIR DEL DIA',
            'FECHA CONTRATO ARRENDAMIENTO',
            'FECHA ARRENDAMIENTO INICIO ',
            'VIGENCIA ARRENDAMIENTO',
            'FECHA ARRENDAMIENTO TERMINO',
            'VIGENCIA GJI',
            'COBERTURA',
            'MONTO OPERACIÓN',
            'MONTO EN LETRA',
            'COMISION',
            'INMOBILIARIA',
            'COMENTARIOS',
            'VALOR PAGARE',
            'KTOF',
            ]]
    for line in f:
        #Arrendador
        row = arrd(default(line))
        file.append(row)
        #Arrendatario
        row = arrt(default(line))
        file.append(row)
        #Fiador
        row = fia(default(line))
        file.append(row)
        #Asesor inmobiliario
        row = ase(default(line))
        file.append(row)

    return file

def download(new_csv):
    with open('GJI - OCT NOV DIC - Nuevo.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(new_csv)

def read_csv(file_name):
    with open(f"{file_name}","r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        tittle = next(reader)
        file = []
        for row in reader:
            file.append(row)
    return file

def main():
    old_csv = read_csv('GJI - OCT NOV DIC.xlsx - Original.csv')
    download(new_csv(old_csv))

if __name__ == '__main__':main()