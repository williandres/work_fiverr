import csv
import json
import re
from word2number import w2n


def separar_alfanumericos(cadena):
    # Patrón para encontrar letras y números
    patron_letras = re.compile(r'[a-zA-Z]+')
    patron_numeros = re.compile(r'\d+')

    # Encontrar todas las letras y números en la cadena
    letras_encontradas = ''.join(patron_letras.findall(cadena))
    numeros_encontrados = ''.join(patron_numeros.findall(cadena))

    return letras_encontradas, numeros_encontrados

def parse_speed(speed):
    speed_dict = {}
    partes = speed.split(',')
    partes = [parte.replace('ft.', '').strip() for parte in partes]
    try:
        speed_dict['Land'] = int(partes[0])
    except:
        speed_dict['Land'] = partes[0]
    if len(partes) > 1:
        for item in partes[1:]:
            letras, numeros = separar_alfanumericos(item)
            try:
                speed_dict[letras.capitalize()] = int(numeros)
            except:
                speed_dict['errir'] = 'errir'

    return speed_dict

def parse_stat_line(stat_line):
    stat_dict = {}
    partes = stat_line.split(',')
    for i in partes:
        letras, numeros = separar_alfanumericos(i)
        stat_dict[letras] = int(numeros)
    return stat_dict

def parse_senses(senses):
    senses_dict = {}
    partes = senses.split(',')
    partes = [parte.replace('ft.', '').strip() for parte in partes]
    for i in partes:
        letras, numeros = separar_alfanumericos(i)
        try:
            senses_dict[letras] = int(numeros)
        except:
            senses_dict['errir'] = 'errir'

    return senses_dict

def hard_acts(tuki):
    try:
        tuki= [elemento for elemento in tuki if "or range" not in elemento]
        print(tuki)
        data = {}
        primero = tuki[0].split(':')
        titulo = primero[0]
        valor = primero[1].split(',')[0]
        rango = int(re.findall(r'\d+', primero[1].split(',')[1])[0])
        tarjeta = tuki[1].replace('target', '')
        tarjeta = w2n.word_to_num(tarjeta.replace(',', ''))
        segundo = tuki[2].split(':')
        dmg = segundo[1].split(')')[0] + ')'
        tipo = ''.join(segundo[1].split(')')[1:])
        try:
            ad = ''
            for i in tuki[3:]:
                ad += i.strip() + ' '
            ad = ad.strip()
        except:
            ad = 'None'

        data[titulo.strip()] = valor.strip()
        data['Range'] = rango
        data['Targets'] = tarjeta
        data['Damage'] = dmg.strip()
        data['Damage Type'] = tipo.strip()
        if ad == '':
            ad =  'None'
        if not ad == 'None':
            data['Additional Information'] = ad
    except:
        data['ERRER'] = 'ERRER'

    return data

def soft_acts(tuki):
    polla = {}
    par = 0
    for i in tuki:
        if par == 0:
            clave = i
            par += 1
        elif par == 1:
            polla[clave.strip()] = i.strip()
            par = 0

    return polla

def liar_acts(tuki):
    polli = {}
    locowin = tuki.split(':')
    polli['Description'] = locowin[0].strip()
    try:
        loco = locowin[1].split('.')
    except:
        loco = []
    par = 0
    for i in loco:
        if par == 0:
            clave = i
            par += 1
        elif par == 1:
            polli[clave.strip()] = i.strip()
            par = 0
    return polli

def actions(actions,bonus,reactions,legendaddy,mitico,liar,region,envio):
    acts = {}
    #Actions
    acts_partes = actions.split('.')

    posiciones = []
    illo = []
    par = 0
    for indice, cadena in enumerate(acts_partes):
        if 'Attack:' in cadena:
            illo.append(indice)
        if 'Hit:' in cadena:
                illo.append(indice)
                posiciones.append(illo)
                illo = []


    extended = []
    for i in posiciones:
        fro = i[0]-1
        unti = i[1] +1
        try:
            for i in acts_partes[unti:]:
                if len(i) > 25:
                    unti += 1
                else:
                    break
        except:
            pass
        accion = acts_partes[fro:unti]
        for j in range(fro, unti):
            acts_partes[j] = ""
        extended.append([accion[0],hard_acts(accion[1:])])

    llave = ''
    lista_sin_vacios = [elemento for elemento in acts_partes if elemento != ""]
    print(lista_sin_vacios)
    for i in lista_sin_vacios:
        if len(i) < 25 and llave != '':
            try:
                acts[clave.strip()] = llave.strip()
                llave = ''
            except:
                clave = 'errur'
                acts[clave.strip()] = llave.strip()
                llave = ''
        if len(i) < 25 and llave == '':
            clave = i
        else:
            llave += i.strip() + '. '
            if i == lista_sin_vacios[-1]:
                try:
                    acts[clave.strip()] = llave.strip()
                    llave = ''
                except:
                    clave = 'errur'
                    acts[clave.strip()] = llave.strip()
                    llave = ''

    for i in extended:
        acts[i[0].strip()] = i[1]
    #bonus
    if bonus:
        acts["Bonus Actions"] = soft_acts(bonus.split('.'))
    else:
        acts["Bonus Actions"] = 'None'
    #reactions
    if reactions:
        acts["Reactions"] = soft_acts(reactions.split('.'))
    else:
        acts["Reactions"] = 'None'
    #,,
    if legendaddy:
        acts["Legendary Actions"] = soft_acts(legendaddy.split('.'))
    else:
        acts["Legendary Actions"] = 'None'
    #,
    if mitico:
        acts["Mythic Actions"] = soft_acts(mitico.split('.'))
    else:
        acts["Mythic Actions"] = 'None'
    #,liar,
    if liar:
        acts["Lair Actions"] = liar_acts(liar)
    else:
        acts["Lair Actions"] = 'None'
    #region
    if region:
        acts["Regional Effects"] = region
    else:
        acts["Regional Effects"] = 'None'
    #,envio
    if envio:
        acts["Environment"] = envio
    else:
        acts["Environment"] = 'None'

    return acts

def csv_to_json(csv_file_path, json_file_path):
    data = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            json_obj = {
                "Name": row["Name"].strip() if row["Name"] else 'None',
                "Source": row["Source"].strip() if row["Source"] else 'None',
                "Page": row["Page"].strip() if row["Page"] else 'None',
                "Size": row["Size"].strip() if row["Size"] else 'None',
                "Type": row["Type"].strip() if row["Type"] else 'None',
                "Alignment": row["Alignment"].strip() if row["Alignment"] else 'None',
                "AC": row["AC"].strip() if row["AC"] else 'None',
                "HP": row["HP"].strip() if row["HP"] else 'None',
                "Speed": parse_speed(row["Speed"]) if row["Speed"] else 'None',
                "Stats": {
                    "Strength": int(row["Strength"]) if row["Strength"] else 'None',
                    "Dexterity": int(row["Dexterity"]) if row["Dexterity"] else 'None',
                    "Constitution": int(row["Constitution"]) if row["Constitution"] else 'None',
                    "Intelligence": int(row["Intelligence"]) if row["Intelligence"] else 'None',
                    "Wisdom": int(row["Wisdom"]) if row["Wisdom"] else 'None',
                    "Charisma": int(row["Charisma"]) if row["Charisma"] else 'None'
                },
                "Saving Throws": parse_stat_line(row["Saving Throws"]) if row["Saving Throws"] else 'None',
                "Skills": parse_stat_line(row.get("Skills", "")) if row.get("Skills", "") else 'None',
                "Damage Vulnerabilities": row["Damage Vulnerabilities"].strip() if row["Damage Vulnerabilities"] else 'None',
                "Damage Resistances": row["Damage Resistances"].strip() if row["Damage Resistances"] else 'None',
                "Damage Immunities": row["Damage Immunities"].strip() if row["Damage Immunities"] else 'None',
                "Condition Immunities": row["Condition Immunities"].strip() if row["Condition Immunities"] else 'None',
                "Senses": parse_senses(row.get("Senses", "")) if row.get("Senses", "") else 'None',
                "Languages": [row["Languages"].strip()] if row["Languages"] else 'None',
                "CR": row["CR"].strip() if row["CR"] else 'None',
                "Traits": row["Traits"].strip() if row["Traits"] else 'None',
                "Actions": actions(row["Actions"],row["Bonus Actions"],row["Reactions"],row["Legendary Actions"],row["Mythic Actions"],row["Lair Actions"],row["Regional Effects"],row["Environment"]) 

            }
            data.append(json_obj)
    
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)

csv_file_path = 'sources/Bestiary.csv'
json_file_path = 'sources/Bestiary.json'
csv_to_json(csv_file_path, json_file_path)
