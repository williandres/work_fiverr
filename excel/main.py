import csv
import os
nums = [str(x) for x in range(0,10)]
exe = [" ", "(", ")", "-"]

def default(l):
    row = ['' for x in l]
    row[0] = l[0]
    row[2] = l[1]
    row[4] = l[3]
    row[5] = l[4]
    row[6] = l[5]
    row[11] = l[10]
    row[12] = l[15]
    row[13] = l[16]
    row[14] = l[17]
    row[15] = l[18]
    row[16] = l[19]
    row[17] = l[20]
    row[18] = l[21]
    row[19] = l[22]
    row[20] = l[23]
    row[21] = l[24]
    row[22] = l[25]
    row[23] = l[26]
    row[24] = l[28]
    row[25] = l[29]
    row[26] = l[30]
    row[27] = l[31]
    return row

def arrd(l, old_csv):
    l[1] = "Arrendador"
    l[3] = old_csv[2]
    l[7] = old_csv[6]
    l[8] = old_csv[7]
    l[9] = old_csv[9]
    l[10] = old_csv[8]
    return l

def arrt(l, old_csv):
    l[1] = "Arrendatario"
    l[3] = old_csv[11]

    p = 0
    t = old_csv[12].find("@")
    for i in range (0, t):
        if  old_csv[12][t-i]== " " or old_csv[12][t-i]== "," or old_csv[12][t-i]== ":":
            p = t - i
            break
    l[10] = old_csv[12][p+1:]

    m = 0
    y = m
    c = p
    tokens = 0
    for i in range(0, p):
        if old_csv[12][i] in nums or old_csv[12][i] in exe:
            tokens += 1
        if old_csv[12][i] not in nums and old_csv[12][i] not in exe:
            tokens = 0
        elif tokens == 1:
            m = i
        elif tokens > 5:
            y = m
            c = i

    l[8] = old_csv[12][y:c+1]

    return l
def fia(l, old_csv):
    l[1] = "Fiador"
    l[3] = old_csv[13]

    m = 0
    y = 0
    c = 0
    tokens = 0
    for i in range(0, len(old_csv[14])):
        if old_csv[14][i] in nums or old_csv[14][i] in exe:
            tokens += 1
        if old_csv[14][i] not in nums and old_csv[14][i] not in exe:
            tokens = 0
        elif tokens == 1:
            m = i
        elif tokens > 6:
            y = m
            c = i + 1
    l[8] = old_csv[14][y:c] 

    p = 0
    v = 0
    if "@" in old_csv[14]:
        t = old_csv[14].find("@")
        for i in range (0, t):
            if  old_csv[14][t-i]== " " or old_csv[14][t-i]== "," or old_csv[14][t-i]== ":":
                p = t - i
                p += 1
                break
        for i in range (t, len(old_csv[14])-1):
            if  old_csv[14][i]== ".":
                v = i
                v += 3
                break
        l[10] = old_csv[14][p:v]

    new = ""
    dom1 = [i for i in range(y, c)]
    dom2 = [i for i in range(p, v)]

    for i in range(len(old_csv[14])):
        if i not in dom1 and i not in dom2:
            new = new + old_csv[14][i]
    l[7] = new
    return l

def ase(l, old_csv):
    l[1] = "Asesor inmobiliario"
    l[3] = old_csv[27]
    return l

def new_csv(f):
    file = [[
            'CONTRATO (FOLIO)',
            'PERSONALIDAD',
            '¿RENOVACION?',
            'NOMBRE',
            'TOTAL',
            'IMPUESTO',
            '$',
            'DOMICILIO',
            'NUMERO CONTACTO 1',
            'NUMERO CONTACTO 2',
            'CORREO ELECTRONICO',
            'DOMICILIO INMUEBLE', #11
            'MONTO RENTA',
            'SE PAGA APARTIR DEL DIA',
            'BANCO, NUMERO DE CUENTA Y ANOMBRE DE QUIEN ESTA',
            'FECHA CONTRATO ARRENDAMIENTO',
            'FECHA ARRENDAMIENTO INICIO ',
            'VIGENCIA ARRENDAMIENTO',
            'FECHA ARRENDAMIENTO TERMINO',
            'VIGENCIA GJI', #19
            'COBERTURA',
            'MONTO OPERACIÓN',
            'MONTO EN LETRA',
            'COMISION',#23
            'INMOBILIARIA',
            'COMENTARIOS',
            'VALOR PAGARE',
            'KTOF',
            ]]
    for line in f:
        #Arrendador
        row = arrd(default(line), line)
        file.append(row)
        #Arrendatario
        row = arrt(default(line), line)
        file.append(row)
        #Fiador
        row = fia(default(line), line)
        file.append(row)
        #Asesor inmobiliario
        row = ase(default(line), line)
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