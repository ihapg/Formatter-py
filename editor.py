import os
import json
import csv

ruta = os.path.join('tests', 'numeros.txt')


# ::: funciones :::

# __ Funcion para ordenar en base a un campo __
def sorter(array, field, reversed):
    array.sort(key=lambda x: x.get(field, ''), reverse=reversed)

# __ Funcion para guardar en archivo __
def save(array, path, json_bool):
    with open(path, 'w', encoding='utf-8') as out_file:
        if json_bool: 
            # __ archivo json __
            json.dump(array, out_file, ensure_ascii=False, indent=2)
        
        else:
            # __ archivo txt __
            for item in array:
                out_file.write(json.dumps(item, ensure_ascii=False) + '\n')

# __ Cargar elementos de JSON
def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    array_items = []
    for item in items:
        array_items.append(item)
    return array_items

# __ Funcion para filtrar por atributo y valor __
def filter_by_atr(array, atr, values):
    filtered = []
    for item in array:
        for value in values:
            if item.get(atr) == value:
                filtered.append(item)
    
    return filtered
    # return [item for item in array if item.get(atr) == value]

# __ Modificar campo __
def mod_field(array, field, values):
    array_mod = []
    for item in array:
        if field in item:
            # Modificacion para pasar array de valores y poder modificar 1:1
            # cambios en parametro value>values y values.pop(0) para ir sacando el primer elemento a la par que avanza el bucle de items
            item[field] = values.pop(0)
        array_mod.append(item)
    
    return array_mod

# __ Modificar campo Batch filtrando por Serial __
def mod_batch_serial_value(items, batch_name, serial_name, values):
    array_mod = []
    for item in items:
        if batch_name in item and serial_name in item:
            for value in values:
                if item[serial_name] == value['Serial']:
                    item[batch_name] = value['Batch']
                    array_mod.append(item)

    return array_mod

# __ Obtener valores de un campo __
def get_field_values(array, field):
    array_values = []
    for item in array:
        if field in item:
            if item[field] not in array_values:
                array_values.append(item[field])
    
    return array_values

# __ Generar números __
def num_generator_txt(ruta_archivo, inicio, fin):
    with open(ruta_archivo, 'w', encoding='utf-8') as txt:
        for numero in range(inicio, fin + 1):
            txt.write(f"{numero}\n")

# __ Pasar números de .txt a array __
def num_reader_txt(ruta_archivo):
    numeros = []
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            numero = linea.strip()
            if numero:  # Evita líneas vacías
                # numeros.append(int(numero))
                numeros.append(numero) # Para números en formato texto
    return numeros

# __ Convertir CSV (delimitado por ;) a JSON __
def csv_to_json(ruta_csv, ruta_json):
    datos = []
    with open(ruta_csv, 'r', encoding='utf-8') as csv_file:
        lector = csv.DictReader(csv_file, delimiter=';')
        for fila in lector:
            datos.append(dict(fila))
    with open(ruta_json, 'w', encoding='utf-8') as output_file:
        json.dump(datos, output_file, ensure_ascii=False, indent=2)

# ::: ejecucion pruebas :::



# Ejemplo de uso:
# csv_a_json('data/serial_sensores_batch.csv', 'data/serial_sensores_batch.json')