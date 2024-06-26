import pandas as pd
import re
from collections import Counter

def find_closest_match(keyword, text_list):
    # Función para limpiar el texto eliminando saltos de línea y caracteres especiales
    def clean_text(text):
        cleaned_text = re.sub(r'\s+', ' ', text)  # Eliminar múltiples espacios en blanco
        cleaned_text = cleaned_text.replace('\n', ' ')  # Reemplazar saltos de línea con espacios
        cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)  # Eliminar caracteres especiales
        return cleaned_text.strip().lower()

    # Convertir keyword en una lista de palabras clave ordenadas por importancia
    keyword_words = keyword.lower().split()
    keyword_priority = {word: idx for idx, word in enumerate(keyword_words)}

    # Función para calcular la puntuación de coincidencia entre keyword y un texto
    def match_score(text):
        cleaned_text = clean_text(text)
        text_words = cleaned_text.split()
        score = 0
        for word in text_words:
            if word in keyword_priority:
                score += len(keyword_words) - keyword_priority[word]
        return score

    # Encontrar el texto con la puntuación de coincidencia más alta
    closest_match = max(text_list, key=match_score) if text_list else None

    return closest_match


# Leer el archivo Excel
df_categorias = pd.read_excel('sources/data_ord.xlsx', usecols="A:B", nrows=15, header=None)
df = pd.read_excel('sources/price.xlsx', usecols="B:AM", skiprows=9, nrows=623, header=None)

# Crear el encabezado manualmente
column_names = [f'Column{i+1}' for i in range(df.shape[1])]
df.columns = column_names

# Eliminar filas donde la primera columna no tenga contenido
df = df.dropna(subset=['Column1'])

# Crear el diccionario
cat_list = df_categorias.values.tolist()
for lista in cat_list:
    lista[1] = lista[1].replace('&#10;', '\n')

data_range = pd.read_excel('sources/data_ord.xlsx', usecols="B", skiprows=19, nrows=32, header=None)

# Convertir el rango a una lista
prd_list = data_range.iloc[:, 0].tolist()
modified_prd_list = []
for item in prd_list:
    if isinstance(item, str) and '\n' in item:
        item = item.replace('\n', '\n\n', 1)  # Reemplazar solo el primer salto de línea
    modified_prd_list.append(item)
# Iterar sobre las filas del DataFrame

if __name__ == '__main__':
    # aqui se crea un dataframe absoluto con las columnas: name,artikel,price y description
    absolute_df = pd.DataFrame(columns=['name', 'artikel', 'price', 'description'])
    for index, row in df.iterrows():
        # aqui se crea un dataframe temporal con las columnas: name,artikel,price y description
        temp_df = pd.DataFrame(columns=['name', 'artikel', 'price', 'description'])
        per_prod = []
        if not pd.isna(row['Column5']):
            per_prod.append([cat_list[0][0],cat_list[0][1],5])
        if not pd.isna(row['Column8']):
            per_prod.append([cat_list[1][0],cat_list[1][1],8])
            per_prod.append([cat_list[2][0],cat_list[2][1],8])
        if not pd.isna(row['Column11']):
            per_prod.append([cat_list[3][0],cat_list[3][1],11])
            per_prod.append([cat_list[4][0],cat_list[4][1],11])
        if not pd.isna(row['Column14']):
            per_prod.append([cat_list[5][0],cat_list[5][1],14])
            per_prod.append([cat_list[6][0],cat_list[6][1],14])
        if not pd.isna(row['Column17']):
            per_prod.append([cat_list[7][0],cat_list[7][1],17])
        if not pd.isna(row['Column20']):
            per_prod.append([cat_list[8][0],cat_list[8][1],20])
        if not pd.isna(row['Column23']):
            per_prod.append([cat_list[9][0],cat_list[9][1],23])
        if not pd.isna(row['Column26']):
            per_prod.append([cat_list[10][0],cat_list[10][1],26])
        if not pd.isna(row['Column29']):
            per_prod.append([cat_list[11][0],cat_list[11][1],29])
        if not pd.isna(row['Column32']):
            per_prod.append([cat_list[12][0],cat_list[12][1],32])
        if not pd.isna(row['Column35']):
            per_prod.append([cat_list[13][0],cat_list[13][1],35])
        if not pd.isna(row['Column38']):
            per_prod.append([cat_list[14][0],cat_list[14][1],38])
        for i in per_prod:
            #aqui se añaden filas al dataframe temporal
            name = row['Column1'] + ' - ' + row[f'Column{str(i[2]-2)}']
            artikel = row['Column2'] + '-' + i[0]
            price = row[f'Column{str(i[2])}']
            description = find_closest_match(name, modified_prd_list) + '\n\n' + str(i[1])
            temp_df.loc[len(temp_df)] = {'name': name, 'artikel': artikel, 'price': price, 'description': description}
        # aqui se añade los datos del dataframe temporal al datraframe absoluto
        absolute_df = pd.concat([absolute_df, temp_df], ignore_index=True)
    #aqui se imprime el resultado final de dataframe absoluto 
    absolute_df.to_excel('output.xlsx', index=False)


