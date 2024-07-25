import pandas as pd
from datetime import datetime

def combined(df_urgencias, df_habitantes, df_mortalidad, df_nacimientos, df_meteo, df_contaminantes, df_partidos):
    pass

def unify_csv():
    root = 'sources/cleaned/'
    
    # Cargar los datos de las visitas del hospital
    df_2021 = pd.read_csv(root + 'Urgencias_Limpio_Completo_2021.csv', parse_dates=['Fecha de atención'])
    df_2022 = pd.read_csv(root + 'Urgencias_Limpio_Completo_2022.csv', parse_dates=['Fecha de atención'])

        # Concatenar los datos de 2021 y 2022
    df_urgencias = pd.concat([df_2021, df_2022])
    df_urgencias.set_index('Fecha de atención', inplace=True)
    df_urgencias.sort_index(inplace=True)
    df_urgencias['Edad'] = df_urgencias['Edad'].astype(int)
    df_urgencias['Nivel de triaje'] = df_urgencias['Nivel de triaje'].astype(int)

    # Cargar los datos de demografía
    df_hombres = pd.read_csv(root + 'Total habitantes hombres Valladolid.csv')
    df_hombres['SEXO'] = 'Hombre'
    df_mujeres = pd.read_csv(root + 'Total habitantes mujeres Valladolid.csv')
    df_mujeres['SEXO'] = 'Mujer'

        # Unificar datos de población
    df_habitantes = pd.concat([df_hombres, df_mujeres])
    df_habitantes['PERIODO'] = df_habitantes['PERIODO'].astype(int)
    df_habitantes.set_index('PERIODO', inplace=True)
    df_habitantes.sort_index(inplace=True)
    df_habitantes['VALOR'] = df_habitantes['VALOR'].astype(int)

    # Cargar los datos de mortalidad
    df_mort_hombres_2021 = pd.read_csv(root + 'Tasa mortalidad por edades hombres Valladolid 2021.csv')
    df_mort_mujeres_2021 = pd.read_csv(root + 'Tasa mortalidad por edades mujeres Valladolid 2021.csv')
    df_mort_hombres_2022 = pd.read_csv(root + 'Tasa mortalidad por edades hombres Valladolid 2022.csv')
    df_mort_mujeres_2022 = pd.read_csv(root + 'Tasa mortalidad por edades mujeres Valladolid 2022.csv')

        # Unificar datos de mortalidad
    df_mortalidad = pd.concat([df_mort_hombres_2021, df_mort_mujeres_2021, df_mort_hombres_2022, df_mort_mujeres_2022])
    df_mortalidad['Periodo'] = df_mortalidad['Periodo'].astype(int)
    df_mortalidad.set_index('Periodo', inplace=True)
    df_mortalidad.sort_index(inplace=True)
    df_mortalidad['Total'] = df_mortalidad['Total'].apply(lambda x: float(str(x).replace(',','.')))
    df_mortalidad.dropna(inplace=True)

    # Cargar los datos de nacimientos
    df_nac_hombres_2021 = pd.read_csv(root + 'Nacimientos por mes hombres Valladolid 2021.csv')
    df_nac_mujeres_2021 = pd.read_csv(root + 'Nacimientos por mes mujeres Valladolid 2021.csv')
    df_nac_hombres_2022 = pd.read_csv(root + 'Nacimientos por mes hombres Valladolid 2022.csv')
    df_nac_mujeres_2022 = pd.read_csv(root + 'Nacimientos por mes mujeres Valladolid 2022.csv')

        # Unificar datos de nacimientos
    df_nacimientos = pd.concat([df_nac_hombres_2021, df_nac_mujeres_2021, df_nac_hombres_2022, df_nac_mujeres_2022])
    df_nacimientos['Periodo'] = df_nacimientos['Periodo'].astype(int)
    df_nacimientos.set_index('Periodo', inplace=True)
    df_nacimientos.sort_index(inplace=True)
    df_nacimientos['Total'] = df_nacimientos['Total'].astype(int)

    # Cargar los datos meteorológicos
    df_meteo_2021 = pd.read_csv(root + 'Meteo_Valladolid_2021_Limpio.csv', parse_dates=['date'])
    df_meteo_2022 = pd.read_csv(root + 'Meteo_Valladolid_2022_Limpio.csv', parse_dates=['date'])

        # Concatenar datos meteorológicos
    df_meteo = pd.concat([df_meteo_2021, df_meteo_2022])
    df_meteo.set_index('date', inplace=True)
    df_meteo.sort_index(inplace=True)

    # Cargar los datos de contaminantes
    df_contam_2021 = pd.read_csv(root + 'Contaminantes_2021.csv', parse_dates=['FECHA'])
    df_contam_2022 = pd.read_csv(root + 'Contaminantes_2022.csv', parse_dates=['FECHA'])

        # Concatenar datos de contaminantes
    df_contaminantes = pd.concat([df_contam_2021, df_contam_2022])
    df_contaminantes['FECHA'] = df_contaminantes['FECHA'].apply(lambda x: datetime.strptime(str(x), '%d/%m/%Y'))
    df_contaminantes.set_index('FECHA', inplace=True)
    df_contaminantes.sort_index(inplace=True)

    # Cargar los datos de partidos de fútbol
    df_partidos = pd.read_csv(root + 'Partidos.csv', parse_dates=['Fecha'])
    df_partidos.set_index('Fecha', inplace=True)

    combined(df_urgencias, df_habitantes, df_mortalidad, df_nacimientos, df_meteo, df_contaminantes, df_partidos)

def main():
    unify_csv()

if __name__ == '__main__':
    main()
