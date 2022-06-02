import buses as bus
import day
import time as ti

def run():
    inicio = ti.time()
    bus.fileCsv(20220404,20220428)
    print(f'Todos los buses han sido registrados')
    day.read_buses(20220404,20220428)
    final = ti.time()
    print(f'Telemetria por dia construida, Tiempo de ejecucion: {round(final-inicio)} segundos')
if __name__== "__main__":
    run()