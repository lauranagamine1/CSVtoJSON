import os
import csv
import json

def csv_a_json(ruta_csv, ruta_json):
    with open(ruta_csv, encoding='utf-8') as csv_file:
        lector = csv.DictReader(csv_file)
        datos = list(lector)
    with open(ruta_json, 'w', encoding='utf-8') as json_file:
        json.dump(datos, json_file, indent=4, ensure_ascii=False)
    print(f'Convertido: {ruta_csv} -> {ruta_json}')

def convertir_csv_en_carpeta(carpeta_csv, carpeta_json):
    os.makedirs(carpeta_json, exist_ok=True)

    for archivo in os.listdir(carpeta_csv):
        if archivo.endswith('.csv'):
            ruta_csv=os.path.join(carpeta_csv, archivo)
            nombre_base=os.path.splitext(archivo)[0]
            ruta_json=os.path.join(carpeta_json, nombre_base + '.json')

            csv_a_json(ruta_csv, ruta_json)

# carpetas
carpeta_csv = 'datos/csv'
carpeta_json = 'datos/json'

convertir_csv_en_carpeta(carpeta_csv, carpeta_json)
