import csv

def read_file(num):
    data = [["IdVehiculo","KilometrosOdometro"]]
    try:
        with open(f"./test/{num}_p60.csv","w", encoding = "utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(data)
    except FileNotFoundError:
        pass

def fileCsv():
    for i in range (20220404, 20220431):
        read_file(i)

def ord(data):
    pass

"""
ALGORITMOS 
Se puede usar el merge sort pero necesita su tiempo para entenderlo
Bubble sort
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
Binary Search
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2 #division entera

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

"""