import buses as bus # buses.py
import day #  day.py
import time as ti # Libreria para calcular el tiempo

def run():
    """ Funcion de ejecucion
        -inicio = ti.time(),final = ti.time():Las usamos para capturar el tiempo preciso en sus determinados
         momentos, para luego usarlos mostrar el tiempo de ejecucion del codigo.
        
        -bus.fileCsv(20220404,20220428) : llamamos la funcion fileCsv que se encuentra en el archivo buses.py.
         Dicho archivo es el encargado de construir un csv con los id_buses que se encuentra en un cierto rango en los csv de telemetria;
         rango el cual se determina desde arg1 hasta arg2 '20220404,20220428'.
        
        -day.read_buses(20220404,20220428) : llamamos la funcion read_buses que se encuentra en el archivo day.py.
         Dicho archivo esta encargado de construir una columna por dia en el que por id_buses determine si en ese dia  fue registrado,
         tiene datos correctos, datos irregulares o sin datos. Establece una columna de cada dia por un determinado rango;
         rango el cual se determina desde arg1 hasta arg2 '20220404,20220428.
    """
    inicio = ti.time()
    bus.fileCsv(20220404,20220428)
    print(f'Todos los buses han sido registrados')
    day.read_buses(20220404,20220428)
    final = ti.time()
    print(f'Telemetria por dia construida, Tiempo de ejecucion: {round(final-inicio)} segundos')

if __name__== "__main__":
    run()