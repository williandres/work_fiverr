import os
import functions as func
def ui():
    os.system('cls')
    print("""
    ¿Que quieres hacer?

    1. Cargar un archivo csv
    2. Consultar
    3. Salir
    """)

def run():
    ui()
    execution = True
    while execution:
        try:
            option = int(input("Escoge una opcion segun su numero: "))
            if option == 1:
                file = input("Digite el nombre su archivo(.csv) completo: ")
                print(func.upload_file(file))
            if option == 2:
                pass
            if option == 3:
                execution = False
        except ValueError:
            print("Escoga una opcion correcta")
    print("Gracias!!!")
if __name__== "__main__":
    run()